import math
import numpy as np
from scipy.optimize import curve_fit

class ExponentialDecay:
    def __init__(self):
        self.params = None

    def exponential_decay(self, x, c, d, e):
        """Calculate exponential decay model"""
        f = c + (d - c) * np.exp(-x / e)
        return f

    def fit(self, x_data, y_data):
        """Estimate parameters (c, d, e)"""
        params, _ = curve_fit(self.exponential_decay, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict output of the exponential decay model"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        c, d, e = self.params
        return self.exponential_decay(x, c, d, e)
