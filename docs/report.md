# NutriTrack — Technical Project Report

## Abstract
NutriTrack is a learning prototype for recording child growth visits and highlighting nutritional screening concerns. It combines a Streamlit interface, FastAPI backend, SQLAlchemy persistence, simplified growth indicators, deterministic rules, a trend-based risk score and a synthetic scikit-learn training pipeline. The project demonstrates full-stack engineering and basic MLOps automation.

## 1. Introduction
Repeated child measurements can be more informative than isolated values. NutriTrack demonstrates how digital visit records can make longitudinal review and follow-up lists easier to inspect.

## 2. Problem definition
The project addresses the difficulty of organizing growth measurements and identifying records that warrant review. It is not a clinical decision system.

## 3. Literature
The design is informed by WHO child growth standards, WHO nutrition guidance, UNICEF/WHO/World Bank malnutrition estimates, SHAP explainability literature and MLOps/continuous-delivery literature. See `literature_survey.md`.

## 4. System design
The Streamlit frontend communicates with a FastAPI REST API. SQLAlchemy stores child and visit entities in SQLite or PostgreSQL. Service modules isolate growth calculations, rules, trend risk and explanations.

## 5. Implementation
Input validation constrains ages and measurements. The API calculates simplified WAZ/HAZ/WHZ-style scores, classifies screening status and records a risk score based on the latest visit and previous visit. Dashboard endpoints provide counts, category distribution, high-risk items and CSV export. The ML scripts generate synthetic observations and compare three classifiers.

## 6. DevOps
GitHub Actions checks formatting, linting and tests. On main, a Docker workflow builds API and frontend images and publishes them to GHCR with the built-in token. A downstream workflow starts Compose and checks service health and a sample API operation. Render deployment is optional.

## 7. Testing
Pytest covers z-score math, classification boundaries, risk scoring, explanation factors, login, health, child/visit workflows, dashboard and CSV response. Coverage is configured to fail below 70%; local and CI runs provide the actual measured result.

## 8. Results
The system is designed to produce a reproducible synthetic ML comparison and an evaluation report. Results must be interpreted only as performance on generated data. Synthetic performance is not evidence of clinical accuracy.

## 9. Limitations
Growth calculations are compact educational approximations rather than official WHO LMS tables. The demo login is not production authentication. Synthetic data may encode artificial patterns. The trend score is heuristic, recommendations are generic, and no clinical validation or patient-data security review has been performed.

## 10. Future work
Integrate official licensed WHO reference data; validate with ethically approved and de-identified datasets; add multilingual/mobile usability; add role-based access, audit logging, encryption and consent workflows; validate with qualified clinicians; monitor model drift and fairness.

## 11. Conclusion
NutriTrack demonstrates a complete educational full-stack and DevOps workflow for growth-monitoring data. It should remain a screening-aid prototype and must never replace qualified assessment.
