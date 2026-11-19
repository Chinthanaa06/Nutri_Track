# Git lab viva demo
Use these six commands in a disposable demo branch; make a harmless text edit between commands.

1. `git switch develop` — move to integration branch.
2. `git switch -c feature/viva-demo` — create a feature branch.
3. `git add . && git commit -m "feat: add viva demo note"` — commit the change.
4. `git switch develop && git merge --no-ff feature/viva-demo` — demonstrate merge history.
5. `git switch -c feature/conflict-demo`; edit the same line in two branches, merge, resolve markers, then `git add GIT_DEMO.md && git commit -m "fix: resolve demo merge conflict"` — explain conflict resolution.
6. `git switch feature/viva-demo && git rebase develop` — replay feature commit on latest develop (do not rebase shared branches).
