from pathlib import Path

import joblib
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from ml.data_gen import generate_dataset

FEATURES = [
    "age_months",
    "sex",
    "weight_kg",
    "height_cm",
    "muac_cm",
    "recent_illness",
    "dietary_diversity",
]


def train():
    data = generate_dataset()
    x, y = data[FEATURES], data["status"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=42, stratify=y
    )
    candidates = {
        "LogisticRegression": make_pipeline(
            StandardScaler(), LogisticRegression(max_iter=1000)
        ),
        "RandomForest": RandomForestClassifier(
            n_estimators=120, random_state=42, class_weight="balanced"
        ),
        "GradientBoosting": GradientBoostingClassifier(random_state=42),
    }
    scores = {}
    best_name, best_model, best_score = None, None, -1
    for name, model in candidates.items():
        model.fit(x_train, y_train)
        score = f1_score(y_test, model.predict(x_test), average="weighted")
        scores[name] = score
        if score > best_score:
            best_name, best_model, best_score = name, model, score
    output = Path(__file__).parent / "models"
    output.mkdir(exist_ok=True)
    joblib.dump(
        {"model": best_model, "features": FEATURES, "name": best_name},
        output / "nutritrack_model.joblib",
    )
    return scores, best_name


if __name__ == "__main__":
    scores, best = train()
    print("Weighted F1:", scores, "Best:", best)
