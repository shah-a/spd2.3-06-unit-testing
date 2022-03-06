import math
from src.calculate_grades import calculate_stat


def test_calculate_stat():
    mean, sd = calculate_stat([90, 95, 100, 95, 90])
    assert math.isclose(mean, 94.0)
    assert math.isclose(sd, 3.7416573867739413)
