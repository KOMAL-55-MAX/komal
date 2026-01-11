# PowerShell script to push to GitHub
# After creating a GitHub repository, run this script with your repository URL

param(
    [Parameter(Mandatory=$true)]
    [string]$RepoUrl
)

Write-Host "Adding remote repository: $RepoUrl" -ForegroundColor Green
git remote add origin $RepoUrl

Write-Host "`nChecking current branch..." -ForegroundColor Green
$currentBranch = git branch --show-current
Write-Host "Current branch: $currentBranch" -ForegroundColor Yellow

Write-Host "`nPushing to GitHub..." -ForegroundColor Green
git push -u origin $currentBranch

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Successfully pushed to GitHub!" -ForegroundColor Green
    Write-Host "Repository URL: $RepoUrl" -ForegroundColor Cyan
} else {
    Write-Host "`n❌ Error pushing to GitHub. Please check:" -ForegroundColor Red
    Write-Host "1. Repository URL is correct" -ForegroundColor Yellow
    Write-Host "2. You have authentication set up (SSH key or GitHub CLI)" -ForegroundColor Yellow
    Write-Host "3. Repository exists on GitHub" -ForegroundColor Yellow
}
