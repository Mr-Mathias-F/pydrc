import math

def logistic_P4(x, b, c, d, e):
    """Calculates the log-logistic curve (4-parameter model)"""
    f = c + (d - c)/(1 + math.exp(b*(math.log(x) - math.log(e))))
    return f
