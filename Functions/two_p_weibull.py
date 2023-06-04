import math

def two_p_weibull(x, b, e):
    """Calculates value of two-parameter Weibull function"""
    f = math.exp(- math.exp(b * (math.log(x) - e)))
    return f
