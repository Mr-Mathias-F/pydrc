import math
import numpy as np
from scipy.optimize import curve_fit

class NecModel:
    def __init__(self):
        self.params = None

    def nec_model(self, x, c, b, d, e, b_2, d_2, e_2, I):
        """Calculate the no effect concentration model"""
        f = c + (d - c) * np.exp(-b * (x - e) * I * (x - e)) + ((d_2) / (1 + np.exp(b_2 * (np.log(x)) - np.log(e_2))))
        return f

    def fit(self, x_data, y_data):
        """Estimate parameters (c, b, d, e, b_2, d_2, e_2, I)"""
        params, _ = curve_fit(self.nec_model, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the no effect concentration model"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        c, b, d, e, b_2, d_2, e_2, I = self.params
        return self.nec_model(x, c, b, d, e, b_2, d_2, e_2, I)
