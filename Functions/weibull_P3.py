import math

def weibull_P3(x, b, d, e):
    """Calculate value of three-parameter Weibull function"""
    f = 0 + (d - 0) * math.exp(-math.exp(b * (math.log(x) - e)))
    return f
