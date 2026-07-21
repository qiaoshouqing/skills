# Cleanup Policy

## Safety tiers

| Tier | Typical items | Required evidence |
|---|---|---|
| P0 | Finished Worktrees, inactive build outputs, package caches, old installed-app installers, verified orphan temp copies | Exact path, no active/open use, reproducible or archived, immediate pre-delete recheck |
| P1 | Recent temp data, broad application caches, browser models, optional simulators | User choice or stronger app-specific evidence |
| Keep | Dirty/active/unproven Worktrees, personal data, profiles, VMs, sessions, common devices | Do not delete without an explicit, specific request |
| Admin-only | Root-owned generated residues | Report size and exact scope; require separate administrator authorization |

## Worktree proof

A removable Worktree needs independent state and completion evidence.

- State proof: inactive and Git-clean, including untracked files.
- Completion proof: HEAD is an ancestor of a live-current `origin/main`, or the matching GitHub PR is merged.
- A merged PR does not override dirty or active state.
- A clean Worktree with an open PR is not finished.
- A missing/broken `.git` pointer is not completion proof; treat it as an orphan copy and archive source first.
- Do not infer completion from modification time, branch naming, directory naming, or a stopped editor alone.

## Conductor and orphan-copy policy

Classify each depth-bounded workspace root:

1. Valid Git root: preserve when dirty; otherwise apply normal Worktree proof.
2. Broken Git pointer: archive source before cleanup.
3. No Git metadata: archive source before cleanup.
4. Open/active path: preserve regardless of category.

Recovery archives must:

- use an explicit destination outside the deleted tree;
- exclude only known rebuildable directories;
- pass gzip/tar integrity checks;
- contain every intended root;
- remain available after cleanup.

macOS `._` AppleDouble members may appear in archives. Exclude `._` components when counting logical workspace roots, but retain them in the archive.

## Active-state policy

Check more than process names:

- current working directories protect their containing Worktree/repository;
- open file handles protect the exact cache/temp directory;
- current npm/npx/pnpm/Gradle logs can explain cache regeneration;
- a background CoreSimulator service alone does not authorize device deletion;
- current Simulator, xcodebuild, XCTest, or booted devices block related cache cleanup.

If state changes during a long cleanup, recompute eligibility. Never continue from a stale candidate list.

## Permission failures

Normal `rm` may remove user-owned content and then fail on root-owned dependency files. Report all three separately:

- fully removed directories;
- unregistered or partially cleared filesystem residues;
- valid protected workspaces.

Do not count a permission-denied directory as fully removed. Do not invoke `sudo`, broad `chown`, or recursive permission changes without a separate explicit authorization and a new exact-target audit.

## Verification baseline

At minimum verify:

- `/System/Volumes/Data` before/after;
- SMART status;
- APFS snapshot category;
- final registered Worktree classifications;
- dirty-worktree preservation;
- archive integrity;
- simulator/AVD preservation;
- residue sizes;
- active cache regeneration;
- absence of lingering cleanup commands.
