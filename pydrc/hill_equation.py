import warnings
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import pandas as pd

class HillEquationModel:
    def __init__(self, data=None, x=None, y=None, param_constraint=None):
        self.params = None
        self.data = data
        self.x = x
        self.y = y
        self.param_constraint = np.array(param_constraint)

    def hill_eq(self, x, k_a, l, n):
        """Calculate Hill equation"""
        t = 1 / (1 + (k_a / l) ** n)
        return t

    def fit(self, x=None, y=None, param_constraint=None, n_dec=6):
        """Estimate parameters (k_a, l, n) of the Hill equation from data"""

        ### Model data input
        if self.x is None and x is None:
            raise ValueError("Please provide a valid numeric array for the X-axis")
        if self.y is None and y is None:
            raise ValueError("Please provide a valid numeric array for the Y-axis")
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

        ### Model boundary constraints

        # For fixed boundary value constraints
        if len(np.shape(self.param_constraint)) == 1:
            lower_bound = np.where(self.param_constraint == np.inf, -np.inf, self.param_constraint - 1e-14)
            upper_bound = np.where(self.param_constraint == np.inf, np.inf, self.param_constraint + 1e-14)
            mod_bounds = (np.array(lower_bound), np.array(upper_bound))

        # Interval boundary value constraints
        elif len(np.shape(self.param_constraint)) == 2:
            lower_bound = np.where(self.param_constraint[0] == np.inf, -np.inf, self.param_constraint[0] - 1e-14)
            upper_bound = np.where(self.param_constraint[1] == np.inf, np.inf, self.param_constraint[1] + 1e-14)
            mod_bounds = (np.array(lower_bound), np.array(upper_bound))

        # No constraints
        else:
            mod_bounds = (-np.inf, np.inf)

        ### Model fitting

        warnings.filterwarnings("ignore", category=RuntimeWarning)
        params, covariance = curve_fit(self.hill_eq, x_data, y_data, bounds=mod_bounds)
        warnings.filterwarnings("default", category=RuntimeWarning)

        ### Parameter extraction, standard error estimates and residual standard error of the model

        # Model parameters
        self.params = params

        # Standard error of estimates
        self.std_error = np.sqrt(np.diag(covariance))

        # Residual standard error of model
        self.residuals = self.data[self.y] - self.predict()
        self.n_y_data = len(self.data[self.y])
        self.n_params = len(self.params)
        self.RSE = np.sqrt(np.sum(self.residuals**2) / (self.n_y_data - self.n_params))

        ### Model summary table

        summary_params = pd.DataFrame({'Parameter': ['k_a', 'l', 'n'],
                                       'Estimate': np.round(self.params, decimals=n_dec),
                                       'Std. Error': np.round(self.std_error, decimals=n_dec),
                                       't-value': np.round(self.params / self.std_error, decimals=n_dec),
                                       'p-value': np.round((1 - stats.t(df=len(y_data) - len(self.params)).cdf(x=self.params / self.std_error)) * 2, decimals=n_dec)
                                       })
        print(summary_params)
        print()
        print('Residual Standard Error (RSE):', np.round(self.RSE, decimals=n_dec), '   Degrees of Freedom:', len(y_data) - len(self.params))

    def predict(self, x=None):
        """Predict output of the Hill equation"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first")
        if x is None:
            x_pred = self.data[self.x]
        else:
            x_pred = x
        k_a, l, n = self.params
        return self.hill_eq(x_pred, k_a, l, n)
