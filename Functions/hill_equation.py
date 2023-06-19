def hill_eq(k_a, l, n):
    """Calculate the Hill equation output value"""
    t = 1 / (1 + (k_a / l)**n)
    return t
