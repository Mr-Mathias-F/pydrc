from scipy.optimize import curve_fit
import numpy as np

class WeibullP4:
    def __init__(self):
        self.params = None

    def weibull_P4(self, x, b, c, d, e):
        """Calculate four-parameter Weibull function"""
        f = c + (d - c) * np.exp(-np.exp(b * (np.log(x) - np.log(e))))
        return f

    def fit(self, x_data, y_data):
        """Estimate the parameters (b, c, d, e)"""
        params, _ = curve_fit(self.weibull_P4, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the four-parameter Weibull function"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, c, d, e = self.params
        return self.weibull_P4(x, b, c, d, e)
