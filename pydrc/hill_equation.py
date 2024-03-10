import numpy as np

class HillEquation:
    def __init__(self):
        self.params = None

    def hill_eq(self, x, k_a, l, n):
        """Calculate Hill equation"""
        t = 1 / (1 + (k_a / l)**n)
        return t

    def fit(self, x_data, y_data):
        """Estimate parameters (k_a, l, n)"""
        from scipy.optimize import curve_fit
        params, _ = curve_fit(self.hill_eq, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict output of the Hill equation"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        k_a, l, n = self.params
        return self.hill_eq(x, k_a, l, n)
