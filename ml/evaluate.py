from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay, f1_score
from sklearn.model_selection import train_test_split
from ml.data_gen import generate_dataset
from ml.train import FEATURES

def evaluate():
    data = generate_dataset()
    x, y = data[FEATURES], data["status"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.25,
        random_state=42, stratify=y)
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=120, random_state=42, class_weight="balanced")
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    report = classification_report(y_test, pred, output_dict=True, zero_division=0)
    out = Path("docs")
    out.mkdir(exist_ok=True)
    labels = sorted(y.unique())
    ConfusionMatrixDisplay(confusion_matrix(y_test, pred, labels=labels), display_labels=labels).plot(
        xticks_rotation=35, colorbar=False)
    plt.tight_layout()
    plt.savefig(out / "confusion_matrix.png")
    metrics = {"accuracy": accuracy_score(y_test, pred), "weighted_f1": f1_score(y_test, pred, average="weighted"),
               "classification_report": report}
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2))
    lines = ["# ML evaluation results", "", f"- Accuracy: {metrics['accuracy']:.3f}",
             f"- Weighted F1: {metrics['weighted_f1']:.3f}", "",
             "| Candidate | Comparison metric |", "|---|---:|",
             "| Logistic Regression | Run `python -m ml.train` for current comparison |",
             "| Random Forest | Evaluation script baseline |",
             "| Gradient Boosting | Run `python -m ml.train` for current comparison |",
             "", "Synthetic data only; not clinical validation."]
    (out / "ml_report.md").write_text("\n".join(lines))
    return metrics

if __name__ == "__main__":
    print(evaluate())
