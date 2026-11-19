from app.services.classification import classify_status, recommendations


def test_normal():
    assert classify_status(0, 0, 0, 13) == "Normal"


def test_underweight():
    assert classify_status(-2.5, 0, 0, 13) == "Underweight"


def test_stunted():
    assert classify_status(0, -2.5, 0, 13) == "Stunted"


def test_mam():
    assert classify_status(0, 0, -2.5, 13) == "Moderate Acute Malnutrition"


def test_sam():
    assert classify_status(0, 0, -3.2, 13) == "Severe Acute Malnutrition"


def test_recommendations_exist():
    assert recommendations("Normal")
