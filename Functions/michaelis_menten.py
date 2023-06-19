def michaelis_menten(v_max, k_m, s):
    """
    Calculates the rate of an enzymatic reaction using the Michaelis-Menten equation
    """
    v_0 = (v_max * s) / (k_m + s)
    return v_0
