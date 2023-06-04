import math

def four_p_weibull(x, b, c, d, e):
    """Calculate value of four-parameter Weibull function"""
    f = c + (d - c) * math.exp(-math.exp(b * (math.log(x) - math.log(e))))
    return f
