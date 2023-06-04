import math

def two_phase(x, c, b_1, b_2, d_1, d_2, e_1, e_2):
    """Calculates two-phase function value"""
    f = c + ((d_1 - c) / (1 + math.exp(b_1 * (math.log(x) - math.log(e_1))))) + (d_2 / 1 + math.exp(b_2 * (math.log(x) - math.log(e_2))))
    return f
