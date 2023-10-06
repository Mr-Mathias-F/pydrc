import math
import numpy as np
from scipy.optimize import curve_fit

class ARModel:
    def __init__(self):
        self.params = None

    def ar_model(self, x, c, d, e):
        """Calculate asymptotic regression model"""
        f = c + (d - c) * (1 - np.exp(-x / e))
        return f

    def fit(self, x_data, y_data):
        """Estimate the parameters (c, d, e)"""
        params, _ = curve_fit(self.ar_model, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict output of the asymptotic regression model"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        c, d, e = self.params
        return self.ar_model(x, c, d, e)
