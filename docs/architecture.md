# Architecture

```mermaid
flowchart LR
  H[Health worker] --> UI[Streamlit frontend]
  UI --> API[FastAPI REST API]
  API --> S[Screening services]
  S --> G[Growth approximations]
  S --> R[Rules and trend risk]
  S --> M[Saved sklearn model]
  API --> DB[(SQLite / PostgreSQL)]
  API --> D[Dashboard and CSV]
```

## Data flow
A health worker signs in with the seeded demo account, registers a child and records a visit. The API validates input, loads the child's sex, calculates simplified growth indicators, applies status rules and computes a history-based risk score. The visit is persisted and the result includes contributing indicators and cautious recommendations. Dashboard endpoints aggregate visits.

## ML pipeline
```mermaid
flowchart TD
  A[Synthetic generator] --> B[Feature table]
  B --> C[Train/test split]
  C --> D[Logistic Regression]
  C --> E[Random Forest]
  C --> F[Gradient Boosting]
  D --> G[Compare weighted F1]
  E --> G
  F --> G
  G --> H[Joblib model artifact]
  H --> I[Prediction service]
```

## CI/CD pipeline
```mermaid
flowchart TD
  P[Push / Pull request] --> CI[Ruff + Black + pytest]
  CI -->|main push| DO[Build API and UI images]
  DO --> SM[API smoke test]
  SM --> GHCR[Push to GHCR with GITHUB_TOKEN]
  GHCR --> CD[Compose deployment verification]
  CD --> HC[Health + sample API check]
  CD --> RENDER[Optional Render hook if secret exists]
```

The implementation uses SQLite for local development and PostgreSQL for Docker Compose. The synthetic model is for demonstration, while API category decisions use deterministic rules for transparency.
