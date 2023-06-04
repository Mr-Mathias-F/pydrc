import math

def three_p_weibull(x, b, d, e):
    """Calculate value of three-parameter Weibull function"""
    f = 0 + (d - 0) * math.exp(-math.exp(b * (log(x) - e)))
    return f
