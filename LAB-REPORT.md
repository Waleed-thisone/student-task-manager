# Lab Report — Student Task Manager

**Course:** CSC418 DevOps for Cloud Computing — Lab Assignment 4
**Student:** Muhammad Waleed (SP23-BSE-134)
**Repository:** https://github.com/Waleed-thisone/student-task-manager

## 1. Git vs GitHub, and the purpose of add, commit and push

Git is a distributed version control system that runs on my own machine. It records the history of my files as commits, lets me create branches, and lets me undo changes — all of this works completely offline. GitHub is a hosting service on the internet where Git repositories are stored and shared. GitHub adds collaboration features on top of Git, such as Issues, Pull Requests, code review and GitHub Actions. In short: Git is the tool that tracks changes; GitHub is the place where the tracked project lives and where the team works around it.

The three basic commands form a pipeline. `git add` stages changes, meaning it selects exactly which modified files will go into the next snapshot. `git commit` saves that snapshot into the local repository history with a message explaining the change. `git push` uploads the local commits to GitHub so the work is backed up and visible to others. Nothing reaches GitHub until it is pushed, and nothing is committed until it is added first.

## 2. Why branches and Pull Requests are used, and what causes merge conflicts

A branch is an independent line of development. In this project each feature (add, complete, delete) was built on its own branch, so unfinished work never broke the working code on `main`, several features could progress independently, and each branch could be finished, tested and reviewed at its own pace. If an experiment on a branch fails, the branch can simply be deleted without harming `main`.

A Pull Request is a proposal to merge one branch into another. It shows exactly which files changed, lets the work be reviewed and discussed before it lands, links the change to the Issue it solves, and triggers the automated tests. Merging only happens after that check, which keeps `main` stable.

A merge conflict happens when two branches change the same part of the same file in different ways, starting from the same original version. Git cannot guess which version is correct, so it stops and marks the conflicting area with `<<<<<<<`, `=======` and `>>>>>>>` markers for a human to decide. This project created one deliberately: two branches changed the README line `Project status: Planning` to different values. When the second branch was merged after the first, Git reported a conflict, and I resolved it by keeping the status that reflected the project's real state and merging the result.

## 3. Fetch vs pull, and merge vs rebase

`git fetch` only downloads new commits and branch information from GitHub into the local repository — it does not touch my working files, so I can inspect what changed before accepting it. `git pull` is fetch plus merge: it downloads the changes and immediately merges them into my current branch, updating my files.

`git merge` combines two branches by creating a merge commit with two parents; the full history, including the branch, stays visible. `git rebase` instead replays my commits one by one on top of the other branch, producing a straight, linear history as if I had started from the latest code — but it rewrites my commits, so it should not be used on commits that other people already have.

## 4. How GitHub Issues and Actions help a development team

Issues turn vague ideas and bugs into tracked units of work: each one has a clear description, a label (for example `enhancement` or `documentation`), and a visible open/closed state. Linking Pull Requests to Issues (`Closes #1`) means finished work closes its Issue automatically, and anyone can see what is being worked on, what is done, and what is left.

GitHub Actions automates the repetitive checks. In this project a workflow runs the unit tests on every push and every Pull Request to `main`. The team gets an objective pass/fail signal on every change without anyone running tests by hand, so broken code is caught before it is merged, and the run history shows exactly which commit introduced a failure.

## 5. One difficulty I faced and how I solved it

My first GitHub Actions run failed. The test for adding a task expected the first task to get ID `0`, but the application hands out IDs starting from `1`, so the test failed with `AssertionError: 1 != 0`. I read the failed run's log in the Actions tab, compared it with the `TaskManager` code, and realised the mistake was in my test's expectation, not in the application. I corrected the assertion to expect ID `1` and pushed the fix; the next run passed all three tests. This showed me why automated testing is useful: the failure was caught by CI immediately, with a log that pointed at the exact line.
