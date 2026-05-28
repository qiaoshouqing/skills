---
name: pr-review-loop
description: "Submit or monitor a GitHub pull request with a short polling loop that waits for automated review, fixes actionable feedback, pushes updates, and stops only when the PR has no unresolved review feedback and is merge-ready. Use when the user asks to create a PR and keep checking AI or GitHub code review suggestions every few minutes."
version: "1.1.0"
metadata:
  author: qiaoshouqing
---

# PR Review Loop

## Overview

Use this skill to turn "submit a PR and keep watching review feedback" into a closed loop. The loop should keep Git history clean, handle automated review latency, implement actionable review comments, and stop itself when there is no unresolved feedback left.

The default cadence is every 3 minutes unless the user gives a different interval.

This skill is agent-agnostic. Its core workflow relies on GitHub, `git`, `gh`, and repo-native verification commands. Persistent background monitoring is optional and depends on the current AI agent/runtime.

## Agent Compatibility

- Use the current agent's native scheduling or automation feature when it exists.
- If the agent has no persistent scheduling capability, run a bounded polling loop only while the current session is active, or tell the user that background monitoring is not available in this environment.
- Do not pretend the agent will keep checking after the session ends unless a real persistent monitor was created.
- Do not require platform-specific metadata files. Keep the skill portable unless this repository intentionally adds adapter files for every supported agent.
- When documenting or configuring monitors, use generic names like `pr-review-loop`, the repo, PR number, branch, stop condition, and verification commands. Avoid hard-coding one vendor unless it is the current runtime.

## Workflow

1. Resolve the PR and repository.
   - If a PR number or URL is provided, use it directly.
   - If no PR exists yet, create one from a clean branch after committing only the task-related files.
   - In a dirty checkout, use a fresh worktree from the PR branch or from `origin/main`; do not reset or stage unrelated user changes.

2. Inspect current state before starting a monitor.
   - Check `gh pr view <number> --repo <owner>/<repo> --json number,url,state,isDraft,mergeStateStatus,reviewDecision,statusCheckRollup,headRefName,baseRefName,title`.
   - Fetch thread-aware review state with GraphQL, not only flat PR comments:

```sh
gh api graphql \
  -f owner=<owner> \
  -f name=<repo> \
  -F number=<number> \
  -f query='query($owner:String!, $name:String!, $number:Int!) {
    repository(owner:$owner, name:$name) {
      pullRequest(number:$number) {
        reviewThreads(first: 100) {
          nodes {
            isResolved
            isOutdated
            path
            line
            comments(first: 20) {
              nodes { author { login } body createdAt }
            }
          }
        }
        reviews(first: 50) {
          nodes { author { login } state body submittedAt }
        }
        comments(first: 50) {
          nodes { author { login } body createdAt }
        }
      }
    }
  }'
```

3. Avoid duplicate monitors.
   - If the current agent exposes an automation, reminder, scheduled task, or heartbeat registry, inspect it for the PR number, branch name, and `pr-review-loop` name.
   - For Codex environments, this may include `$CODEX_HOME/automations/*/automation.toml`.
   - For other agents, use their native registry or skip this step if no persistent monitor system exists.
   - Update an existing matching monitor instead of creating another one.

4. Start a recurring monitor when the user asks for polling.
   - Prefer the current agent's native recurring monitor, heartbeat, scheduled task, reminder, or automation feature for minute-level polling.
   - Use a 3-minute cadence by default unless the user asks for a different interval.
   - If the current runtime uses RRULE schedules, `FREQ=MINUTELY;INTERVAL=3` represents the default cadence.
   - If no persistent monitor feature exists, run a bounded in-session polling loop only when practical and clearly report that it will not continue after the session ends.
   - The monitor prompt must name the repo, PR number, branch, stop condition, and test commands.

5. On every poll, choose exactly one path.
   - If the PR is closed or merged, stop the monitor and report the terminal state.
   - If automated review or checks are still pending, report a short waiting status and keep the monitor active.
   - If a review check failed because of infrastructure, quota, session limit, or timeout, rerun the latest failed review check when the current tools support it, then keep monitoring.
   - If unresolved actionable review feedback exists, implement the fix, run targeted verification, commit, push, and keep monitoring for the next review.
   - If comments are informational or ambiguous, report them separately instead of forcing a code change.
   - If there are no unresolved actionable threads, no blocking checks, and the PR is clean or mergeable, stop the monitor and report that it is ready to merge. Do not merge unless the user explicitly asked for merge.

## Fixing Feedback

- Cluster review comments by behavior or file before editing.
- Keep every code change traceable to a review thread or top-level reviewer request.
- Prefer small commits with imperative messages, for example `Fix ellipsis normalization in English uploads`.
- Do not force push, bypass failing checks, resolve threads on GitHub, or merge without explicit user permission.
- After pushing a fix, request a new automated review if the repository does not automatically review new commits. Use the repository's actual trigger phrase or integration, such as a configured bot command, only when the user has asked for an automated review loop.

## Verification

Choose the smallest checks that cover the changed surface. Prefer repo-native commands from package scripts, CI config, README, or nearby tests. Common examples include:

```sh
npm test -- --run __tests__/upload-material-routing.test.ts
npm run lint -- <changed files>
npx prisma generate
npx tsc --noEmit --pretty false
```

Report exactly what passed, what was skipped, and why.

## Stop Conditions

Stop the loop only when one of these is true:

- The PR is merged or closed.
- The PR has no unresolved actionable review threads, review checks are complete, required checks are passing, and `mergeStateStatus` is clean or otherwise mergeable.
- The same external blocker repeats across three consecutive polls and cannot be fixed without user action; report it as blocked instead of polling silently forever.
