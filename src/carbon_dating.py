import math


T_HALF = 5730
DECAY_CONSTANT = -0.693


def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14
    in the sample conpared to the amount in living
    tissue (unitless).
    """
    if carbon_14_ratio <= 0:
        raise ValueError("carbon_14_ratio must be positive")
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
