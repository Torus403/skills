### Shipping

**You own what lands. Merge only on Jack's call, and only what you verified.**

1. **Confirm the call.** Jack said to merge this PR in this conversation. "Babysit it" or "get it green" is not a merge call.
2. **Confirm it is merge-ready.** Run the **Babysit** playbook in `check` mode. Anything red goes back to Babysit `drive` first.
3. **Confirm the verification still describes the code.** If commits landed after the last verification, run the PR's evidence again on the current head with `control-ui`, `control-cli`, or the **verify-this** skill. Green CI is not a verification, because it does not run the change the way a user would.
4. **Squash-merge.** `gh pr merge <pr> --squash`. Keep the PR title as the commit subject, since it is already a Conventional Commit.
5. **Read it back.** `gh pr view <pr> --json state,mergedAt,mergeCommit`. A queued or auto-merge request is not a merge.
6. **Clean up.** Delete the remote branch if the repo doesn't do it automatically, and remove any local worktree for it.

**Reply:** what merged, the merge commit, and how you confirmed it.
