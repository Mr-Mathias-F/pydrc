import math

def exponential_decay(x, c, d, e):
    """Calculate value of exponential decay model"""
    f = c + (d - c) * (math.exp(-x / e))
    return f
