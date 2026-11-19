# Presentation outline (14 slides)

1. **Title — NutriTrack**: Project name, student, course. *Say:* “This is a child growth screening prototype with longitudinal risk flags.”
2. **Problem**: Repeated growth records are hard to review manually. *Say:* “The project organizes records and highlights follow-up signals.”
3. **Objectives**: Capture, calculate, classify, explain, visualize. *Say:* “These are the five core goals.”
4. **Users**: Anganwadi/ASHA worker, school nurse, supervisor. *Say:* “The interface is designed around simple workflows.”
5. **Proposed solution**: Streamlit + FastAPI + database. *Say:* “The UI calls a separate backend.”
6. **Architecture**: Show architecture diagram. *Say:* “Each service has a clear responsibility.”
7. **Growth indicators**: WAZ/HAZ/WHZ-style scores and MUAC. *Say:* “This implementation is simplified and not the official WHO reference.”
8. **Classification**: Rule thresholds and status labels. *Say:* “Rules are transparent and prioritized by acute risk.”
9. **Early-risk score**: Visit history and trend signals. *Say:* “The score helps flag a normal record trending downward.”
10. **ML workflow**: Synthetic data, three classifiers, model comparison. *Say:* “This is a reproducible ML exercise, not clinical validation.”
11. **Explainability and recommendations**: Indicator flags and safe referrals. *Say:* “We show the factors that triggered a flag.”
12. **Dashboard and UX**: Distribution, high-risk list, CSV. *Say:* “Labels accompany color so meaning is not color-only.”
13. **DevOps and testing**: CI, Docker, GHCR, CD verification. *Say:* “The pipeline uses the built-in token and no external secrets.”
14. **Limitations and conclusion**: Synthetic data, simplified references, future work. *Say:* “This is a screening aid only, not a diagnosis.”

## Closing
Thank the audience and invite questions. Never present the prototype as a validated medical tool.
