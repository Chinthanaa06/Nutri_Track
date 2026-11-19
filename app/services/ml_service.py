from pathlib import Path

import joblib

MODEL_PATH = (
    Path(__file__).resolve().parents[2] / "ml" / "models" / "nutritrack_model.joblib"
)


def predict_ml(features):
    if not MODEL_PATH.exists():
        return {"prediction": "Normal", "probability": 0.5, "model": "rules-fallback"}
    model = joblib.load(MODEL_PATH)
    labels = model.predict([features])
    probabilities = model.predict_proba([features])[0]
    return {
        "prediction": str(labels[0]),
        "probability": float(max(probabilities)),
        "model": "RandomForest",
    }
