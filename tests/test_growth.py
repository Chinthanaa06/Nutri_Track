import pytest

from app.services.growth import calculate_z_scores, z_score


def test_z_score_zero():
    assert z_score(10, 10, 2) == 0


def test_z_score_positive():
    assert z_score(12, 10, 2) == 1


def test_z_score_negative():
    assert z_score(8, 10, 2) == -1


def test_invalid_sd():
    with pytest.raises(ValueError):
        z_score(1, 1, 0)


def test_growth_returns_three_scores():
    result = calculate_z_scores(24, "F", 10, 80)
    assert set(result) == {"waz", "haz", "whz"}


def test_invalid_sex():
    with pytest.raises(ValueError):
        calculate_z_scores(12, "X", 8, 70)
