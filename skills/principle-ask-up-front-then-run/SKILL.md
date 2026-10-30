---
name: principle-ask-up-front-then-run
description: "Apply when tempted to start building before the plan is clear, or tempted to stop mid-build to ask about reversible work."
disable-model-invocation: true
---

# Ask Up Front, Then Run

Jack plans deeply and then wants the work done without interruptions. Every question belongs before the build. None belong during it.

- **Settle what the code settles, ask the rest first.** Before building, interview Jack with the **grilling** skill until no branch of the design is left to guess. Follow precedent and make the cheap calls yourself, and list both. Ask Jack the judgement calls, each with your recommendation. Data models and anything a user sees are always judgement calls.
- **Find facts yourself.** A question you can answer by reading the code, running something, or building a quick prototype is yours, not Jack's.
- **Wait for the go.** Start building only after Jack confirms you share the understanding.
- **Then don't block.** During the build, make reasonable decisions on reversible work, proceed, and report them. Edits, commits, branches, pushes to your own branch, and opening the PR need no permission.
- **Stop only for new product calls.** If the build uncovers a product or preference decision the plan didn't cover, ask. Otherwise keep going.
- **Irreversible actions always need confirmation.** Merging, force-pushing a shared branch, deploys, deleting data, and messages sent outside the repo.
