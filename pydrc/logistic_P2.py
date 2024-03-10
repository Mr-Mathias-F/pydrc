import math
import numpy as np
from scipy.optimize import curve_fit

class LogisticP2:
    def __init__(self):
        self.params = None

    def logistic_P2(self, x, b, e):
        """Calculate log-logistic curve"""
        f = 1 / (1 + np.exp(b * (np.log(x) - np.log(e))))
        return f

    def fit(self, x_data, y_data):
        """Estimate parameters (b, e)"""
        params, _ = curve_fit(self.logistic_P2, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict output of log-logistic curve (2-parameter model)"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, e = self.params
        return self.logistic_P2(x, b, e)
