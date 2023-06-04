import math

def ar_model(x, c, d, e):
    """Calculate value of asymptotic regression model"""
    f = c + (d - c) * (1 - math.exp(-x / e))
    return f
