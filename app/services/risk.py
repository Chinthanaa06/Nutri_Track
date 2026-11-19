def early_risk_score(history):
    # Transparent trend heuristic: only history is used; output is a screening signal.
    if not history:
        return 0.0
    ordered = sorted(history, key=lambda row: row["age_months"])
    latest = ordered[-1]
    score = 0.15
    if latest.get("whz", 0) < -1:
        score += 0.25
    if latest.get("muac_cm", 13) < 12.5:
        score += 0.25
    if latest.get("recent_illness", 0):
        score += 0.10
    if len(ordered) >= 2:
        previous = ordered[-2]
        if latest.get("whz", 0) < previous.get("whz", 0):
            score += 0.15
        if latest.get("weight_kg", 0) <= previous.get("weight_kg", 0):
            score += 0.10
    return round(min(score, 1.0), 2)

def explain_factors(visit):
    factors = []
    if visit["whz"] < -1: factors.append("Low weight relative to height")
    if visit["muac_cm"] < 12.5: factors.append("Low mid-upper arm circumference")
    if visit.get("recent_illness"): factors.append("Recent illness reported")
    if visit.get("dietary_diversity", 0) < 4: factors.append("Low dietary diversity")
    return factors[:4] or ["No major screening flag in the recorded indicators"]
