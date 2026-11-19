# Compact educational LMS approximation, not the full WHO reference tables.
# Values are illustrative anchors; interpolate by age and sex for screening demos.
ANCHORS = {
    "M": {"w": (3.3, 9.0), "h": (49.9, 74.0), "muac": (10.5, 13.5)},
    "F": {"w": (3.2, 8.4), "h": (49.1, 72.5), "muac": (10.4, 13.2)},
}


def _expected(age_months: int, sex: str, metric: str) -> float:
    sex = sex.upper()
    if sex not in ANCHORS:
        raise ValueError("sex must be M or F")
    start, end = ANCHORS[sex][metric]
    fraction = min(max(age_months, 0), 60) / 60
    return start + fraction * (end - start)


def z_score(value: float, median: float, sd: float) -> float:
    if sd <= 0:
        raise ValueError("sd must be positive")
    return (value - median) / sd


def calculate_z_scores(age_months: int, sex: str, weight_kg: float, height_cm: float):
    # Simplified age/sex reference approximations; WHZ uses height-based expected weight.
    expected_w = _expected(age_months, sex, "w")
    expected_h = _expected(age_months, sex, "h")
    waz = z_score(weight_kg, expected_w, max(0.65, expected_w * 0.12))
    haz = z_score(height_cm, expected_h, max(2.2, expected_h * 0.035))
    expected_weight_for_height = max(2.5, 0.105 * height_cm - 1.8)
    whz = z_score(
        weight_kg,
        expected_weight_for_height,
        max(0.45, expected_weight_for_height * 0.12),
    )
    return {"waz": round(waz, 2), "haz": round(haz, 2), "whz": round(whz, 2)}
