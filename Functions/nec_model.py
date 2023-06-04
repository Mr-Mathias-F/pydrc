import math

def nec_model(x, c, b, d, e):
    """Calculates no effect concentration model"""
    f = c + (d - c) * math.exp(-b(x - e) * I * (x - e)) + ((d * 2) / (1 + math.exp((b*2) * (math.log(x))) - math.log(e*2)))
    return f
