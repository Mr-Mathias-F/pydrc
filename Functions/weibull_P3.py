from scipy.optimize import curve_fit
import numpy as np

class WeibullP3Model:
    def __init__(self):
        """Initialize a WeibullP3Model instance with parameters set to None"""
        self.params = None

    def weibull_P3(self, x, b, d, e):
        """Calculate the three-parameter Weibull function at a given point"""
        f = (d - 0) * np.exp(-np.exp(b * (np.log(x) - e)))
        return f

    def fit(self, x_data, y_data):
        """Estimate the parameters (b, d, e) of the three-parameter Weibull function from data"""
        params, _ = curve_fit(self.weibull_P3, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the output of the three-parameter Weibull function for a given input using estimated parameters"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, d, e = self.params
        return self.weibull_P3(x, b, d, e)
