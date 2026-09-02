# Starting a New Topic — Simple Guide

This is a short, plain-language guide for starting new work in this project using **git** (the tool that tracks changes to files) and a **terminal** (a window where you type commands).

You do not need to understand git deeply. Just follow the steps in order.

---

## What is a "branch"?

Think of the project like one long document with a full history. A **branch** is a separate copy of that document where you can make changes safely, without touching the main version, until you're ready.

- `main` = the official, finished version.
- A new branch = your own workspace for one topic (e.g. "automated report", "new icons").

You should create a new branch every time you start a new, separate topic.

---

## Step-by-step: starting a new topic

Open a terminal (Terminal.app on Mac, or the terminal panel in your editor), and make sure you're in the project folder. Then do these steps **in this order**:

### 1. Go back to the official version

```bash
git checkout main
```

This switches you to the main, up-to-date version before starting anything new.

### 2. Get the latest updates

```bash
git pull origin main
```

This downloads any changes other people may have made, so you start from the freshest version.

### 3. Create your new branch

```bash
git checkout -b category/short-description
```

Replace `category/short-description` with a real name — no `<` or `>` symbols, those are not part of the name, they were just placeholders in an example.

Examples of real names:
- `docs/automated-report`
- `figma/sync-illustrations`

Use one of these categories: `figma`, `zeroheight`, `docs`, `audit` — pick the one that best matches your topic.

**Common mistake:** if you copy-paste an example that still has `<` and `>` in it, the terminal will show a `parse error`. Just remove the angle brackets and type the real name.

### 4. Confirm which branch you're on

```bash
git branch --show-current
```

This prints the name of the branch you're currently working on. Check it matches what you just created.

---

## Step-by-step: saving and sharing your work when you're done

Once you (or Claude) have made changes and you're happy with them, do these steps **in this order**:

### 1. See what changed

```bash
git status
```

This lists every file you added or modified. Just a check — nothing is saved yet.

### 2. Stage your changes

```bash
git add my-file.md
```

"Staging" means marking a file as ready to be saved. Name the exact file(s) you changed.

### 3. Commit your changes

```bash
git commit -m "Short description of what you did"
```

A **commit** is a saved snapshot of your work, with a note explaining it. Replace the text in quotes with a short, clear sentence, e.g. `"Add automated report tutorial"`.

**Common mistake:** if you run `git commit` without doing step 2 first, git will reply:

```
nothing added to commit but untracked files present (use "git add" to track)
```

This isn't a real error — it just means nothing was staged yet, so there was nothing to save. Go back and do step 2 (`git add my-file.md`) first, then commit again.

### 4. Push your work

```bash
git push origin your-branch-name
```

**Pushing** uploads your commit from your computer to the shared online copy of the project, so others (and Claude, in other sessions) can see it. Replace `your-branch-name` with the actual branch name you created earlier — check it with `git branch --show-current` if unsure.

If this is the very first push for this branch, git may ask you to run a slightly different command instead, something like:

```bash
git push --set-upstream origin your-branch-name
```

Just copy-paste the exact command git shows you in that case.

---

## Why does `git status` show my files as "deleted" when I only renamed or moved them?

If you (or Claude) rename a file or move it to a different folder, `git status` will show it as **two separate things**, not one "renamed" line:

```
D  tokens/Colors/Border.md
?? tokens/colors-tokens/Border.md
```

- `D` (deleted) = this exact path is gone since the last commit.
- `??` (untracked) = this is a new path git has never seen before.

**Nothing is actually deleted.** Git doesn't track "this file moved" as its own kind of event — it only compares two snapshots (the last commit, and your folder right now) and reports what's different. The content itself is sitting safely at the new path; check with `ls` if you want to be sure.

Git *can* show this as a clean `renamed:` line instead, but only after you stage it:

```bash
git add -A
git status
```

**Common mistake:** don't run a "discard changes" command (like `git checkout .` or `git restore .`) while you're seeing this `D` / `??` pair and think you're "cleaning up" or "undoing a mistake." That would tell git to bring back the "deleted" files from the last commit, while leaving your new, renamed files sitting there as extra untracked files — a mess, not a fix. If the `D`/`??` pair is from an intentional rename, just stage and commit it as usual.

---

## Do I need to "switch" the chat to my new branch?

No. Claude and your terminal both look at the **same project folder on your computer**. Whatever branch is checked out in the terminal is automatically what Claude sees and works with — there is nothing extra to do.

**Careful if you have two chats open at once.** If both chats point at this same folder, they share everything — switching branches in one chat instantly changes it for the other too, since it's literally the same files on disk. Nothing is lost when this happens (all your commits stay safe), but it can be confusing. If you want two chats truly independent, see the next section.

---

## Working on two branches at the same time (using "git worktree")

Normally, one project folder can only show one branch at a time — like one open book. A **worktree** lets you open a *second* folder, connected to the exact same project (same history, nothing re-downloaded), permanently showing a *different* branch — like a second copy of the book, open to a different page. Now you can point one chat at each folder, and they never interfere with each other.

### Step-by-step: opening a second folder for another branch

Run these from inside your main project folder.

#### 1. See what folders already exist for this project

```bash
git worktree list
```

This lists every folder currently connected to this project, and which branch each one is on.

#### 2. Create a second folder for a branch that already exists

```bash
git worktree add ../GSL-Design-System-Documentation--my-branch my-branch
```

Replace `my-branch` (both places) with the real branch name, and pick any folder name you like after `../` — it just needs to not already exist. This creates a brand-new folder, sitting next to your current one, permanently checked out to that branch.

#### 3. Or: create a second folder AND a brand-new branch, in one step

```bash
git worktree add -b docs/my-new-topic ../GSL-Design-System-Documentation--my-new-topic main
```

`-b docs/my-new-topic` means "create this new branch," based on `main`, then check it out straight into the new folder.

#### 4. Confirm which branch each folder is on

```bash
git branch --show-current
```

Run this separately inside each folder to double-check. This is the same command from step 4 of "starting a new topic" above — it works the same way in every worktree folder.

### When you're done with the extra folder

```bash
git worktree remove ../GSL-Design-System-Documentation--my-branch
```

This only removes the extra folder — it does **not** delete the branch or any commits on it. The branch and its history stay safe in the project either way.

**Common mistake:** trying to open the *same* branch in two worktree folders at once. Git will refuse this — a branch can only be checked out in one folder at a time. This is a safety rail, not a bug; pick a different branch, or work in the folder that already has it.

---

## How do I know which branch a chat is on?

Once you have several chats open on different branches, it's easy to lose track of which one is which. Two ways to check, easiest first:

1. **Look at your app's branch panel, if it has one.** Some interfaces show a small status bar above the chat listing each open chat's branch name directly — a quick glance is enough.
2. **Ask, or run the command yourself — this is always the ground truth:**

```bash
git branch --show-current
```

This checks the actual state on disk at that exact moment, so it's never wrong, even if a panel display is stale or unclear. If a panel and this command ever disagree, believe the command.

---

## Quick recap (copy-paste order)

**Starting a new topic:**

```bash
git checkout main
git pull origin main
git checkout -b docs/my-new-topic
git branch --show-current
```

**Finishing and sharing your work:**

```bash
git status
git add my-file.md
git commit -m "Short description of what you did"
git push origin docs/my-new-topic
```

Do the first four steps every time you start a new, unrelated topic. Do the last four once your changes are ready to save and share.

**Opening a second folder for another branch (worktree):**

```bash
git worktree list
git worktree add ../GSL-Design-System-Documentation--my-branch my-branch
git branch --show-current
```

**Removing that extra folder when done:**

```bash
git worktree remove ../GSL-Design-System-Documentation--my-branch
```
