#!/usr/bin/env python3
"""Read-only safety audit for Git worktrees on macOS."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Any


def run(args: list[str], timeout: int = 120) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            args,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return subprocess.CompletedProcess(args, 124, "", str(exc))


def real(path: str | Path) -> str:
    return os.path.realpath(os.fspath(path))


def is_within(item: str | Path, root: str | Path) -> bool:
    try:
        Path(real(item)).relative_to(Path(real(root)))
        return True
    except ValueError:
        return False


def discover_roots() -> list[Path]:
    home = Path.home()
    candidates: list[Path] = []
    apps = home / "apps"
    if apps.is_dir():
        for child in sorted(apps.iterdir()):
            if child.is_dir() and (child / ".git").exists():
                candidates.append(child)
    pindou = home / "pindou"
    if pindou.is_dir() and (pindou / ".git").exists():
        candidates.append(pindou)
    return candidates


def active_cwds() -> tuple[set[str], bool]:
    if not shutil.which("lsof"):
        return set(), False
    proc = run(["lsof", "-nP", "-a", "-u", str(os.getuid()), "-d", "cwd", "-Fn"])
    if proc.returncode not in (0, 1):
        # lsof commonly returns 1 when no matching files exist.
        return set(), False
    return {line[1:] for line in proc.stdout.splitlines() if line.startswith("n/")}, True


def parse_worktrees(root: Path) -> list[dict[str, str]]:
    proc = run(["git", "-C", str(root), "worktree", "list", "--porcelain"])
    if proc.returncode:
        raise RuntimeError(f"git worktree list failed for {root}: {proc.stderr.strip()}")
    entries: list[dict[str, str]] = []
    current: dict[str, str] = {}
    for line in proc.stdout.splitlines() + [""]:
        if not line:
            if current:
                entries.append(current)
                current = {}
            continue
        key, _, value = line.partition(" ")
        current[key] = value
    return entries


def github_slug(root: Path) -> str | None:
    proc = run(["git", "-C", str(root), "remote", "get-url", "origin"])
    if proc.returncode:
        return None
    match = re.search(r"github\.com[:/](.+?)(?:\.git)?$", proc.stdout.strip())
    if not match:
        return None
    slug = match.group(1)
    return slug[:-4] if slug.endswith(".git") else slug


def merged_prs(slug: str | None, online: bool) -> dict[str, int]:
    if not online or not slug or not shutil.which("gh"):
        return {}
    proc = run(
        [
            "gh",
            "pr",
            "list",
            "--repo",
            slug,
            "--state",
            "merged",
            "--limit",
            "500",
            "--json",
            "headRefName,number",
        ]
    )
    if proc.returncode:
        return {}
    try:
        return {row["headRefName"]: int(row["number"]) for row in json.loads(proc.stdout or "[]")}
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return {}


def main_is_live_current(root: Path, online: bool) -> bool:
    if not online:
        return False
    local = run(["git", "-C", str(root), "rev-parse", "origin/main"])
    remote = run(["git", "-C", str(root), "ls-remote", "origin", "refs/heads/main"])
    if local.returncode or remote.returncode or not remote.stdout.strip():
        return False
    return local.stdout.strip() == remote.stdout.split()[0]


def allocated_bytes(path: Path, enabled: bool) -> int | None:
    if not enabled or not path.exists():
        return None
    proc = run(["du", "-sk", str(path)], timeout=600)
    if proc.returncode or not proc.stdout.strip():
        return None
    try:
        return int(proc.stdout.split()[0]) * 1024
    except (ValueError, IndexError):
        return None


def audit_root(
    root: Path,
    online: bool,
    sizes: bool,
    cwds: set[str],
    cwd_detection_ok: bool,
) -> list[dict[str, Any]]:
    slug = github_slug(root)
    merged = merged_prs(slug, online)
    live_main = main_is_live_current(root, online)
    results: list[dict[str, Any]] = []

    for entry in parse_worktrees(root):
        path = Path(entry.get("worktree", ""))
        head = entry.get("HEAD", "")
        branch_ref = entry.get("branch", "")
        branch = branch_ref.removeprefix("refs/heads/") if branch_ref else ""
        is_main = real(path) == real(root)
        exists = path.is_dir()
        active = any(is_within(cwd, path) for cwd in cwds) if cwd_detection_ok else None

        status_proc = run(
            ["git", "-C", str(path), "status", "--porcelain=v1", "--untracked-files=normal"]
        )
        clean = status_proc.returncode == 0 and not status_proc.stdout
        status_ok = status_proc.returncode == 0
        contained = False
        if live_main and head:
            contained = (
                run(
                    ["git", "-C", str(root), "merge-base", "--is-ancestor", head, "origin/main"]
                ).returncode
                == 0
            )
        merged_number = merged.get(branch)

        reasons: list[str] = []
        if is_main:
            classification = "MAIN"
        elif active is None:
            classification = "KEEP_ACTIVE_UNKNOWN"
            reasons.append("lsof CWD detection unavailable")
        elif active:
            classification = "KEEP_ACTIVE"
            reasons.append("process CWD inside worktree")
        elif not exists or not status_ok:
            classification = "KEEP_STATUS_UNKNOWN"
            reasons.append(status_proc.stderr.strip() or "worktree missing or status unavailable")
        elif not clean:
            classification = "KEEP_DIRTY"
            reasons.append("tracked or untracked changes exist")
        elif contained:
            classification = "SAFE_MAIN_CONTAINS"
            reasons.append("HEAD is contained in verified-current origin/main")
        elif merged_number is not None:
            classification = "SAFE_PR_MERGED"
            reasons.append(f"GitHub PR #{merged_number} is merged")
        else:
            classification = "KEEP_CLEAN_UNPROVEN"
            reasons.append("clean and inactive but completion proof is missing")

        results.append(
            {
                "classification": classification,
                "repository": str(root),
                "path": str(path),
                "branch": branch or None,
                "head": head or None,
                "exists": exists,
                "active": active,
                "clean": clean if status_ok else None,
                "live_main_current": live_main,
                "main_contains": contained,
                "merged_pr": merged_number,
                "allocated_bytes": allocated_bytes(path, sizes),
                "reasons": reasons,
            }
        )
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", action="append", default=[], help="Main Git repository root")
    parser.add_argument(
        "--online",
        action="store_true",
        help="Verify live origin/main and merged GitHub PRs (still read-only)",
    )
    parser.add_argument("--sizes", action="store_true", help="Measure each worktree with du -sk")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of TSV")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    roots = [Path(item).expanduser().resolve() for item in args.root] or discover_roots()
    roots = list(dict.fromkeys(roots))
    if not roots:
        print("No repository roots found. Pass --root /absolute/path.", file=sys.stderr)
        return 2

    cwds, cwd_detection_ok = active_cwds()
    rows: list[dict[str, Any]] = []
    errors: list[str] = []
    for root in roots:
        if not root.is_dir() or not (root / ".git").exists():
            errors.append(f"Not a Git root: {root}")
            continue
        try:
            rows.extend(audit_root(root, args.online, args.sizes, cwds, cwd_detection_ok))
        except RuntimeError as exc:
            errors.append(str(exc))

    if args.json:
        print(json.dumps({"rows": rows, "errors": errors}, ensure_ascii=False, indent=2))
    else:
        print("classification\trepository\tpath\tbranch\thead\tactive\tclean\tbytes\treason")
        for row in rows:
            print(
                "\t".join(
                    [
                        str(row["classification"]),
                        str(row["repository"]),
                        str(row["path"]),
                        str(row["branch"] or ""),
                        str(row["head"] or ""),
                        str(row["active"]),
                        str(row["clean"]),
                        str(row["allocated_bytes"] or ""),
                        "; ".join(row["reasons"]),
                    ]
                )
            )
        if errors:
            print("\nErrors:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)

    safe = sum(row["classification"].startswith("SAFE_") for row in rows)
    kept = sum(row["classification"].startswith("KEEP_") for row in rows)
    print(f"summary: roots={len(roots)} rows={len(rows)} safe={safe} kept={kept}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
