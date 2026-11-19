#!/usr/bin/env bash
set -euo pipefail
read -rp "Your name: " STUDENT_NAME
read -rp "GitHub username: " Chinthanaa06
read -rp "GitHub repository name: " Nutri_Track
git config user.name "$STUDENT_NAME"
git config user.email "${Chinthanaa06}@users.noreply.github.com"
find . -type f ! -path './.git/*' -print0 | xargs -0 sed -i "s/Chinthanaa06/$Chinthanaa06/g; s/Nutri_Track/$Nutri_Track/g"
sed -i "s/@Chinthanaa06/@$Chinthanaa06/" .github/CODEOWNERS
git init -b main
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
git remote add origin "https://github.com/$Chinthanaa06/$Nutri_Track.git"
git push -u origin main develop --tags
