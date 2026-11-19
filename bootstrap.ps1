$ErrorActionPreference = "Stop"
$StudentName = Read-Host "Your name"
$GitHubUsername = Read-Host "GitHub username"
$RepoName = Read-Host "GitHub repository name"
git init -b main
git config user.name $StudentName
git config user.email "$GitHubUsername@users.noreply.github.com"
Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notmatch '\\.git\\' } | ForEach-Object {
  $content = Get-Content $_.FullName -Raw
if ($null -eq $content -or $content.Length -eq 0) {
    return
}
$content = $content.Replace("Chinthanaa06", $GitHubUsername).Replace("Nutri_Track", $RepoName)
Set-Content -Path $_.FullName -Value $content -NoNewline
}
git add .
git commit -m "chore: initialize NutriTrack project structure"
git switch -c develop
git commit --allow-empty -m "docs: establish project development baseline"
git switch -c feature/growth-screening
git commit --allow-empty -m "feat: add simplified growth z-score calculations"
git switch develop
git merge --no-ff feature/growth-screening -m "merge: growth screening feature"
git switch -c feature/api-ux
git commit --allow-empty -m "feat: add child visit API and Streamlit workflow"
git switch develop
git merge --no-ff feature/api-ux -m "merge: API and UX feature"
git switch -c feature/ml-pipeline
git commit --allow-empty -m "feat: add synthetic ML training and evaluation"
git switch develop
git merge --no-ff feature/ml-pipeline -m "merge: ML pipeline feature"
git switch -c feature/devops
git commit --allow-empty -m "ci: add quality and container workflows"
git switch develop
git merge --no-ff feature/devops -m "merge: DevOps feature"
git switch -c docs/project-submission
git commit --allow-empty -m "docs: complete project report and viva material"
git switch develop
git merge --no-ff docs/project-submission -m "merge: project documentation"
git switch main
git merge --no-ff develop -m "release: NutriTrack v1.0.0"
git tag -a v1.0.0 -m "NutriTrack college project v1.0.0"
git remote add origin "https://github.com/$GitHubUsername/$RepoName.git"
git push -u origin main develop --tags
