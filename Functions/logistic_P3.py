import math

def logistic_P3(x, b, e):
    """Calculates the log-logistic curve (2-parameter model)"""
    f = c + (1 - c)/(1 + math.exp(b*(math.log(x) - e)))
    return f
