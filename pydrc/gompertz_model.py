import math
import numpy as np
from scipy.optimize import curve_fit

class GompertzModel:
    def __init__(self):
        self.params = None

    def gompertz_model(self, x, b, c, d, e):
        """Calculate Gompertz model"""
        f = c + (d - c) * np.exp(-np.exp(b * (x - e)))
        return f

    def fit(self, x_data, y_data):
        """Estimate parameters (b, c, d, e)"""
        params, _ = curve_fit(self.gompertz_model, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict output of the Gompertz model"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, c, d, e = self.params
        return self.gompertz_model(x, b, c, d, e)
