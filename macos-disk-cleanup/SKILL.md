---
name: macos-disk-cleanup
description: Safely analyze and clean a nearly full macOS disk, with special handling for Git Worktrees, Codex/Claude worktrees, Conductor workspaces, build artifacts, package caches, Xcode/CoreSimulator data, Android AVDs, installers, temporary directories, active processes, and root-owned residues. Use when the user says the Mac disk is full, asks for a deep disk-space analysis, wants cleanup candidates graded by safety, approves P0/high-confidence cleanup, or suspects many project Worktrees are consuming space.
---

# macOS Disk Cleanup

Perform a two-phase, evidence-driven cleanup: analyze and rank first, then execute only the scope the user approves. Treat source code, personal data, active developer state, and simulator/device data as protected by default.

## Non-negotiable rules

- Measure live state every run. Never reuse old sizes, process state, PR state, or free-space figures as current truth.
- Do not delete during an analysis-only request.
- Never classify a Worktree as finished from age, name, or a clean status alone.
- Before every Worktree removal, require all three:
  1. no process has a current working directory inside it;
  2. `git status --porcelain=v1 --untracked-files=normal` is empty;
  3. its HEAD is contained in a verified-current remote main ref, or its matching GitHub PR is merged.
- Recheck those conditions immediately before deletion. A preflight snapshot is not enough.
- Use `git worktree remove <exact-path>` without `--force`, then `git worktree prune`. Do not delete branches unless separately requested.
- Never run destructive commands against `$HOME`, `~`, a workspace root, a glob, a command substitution, or an unresolved variable. Resolve and validate every exact target first.
- Do not invoke `sudo`, change ownership, or weaken permissions automatically. Report root-owned residues separately.
- Do not delete active caches, open files, personal media, messages, browser profiles, virtual machines, app sessions, common simulators, Android AVDs, or data with uncertain recovery value.
- Preserve dirty worktrees even when their PR is merged or HEAD is in main.

Read [references/cleanup-policy.md](references/cleanup-policy.md) when assigning risk tiers, handling Conductor workspaces, or deciding what must remain.

## Phase 1: Establish live truth

Start with read-only checks:

1. Record `/System/Volumes/Data` capacity, used space, free space, and percentage.
2. Check SMART status and local APFS snapshots. Treat OS update snapshots separately from user-data snapshots.
3. List active process current working directories with `lsof`.
4. Check Trash without assuming it is large.
5. Measure targeted high-yield paths before broad scans. Prefer `gdu`, `du -x`, max-depth scans, and exact known directories over unrestricted recursive scans.
6. Inspect package/build caches, `/private/tmp`, the user's per-session `/private/var/folders/.../X`, developer directories, Downloads installers, and project/worktree roots.

Never chain analysis into deletion unless the user already authorized execution.

## Phase 2: Audit Worktrees

Discover the real repository families first. Include ordinary repos and their `.codex`, `.claude`, sibling, and `/private/tmp` worktrees.

Run the bundled read-only auditor with every main repository root:

```bash
python3 scripts/audit_worktrees.py --online \
  --root /absolute/path/to/repo-a \
  --root /absolute/path/to/repo-b
```

Use `--sizes` only when per-worktree sizing is worth the scan cost. Use `--json` for machine-readable output.

Interpret classifications conservatively:

- `SAFE_MAIN_CONTAINS`: clean, inactive, and HEAD is in a local `origin/main` that exactly matches live `ls-remote`.
- `SAFE_PR_MERGED`: clean, inactive, and the branch has a merged GitHub PR.
- `KEEP_ACTIVE`: a process CWD is inside the Worktree.
- `KEEP_DIRTY`: tracked or untracked changes exist.
- `KEEP_CLEAN_UNPROVEN`: clean and inactive, but merge/completion proof is missing.
- `KEEP_ACTIVE_UNKNOWN`: active-process detection was unavailable; do not delete.

An initially active Worktree may become eligible later only after a fresh audit proves it inactive, clean, and merged/current-main. State this explicitly in the report.

When multiple repositories are cleaned concurrently, use at most one removal worker per repository root. Never run concurrent `git worktree` mutations against the same repository metadata.

## Phase 3: Build a graded plan

Report actual measured sizes and separate overlap where possible.

- **P0 / high confidence:** proven-finished Worktrees; inactive generated `.next`, `.open-next`, build, dist, DerivedData, package caches; verified installed-app installers; old unregistered temporary copies after source recovery; inactive Xcode caches while preserving devices/runtimes.
- **P1 / conditional:** recent temp data, general app caches, browser models, stopped-but-unproven project copies, simulator devices the user may still need.
- **Keep:** active/dirty/unproven Worktrees, WeChat/messages, photos/videos, browser profiles, VMs, Claude/Codex sessions, current npm/build caches, common simulators, Android AVDs, and unknown data.
- **Admin-only residue:** root-owned generated files that normal permissions cannot remove.

Include a reclaim estimate, but distinguish logical directory totals from APFS free-space change and hardlink-deduplicated totals.

## Phase 4: Execute approved P0 in stages

### 1. Standard Git Worktrees

For each exact candidate:

1. Re-read active CWDs.
2. Recheck clean status and unchanged HEAD.
3. Reconfirm live main containment or merged PR proof.
4. Run non-force `git worktree remove`.
5. Record success, safety skip, or permission failure.
6. Prune only after removals.

If Git unregisters a Worktree but leaves root-owned generated files, label it as an unregistered filesystem residue rather than a preserved Worktree.

### 2. Conductor workspaces and unregistered project copies

Preserve every valid Git workspace with changes. For invalid/broken/no-Git workspaces:

1. Establish the exact directory set and verify none are active or open.
2. Create a recovery archive containing source and non-rebuildable files.
3. Exclude rebuildable directories such as `node_modules`, `.next`, `.open-next`, build, dist, `.turbo`, `.dart_tool`, coverage, target, Pods, and caches.
4. Verify the archive with `gzip -t`, list its members, and confirm every intended workspace root appears.
5. Revalidate the exact set after archive creation.
6. Delete only the archived exact roots.
7. Preserve and measure root-owned residues if deletion is denied.

Do not claim an orphan directory was fully removed when only its user-owned portion disappeared.

### 3. Generated caches and temporary data

Before deleting each exact cache:

- verify it is not a symlink;
- check for open files and active project roots;
- record allocated size;
- delete only the exact generated directory;
- verify it is absent or measure the residue.

For `.next`, skip the entire repository when a process CWD is within that repository. For npm/Gradle/pnpm caches, recheck running build processes. If a cache regenerates, inspect logs: retain it when it belongs to current activity.

For Xcode/CoreSimulator:

- preserve installed runtimes and common simulator devices unless the user explicitly approves device deletion;
- require devices to be Shutdown and no Simulator/xcodebuild/XCTest activity before clearing caches;
- verify devices still exist afterward.

For installers, confirm the corresponding application/input method is installed and the image is not mounted before deleting the installer.

## Phase 5: Verify and report

Do not call the cleanup complete until all checks pass:

1. Re-run disk usage and report before/after free space and capacity.
2. Re-run the Worktree auditor. There should be no remaining safe candidate inside the approved scope.
3. Confirm representative dirty and active Worktrees still exist with their changes.
4. Confirm recovery archives pass integrity checks and provide clickable paths.
5. Confirm preserved iOS devices, runtimes, and Android AVDs still exist.
6. Confirm no cleanup processes remain.
7. Measure permission residues and current regenerated caches.
8. Report SMART and snapshot state without deleting OS update snapshots.

Lead with the measured outcome. Then summarize removed categories, protected items, recoverable archives, and any exact blocker requiring administrator authorization.
