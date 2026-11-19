from app.services.risk import early_risk_score, explain_factors

def test_empty_history(): assert early_risk_score([]) == 0
def test_score_bounded():
    history = [{"age_months": 12, "whz": -2, "muac_cm": 11, "weight_kg": 6, "recent_illness": 1}]
    assert 0 <= early_risk_score(history) <= 1
def test_declining_trend_increases_risk():
    history = [{"age_months": 12, "whz": 0, "muac_cm": 13, "weight_kg": 8},
               {"age_months": 18, "whz": -1, "muac_cm": 12.8, "weight_kg": 7.8}]
    assert early_risk_score(history) > .15
def test_explain_factors():
    factors = explain_factors({"whz": -2, "muac_cm": 11.8, "recent_illness": 1, "dietary_diversity": 2})
    assert len(factors) >= 3
