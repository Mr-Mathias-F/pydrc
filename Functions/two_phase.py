import math
import numpy as np
from scipy.optimize import curve_fit

class TwoPhaseModel:
    def __init__(self):
        """Initialize a TwoPhaseModel instance with parameters set to None"""
        self.params = None

    def two_phase(self, x, c, b_1, b_2, d_1, d_2, e_1, e_2):
        """Calculate the two-phase function at a given point"""
        f = c + ((d_1 - c) / (1 + np.exp(b_1 * (np.log(x) - np.log(e_1))))) + (d_2 / (1 + np.exp(b_2 * (np.log(x) - np.log(e_2)))))
        return f

    def fit(self, x_data, y_data):
        """Estimate the parameters (c, b_1, b_2, d_1, d_2, e_1, e_2) of the two-phase function from data"""
        params, _ = curve_fit(self.two_phase, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the two-phase function for a given input using estimated parameters"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        c, b_1, b_2, d_1, d_2, e_1, e_2 = self.params
        return self.two_phase(x, c, b_1, b_2, d_1, d_2, e_1, e_2)
