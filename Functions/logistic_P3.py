import math
import numpy as np
from scipy.optimize import curve_fit

class LogisticP3:
    def __init__(self):
        """Initialize a LogisticP3Model instance with parameters set to None"""
        self.params = None

    def logistic_P3(self, x, b, c, e):
        """Calculate the log-logistic curve (3-parameter model) at a given point"""
        f = c + (1 - c) / (1 + np.exp(b * (np.log(x) - e)))
        return f

    def fit(self, x_data, y_data):
        """Estimate the parameters (b, c, e) of the log-logistic curve (3-parameter model) from data"""
        params, _ = curve_fit(self.logistic_P3, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the log-logistic curve (3-parameter model) for a given input using estimated parameters"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, c, e = self.params
        return self.logistic_P3(x, b, c, e)
