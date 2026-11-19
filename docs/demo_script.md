# Five-minute demonstration script

**0:00–0:40 — Repository and code.** Open the repository in VS Code. Show `app/services/classification.py` and explain the readable rule order. Say: “The service layer keeps business rules separate from API routes.”

**0:40–1:20 — Commit and push.** Make a harmless documentation edit, then run `git add .`, `git commit -m "docs: clarify demo notes"` and `git push`. Say: “A push to main triggers the automated workflow.”

**1:20–2:20 — GitHub Actions.** Open the Actions tab. Show CI quality checks and the container build workflow. Say: “The CI job runs lint, formatting and tests. The Docker workflow builds both images and authenticates with GITHUB_TOKEN.”

**2:20–3:10 — Docker.** Show the package names in GHCR and run `docker compose up --build -d`; show `docker compose ps` and `/health`. Say: “Compose starts the database, API and Streamlit UI with health dependencies.”

**3:10–4:40 — Application.** Open `http://localhost:8501`; login with demo / nutri-demo. Add a synthetic child, record a visit and point out status, risk score, contributing factors and recommendations. Show dashboard and CSV export.

**4:40–5:00 — Safety.** Point to the disclaimer. Say: “All demo data is synthetic. Growth references are simplified, and the tool is not a medical diagnosis.”
