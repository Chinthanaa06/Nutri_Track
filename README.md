# NutriTrack — Intelligent Malnutrition Analysis and Early Risk Identification

[![CI](https://github.com/Chinthanaa06/Nutri_Track/actions/workflows/ci.yml/badge.svg)](https://github.com/Chinthanaa06/Nutri_Track/actions/workflows/ci.yml)
[![Docker](https://github.com/Chinthanaa06/Nutri_Track/actions/workflows/docker.yml/badge.svg)](https://github.com/Chinthanaa06/Nutri_Track/actions/workflows/docker.yml)

A learning-oriented screening prototype for recording child growth visits, calculating simplified growth indicators, surfacing nutritional risk flags, and tracking follow-up.

> **Screening aid only, not a medical diagnosis.** The growth calculations are a simplified educational LMS-style approximation, not the official WHO tables and not suitable for clinical decisions. Use qualified health-worker assessment and local programme protocols.

## Features
- FastAPI + SQLAlchemy API; SQLite by default and PostgreSQL in Compose.
- Streamlit interface for demo login, child registration, visit recording, dashboard and CSV export.
- WAZ/HAZ/WHZ-style approximations, rule-based categories and transparent trend score.
- Synthetic-only training pipeline comparing Logistic Regression, Random Forest and Gradient Boosting.
- Explainable screening factors and referral-oriented prompts.
- Tests, lint/format checks, Docker and GitHub Actions.

## Quick start
Python 3.11 is required.
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```
In another terminal run `streamlit run frontend/streamlit_app.py`; open http://localhost:8501.
Demo login: `demo` / `nutri-demo`.

## Docker demonstration commands
```bash
docker compose up --build -d
docker compose ps
docker image ls
docker ps -a
docker compose logs -f api
docker compose exec api sh
docker build -t nutritrack-api:demo .
docker build -f Dockerfile.frontend -t nutritrack-frontend:demo .
docker tag nutritrack-api:demo ghcr.io/OWNER/nutritrack-api:latest
docker push ghcr.io/OWNER/nutritrack-api:latest
docker compose down
```
Frontend: http://localhost:8501 · API health: http://localhost:8000/health · Swagger: http://localhost:8000/docs.

## ML and data
`python -m ml.data_gen` creates a synthetic WHO-style dataset; `python -m ml.train` compares three classifiers and saves the best estimator. `python -m ml.evaluate` writes metrics and a confusion matrix. The bundled model is created during the API Docker image build. No real patient data is included. To experiment with public data, obtain an appropriately licensed NFHS/DHS or Kaggle child nutrition dataset, verify its provenance and consent/privacy terms, map its columns to the documented features, and retrain; do not upload identifiable records.

The early-risk score is a transparent trend heuristic over visit history. Model training is synthetic demonstration only; current API classification prioritizes deterministic screening rules. Feature explanations are indicator-based, not causal explanations or SHAP values.

## GitHub Actions / zero-secret path
Push to `main` runs CI and publishes both images to GHCR using the repository's built-in `GITHUB_TOKEN`. The CD workflow then pulls the images, starts the compose stack, and verifies health plus a sample child creation. No external account or secret is required for this path. GHCR package visibility may need to be changed to public if you want unauthenticated pulls. Optional Render deploy runs only when `RENDER_DEPLOY_HOOK` is configured.

## Azure ACR/ACI alternative (optional syllabus commands)
```bash
az acr create --resource-group nutritrack-rg --name YOUR_UNIQUE_ACR --sku Basic
az acr login --name YOUR_UNIQUE_ACR
docker tag nutritrack-api:demo YOUR_UNIQUE_ACR.azurecr.io/nutritrack-api:v1
docker push YOUR_UNIQUE_ACR.azurecr.io/nutritrack-api:v1
az container create --resource-group nutritrack-rg --name nutritrack-api --image YOUR_UNIQUE_ACR.azurecr.io/nutritrack-api:v1 --registry-login-server YOUR_UNIQUE_ACR.azurecr.io --ports 8000
```

## Solo Gitflow
Run `bootstrap.ps1` on Windows PowerShell or `bash bootstrap.sh` on macOS/Linux after creating an **empty** GitHub repository (no README/license/gitignore). The script asks for your name, GitHub username and repository name once, substitutes placeholders, creates a sample Gitflow history, tags v1.0.0 and pushes. Review the generated commits before pushing if your course requires your own authored history.

## Project documents
See `docs/` for problem statement, literature survey, architecture, ML report, technical report, presentation notes, demo script, viva Q&A, checklist and UX design brief.
