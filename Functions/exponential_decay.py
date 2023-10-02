import math
import numpy as np
from scipy.optimize import curve_fit

class ExponentialDecay:
    def __init__(self):
        """Initialize an ExponentialDecayModel instance with parameters set to None"""
        self.params = None

    def exponential_decay(self, x, c, d, e):
        """Calculate the exponential decay model at a given point"""
        f = c + (d - c) * np.exp(-x / e)
        return f

    def fit(self, x_data, y_data):
        """Estimate the parameters (c, d, e) of the exponential decay model from data"""
        params, _ = curve_fit(self.exponential_decay, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the exponential decay model for a given input using estimated parameters"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        c, d, e = self.params
        return self.exponential_decay(x, c, d, e)
