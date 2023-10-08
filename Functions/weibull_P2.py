from scipy.optimize import curve_fit
import numpy as np

class WeibullP2:
    def __init__(self):
        self.params = None

    def weibull_P2(self, x, b, e):
        """Calculate two-parameter Weibull function"""
        f = np.exp(-np.exp(b * (np.log(x) - e)))
        return f

    def fit(self, x_data, y_data):
        """Estimate parameters (b, e)"""
        params, _ = curve_fit(self.weibull_P2, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the two-parameter Weibull function"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, e = self.params
        return self.weibull_P2(x, b, e)
