# Quick Steps to Push to GitHub

## You're at this step:
✅ Local repository ready  
✅ GitHub repository created  
⏭️ **Next: Connect and push**

---

## Commands to Run (in PowerShell)

### 1. Navigate to your project
```powershell
cd "C:\Users\kshah\OneDrive\Desktop\web dev\web-dev-day2"
```

### 2. Add GitHub as remote
**Replace `YOUR_USERNAME` and `REPO_NAME` with your actual values:**
```powershell
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

**Example:**
```powershell
git remote add origin https://github.com/komal/web-dev-day2.git
```

### 3. Verify remote was added
```powershell
git remote -v
```
You should see your GitHub URL listed.

### 4. Push your code
```powershell
git push -u origin master
```

---

## If you get errors:

### "Remote 'origin' already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

### Authentication Issues
- GitHub may ask for username and password
- **Don't use your GitHub password!**
- Use a **Personal Access Token** instead
- Create one: GitHub → Settings → Developer settings → Personal access tokens → Generate new token

---

## After pushing, verify:
1. Go to your GitHub repository page
2. Refresh the page
3. You should see all your files!

---

**Need help?** Tell me your GitHub username and I'll give you the exact command! 🚀
