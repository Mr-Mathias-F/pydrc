import math

def nec_model(x, c, b, d, e, b_2, d_2, e_2, I):
    """Calculates no effect concentration model"""
    f = c + (d - c) * math.exp(-b(x - e) * I * (x - e)) + ((d_2) / (1 + math.exp((b_2) * (math.log(x))) - math.log(e_2)))
    return f
