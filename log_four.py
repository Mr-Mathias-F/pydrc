import math

def log_four(x, b, c, d, e):
    """Calculates the logarithm to the base of 4 of a given number"""
    f = c + (d - c)/(1 + math.exp(b*(math.log(x) - math.log(e))))
    return f
