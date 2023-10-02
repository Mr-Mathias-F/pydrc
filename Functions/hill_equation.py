import numpy as np

class HillEquation:
    def __init__(self):
        """Initialize a HillEquationModel instance with parameters set to None"""
        self.params = None

    def hill_eq(self, x, k_a, l, n):
        """Calculate the Hill equation at a given point"""
        t = 1 / (1 + (k_a / l)**n)
        return t

    def fit(self, x_data, y_data):
        """Estimate the parameters (k_a, l, n) of the Hill equation from data"""
        from scipy.optimize import curve_fit
        params, _ = curve_fit(self.hill_eq, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the Hill equation for a given input using estimated parameters"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        k_a, l, n = self.params
        return self.hill_eq(x, k_a, l, n)
