import warnings
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as plt

class DoseResponse:
    def __init__(self, data=None, param_constraint=None):
        self.data = data
        self.x = data.columns[0]
        self.y = data.columns[1]
        self.param_constraint = np.array(param_constraint)
        self.params = None

    def model_function(self, x, *params):
        """Override this method in subclasses with the specific model function"""
        raise NotImplementedError("Subclasses should implement this method")

    def fit(self, x=None, y=None, param_constraint=None, n_dec=6):
        """Estimate parameters of the model from data"""
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if self.data is None:
            raise ValueError("Data must be provided")

        x = self.data[self.x]
        y = self.data[self.y]

        # Model boundary constraints
        if param_constraint is not None:
            self.param_constraint = np.array(param_constraint)

        if len(np.shape(self.param_constraint)) == 1:
            lower_bound = np.where(self.param_constraint == np.inf, -np.inf, self.param_constraint - 1e-14)
            upper_bound = np.where(self.param_constraint == np.inf, np.inf, self.param_constraint + 1e-14)
            mod_bounds = (np.array(lower_bound), np.array(upper_bound))
        elif len(np.shape(self.param_constraint)) == 2:
            lower_bound = np.where(self.param_constraint[0] == np.inf, -np.inf, self.param_constraint[0] - 1e-14)
            upper_bound = np.where(self.param_constraint[1] == np.inf, np.inf, self.param_constraint[1] + 1e-14)
            mod_bounds = (np.array(lower_bound), np.array(upper_bound))
        else:
            mod_bounds = (-np.inf, np.inf)

        # Model fitting
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        params, covariance = curve_fit(self.model_function, x, y, bounds=mod_bounds)
        warnings.filterwarnings("default", category=RuntimeWarning)

        # Parameter extraction, standard error estimates and residual standard error of the model
        self.params = params
        std_error = np.sqrt(np.diag(covariance))
        residuals = self.data[self.y] - self.predict()
        n_y = len(self.data[self.y])
        n_params = len(self.params)
        rse = np.sqrt(np.sum(residuals**2) / (n_y - n_params))

        # Model summary table
        summary_params = pd.DataFrame({
            'Parameter': [f'param_{i}' for i in range(len(self.params))],
            'Estimate': np.round(self.params, n_dec),
            'Std. Error': np.round(std_error, n_dec),
            't-value': np.round(self.params / std_error, n_dec),
            'p-value': np.round((1 - stats.t(df=len(y) - len(self.params)).cdf(x=self.params / std_error)) * 2, n_dec)
        })
        print(summary_params)
        print()
        print('Residual Standard Error (RSE):', np.round(rse, n_dec), '   Degrees of Freedom:', len(y) - len(self.params))

    def predict(self, x=None):
        """Predict the output of the model"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first")
        if x is None:
            x_pred = self.data[self.x]
        else:
            x_pred = x
        return self.model_function(x_pred, *self.params)

    def plot(self):
        """Plot data and fitted model"""
        x = self.data[self.x]
        response = self.data[self.y]
        predictions = self.predict(x)
        plt.plot(predictions, label="prediction")
        plt.plot(response, ".", label="response")
        plt.legend()
        plt.show()
