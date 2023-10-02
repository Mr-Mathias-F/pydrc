import math
import numpy as np
from scipy.optimize import curve_fit

class ARModel:
    def __init__(self):
        """Initialize an ARModel instance with parameters set to None"""
        self.params = None

    def ar_model(self, x, c, d, e):
        """Calculate the asymptotic regression model at a given point"""
        f = c + (d - c) * (1 - np.exp(-x / e))
        return f

    def fit(self, x_data, y_data):
        """Estimate the parameters (c, d, e) of the asymptotic regression model from data"""
        params, _ = curve_fit(self.ar_model, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the asymptotic regression model for a given input using estimated parameters"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        c, d, e = self.params
        return self.ar_model(x, c, d, e)
