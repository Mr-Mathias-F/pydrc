import math
import numpy as np
from scipy.optimize import curve_fit

class GompertzModel:
    def __init__(self):
        """Initialize a GompertzModel instance with parameters set to None"""
        self.params = None

    def gompertz_model(self, x, b, c, d, e):
        """Calculate the Gompertz model at a given point"""
        f = c + (d - c) * np.exp(-np.exp(b * (x - e)))
        return f

    def fit(self, x_data, y_data):
        """Estimate the parameters (b, c, d, e) of the Gompertz model from data"""
        params, _ = curve_fit(self.gompertz_model, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the Gompertz model for a given input using estimated parameters"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, c, d, e = self.params
        return self.gompertz_model(x, b, c, d, e)
