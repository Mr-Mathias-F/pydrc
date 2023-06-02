import math

def LL_two(x, b, e):
    """Calculates the log-logistic curve (2-parameter model)"""
    f = 1/(1 + math.exp(b*(math.log(x) - math.log(e))))
    return f
