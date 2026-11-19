from pathlib import Path

import numpy as np
import pandas as pd


def generate_dataset(rows=1200, seed=42):
    rng = np.random.default_rng(seed)
    age = rng.integers(0, 61, rows)
    sex = rng.integers(0, 2, rows)
    expected = 3.2 + age * (0.095 if sex.mean() > 0.5 else 0.097)
    weight = np.maximum(2.0, expected + rng.normal(0, 1.1, rows))
    height = 49 + age * 0.42 + rng.normal(0, 3.0, rows)
    muac = 10.5 + age * 0.05 + rng.normal(0, 0.9, rows)
    illness = rng.integers(0, 2, rows)
    diversity = rng.integers(0, 11, rows)
    whz_proxy = (weight - (0.105 * height - 1.8)) / 0.8
    labels = np.where(
        (whz_proxy < -2.7) | (muac < 11.5),
        "Severe Acute Malnutrition",
        np.where(
            (whz_proxy < -1.8) | (muac < 12.5),
            "Moderate Acute Malnutrition",
            np.where(weight < expected - 1.3, "Underweight", "Normal"),
        ),
    )
    return pd.DataFrame(
        {
            "age_months": age,
            "sex": sex,
            "weight_kg": weight,
            "height_cm": height,
            "muac_cm": muac,
            "recent_illness": illness,
            "dietary_diversity": diversity,
            "status": labels,
        }
    )


if __name__ == "__main__":
    path = Path(__file__).parent / "synthetic_children.csv"
    generate_dataset().to_csv(path, index=False)
    print(f"Wrote {path}")
