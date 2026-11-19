# Run NutriTrack

## Local setup (Python 3.11)
1. Create and activate a virtual environment.
2. Install: `pip install -r requirements-dev.txt`
3. Start API: `uvicorn app.main:app --reload`
4. In another terminal: `streamlit run frontend/streamlit_app.py`
5. Open `http://localhost:8501`. Demo login: `demo` / `nutri-demo`.

## Docker
`docker compose up --build` then open `http://localhost:8501`; API docs at `http://localhost:8000/docs`.
