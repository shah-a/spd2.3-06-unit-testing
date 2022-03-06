import pytest
import math
from src.carbon_dating import get_age_carbon_14_dating


def test_get_age_carbon_14_dating():
    result = round(get_age_carbon_14_dating(0.35), 2)
    assert math.isclose(result, 8680.35)


def test_get_age_carbon_14_dating_zero():
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(0)


def test_get_age_carbon_14_dating_negative():
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(-1)
