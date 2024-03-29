import math
import numpy as np
from scipy.optimize import curve_fit

class LogisticP3:
    def __init__(self):
        self.params = None

    def logistic_P3(self, x, b, c, e):
        """Calculate log-logistic curve"""
        f = c + (1 - c) / (1 + np.exp(b * (np.log(x) - e)))
        return f

    def fit(self, x_data, y_data):
        """Estimate parameters (b, c, e)"""
        params, _ = curve_fit(self.logistic_P3, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict output of the log-logistic curve (3-parameter model)"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, c, e = self.params
        return self.logistic_P3(x, b, c, e)
