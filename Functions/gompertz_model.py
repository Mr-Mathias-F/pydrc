import math

def gompertz_model(x, c, d, e):
    """Calculate value of Gompertz model"""
    f = c + (d - c) * (math.exp(-math.exp(b * (x - e))))
    return f
