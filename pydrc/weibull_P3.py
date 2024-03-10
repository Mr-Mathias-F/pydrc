from scipy.optimize import curve_fit
import numpy as np

class WeibullP3Model:
    def __init__(self):
        self.params = None

    def weibull_P3(self, x, b, d, e):
        """Calculate three-parameter Weibull function"""
        f = (d - 0) * np.exp(-np.exp(b * (np.log(x) - e)))
        return f

    def fit(self, x_data, y_data):
        """Estimate parameters (b, d, e)"""
        params, _ = curve_fit(self.weibull_P3, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the three-parameter Weibull function"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, d, e = self.params
        return self.weibull_P3(x, b, d, e)
