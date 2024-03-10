import math
import numpy as np
from scipy.optimize import curve_fit

class LogisticP4Model:
    def __init__(self):
        self.params = None

    def logistic_P4(self, x, b, c, d, e):
        """Calculate log-logistic curve (4-parameter model) at a given point"""
        f = c + (d - c) / (1 + np.exp(b * (np.log(x) - np.log(e))))
        return f

    def fit(self, x_data, y_data):
        """Estimate parameters (b, c, d, e) of the log-logistic curve from data"""
        params, _ = curve_fit(self.logistic_P4, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict output of log-logistic curve"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, c, d, e = self.params
        return self.logistic_P4(x, b, c, d, e)
