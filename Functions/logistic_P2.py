import math
import numpy as np
from scipy.optimize import curve_fit

class LogisticP2:
    def __init__(self):
        """Initialize a LogisticP2Model instance with parameters set to None"""
        self.params = None

    def logistic_P2(self, x, b, e):
        """Calculate the log-logistic curve (2-parameter model) at a given point"""
        f = 1 / (1 + np.exp(b * (np.log(x) - np.log(e))))
        return f

    def fit(self, x_data, y_data):
        """Estimate the parameters (b, e) of the log-logistic curve (2-parameter model) from data"""
        params, _ = curve_fit(self.logistic_P2, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the log-logistic curve (2-parameter model) for a given input using estimated parameters"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, e = self.params
        return self.logistic_P2(x, b, e)
