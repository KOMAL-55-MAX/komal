# Git Guide for Web Dev Day 2 Project

## Quick Reference

### Your Repository Status
- **Location**: `C:\Users\kshah\OneDrive\Desktop\web dev\web-dev-day2`
- **Current Branch**: master
- **Commits**: 3 commits ready
- **Git Config**: ✅ Set up (komal <kshah593731@gmail.com>)

---

## Daily Git Workflow

### 1. Check Current Status
```powershell
cd "C:\Users\kshah\OneDrive\Desktop\web dev\web-dev-day2"
git status
```

### 2. Make Changes
Edit your files (HTML, CSS, etc.)

### 3. Stage Changes
```powershell
# Stage specific file
git add index.html

# Stage all changed files
git add .

# Stage specific files
git add index.html styles.css
```

### 4. Commit Changes
```powershell
git commit -m "Description of what you changed"
```

### 5. View History
```powershell
# Compact view
git log --oneline

# Detailed view
git log

# With graph
git log --oneline --graph
```

---

## Push to GitHub

### Step 1: Create a GitHub Repository
1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **+** icon → **New repository**
3. Name it: `web-dev-day2` (or any name you prefer)
4. **DO NOT** initialize with README, .gitignore, or license (since you already have files)
5. Click **Create repository**

### Step 2: Connect Local Repo to GitHub
After creating the repo, GitHub will show you commands. Use these:

```powershell
cd "C:\Users\kshah\OneDrive\Desktop\web dev\web-dev-day2"

# Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/web-dev-day2.git

# Verify remote was added
git remote -v
```

### Step 3: Push Your Code
```powershell
# Push to GitHub (first time)
git push -u origin master

# Future pushes (just use this)
git push
```

**Note**: You'll need to authenticate. GitHub may prompt for:
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (not your password)
  - Create one at: GitHub → Settings → Developer settings → Personal access tokens

---

## Useful Git Commands

### View Changes
```powershell
# See what changed (unstaged)
git diff

# See what's staged
git diff --staged

# See changes in a file
git diff index.html
```

### View Commit Details
```powershell
# Latest commit
git show HEAD

# Specific commit
git show af528d1

# See files changed in latest commit
git show --stat HEAD
```

### Undo Changes
```powershell
# Unstage a file (keep changes)
git reset HEAD filename

# Discard changes to a file (CAREFUL!)
git checkout -- filename

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

### Branching (Optional)
```powershell
# Create new branch
git branch feature-name

# Switch to branch
git checkout feature-name

# Create and switch
git checkout -b feature-name

# List branches
git branch

# Switch back to master
git checkout master

# Merge branch into master
git merge feature-name
```

---

## Common Scenarios

### Scenario 1: Made Changes and Want to Commit
```powershell
git status                    # Check what changed
git add .                     # Stage all changes
git commit -m "Your message"  # Commit
git log --oneline             # Verify commit
```

### Scenario 2: Accidentally Staged Wrong File
```powershell
git reset HEAD filename       # Unstage
git status                    # Verify
```

### Scenario 3: Want to See What You Changed Today
```powershell
git log --since="1 day ago" --oneline
git log --author="komal" --oneline
```

### Scenario 4: Update GitHub with Latest Changes
```powershell
git add .
git commit -m "Your message"
git push
```

---

## Tips

1. **Commit Often**: Small, frequent commits are better than large ones
2. **Meaningful Messages**: Write clear commit messages
3. **Check Status**: Always run `git status` before committing
4. **Review Before Push**: Use `git log` to review before pushing

---

## Troubleshooting

### "Permission Denied" Error
- Check if you're authenticated with GitHub
- Use Personal Access Token instead of password

### "Remote Already Exists"
```powershell
git remote remove origin
git remote add origin <your-github-url>
```

### Want to Start Over?
```powershell
# Remove Git history and start fresh (CAREFUL!)
rm -rf .git
git init
```

---

## Your Current Commits

```
30b197e - Add documentation: fix-notes.md with debugging details and README.md with learning notes
2807e3e - Add broken.html for debugging practice and fixed.html with corrections
af528d1 - Add initial HTML page with header, paragraphs, list, image, and styled buttons
```

---

**Ready to push to GitHub?** Follow Step 1-3 in the "Push to GitHub" section above!
