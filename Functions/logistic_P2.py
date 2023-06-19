import math

def logistic_P2(x, b, e):
    """Calculates the log-logistic curve (2-parameter model)"""
    f = 1/(1 + math.exp(b*(math.log(x) - math.log(e))))
    return f
