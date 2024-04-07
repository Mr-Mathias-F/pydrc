import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

class LogisticP3Model:
    def __init__(self, data=None, x=None, y=None):
        self.params = None
        self.data = data
        self.x = x
        self.y = y

    def logistic_P3(self, x, b, c, e):
        """Calculate log-logistic curve (3-parameter model) at a given point"""
        f = c + (1 - c) / (1 + np.exp(b * (np.log(x) - e)))
        return f

    def fit(self, x=None, y=None, n_dec=6):
        """Estimate parameters (b, c, e) of the log-logistic curve from data"""
        if self.x is None:
            x_data = self.data[x]
            self.x = x
        else:
            x_data = self.data[self.x]
        
        if self.y is None:
            y_data = self.data[y]
            self.y = y
        else:
            y_data = self.data[self.y]

        params, covariance = curve_fit(self.logistic_P3, x_data, y_data)
        self.params = params

        # Standard error of estimates
        self.std_error = np.sqrt(np.diag(covariance))

        # Model summary table
        summary_params = pd.DataFrame({'Parameter': ['b', 'c', 'e'],
                                       'Estimate': np.round(self.params, decimals=n_dec),
                                       'Std. Error': np.round(self.std_error, decimals=n_dec)})
        print(summary_params)

    def predict(self, x):
        """Predict output of log-logistic curve"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        b, c, e = self.params
        return self.logistic_P3(x, b, c, e)
