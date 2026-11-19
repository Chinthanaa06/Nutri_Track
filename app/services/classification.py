def classify_status(waz: float, haz: float, whz: float, muac_cm: float) -> str:
    # Priority follows acute severity first, then chronic/underweight indicators.
    if whz < -3 or muac_cm < 11.5:
        return "Severe Acute Malnutrition"
    if whz < -2 or muac_cm < 12.5:
        return "Moderate Acute Malnutrition"
    if haz < -2:
        return "Stunted"
    if waz < -2:
        return "Underweight"
    return "Normal"

def recommendations(status: str):
    advice = {
        "Normal": ["Continue age-appropriate diverse meals", "Attend routine growth monitoring"],
        "Underweight": ["Arrange a follow-up growth check", "Discuss energy- and protein-rich local foods"],
        "Stunted": ["Review long-term diet and illness history", "Refer for a qualified growth assessment"],
        "Moderate Acute Malnutrition": ["Arrange prompt assessment by a qualified health worker", "Follow local nutrition programme guidance"],
        "Severe Acute Malnutrition": ["Urgent referral to an appropriate health facility", "Do not delay professional assessment"],
    }
    return advice.get(status, ["Seek qualified health-worker assessment"])
