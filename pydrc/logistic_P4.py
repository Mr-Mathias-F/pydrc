import warnings
import math
import numpy as np
from scipy import stats # For t-tests
from scipy.optimize import curve_fit # Parameter optimization

class LogisticP4Model:
    def __init__(self, data = None, x = None, y = None, param_constraint = None):
        self.params = None
        self.data = data
        self.x = x
        self.y = y
        self.param_constraint = np.array(param_constraint)

    def logistic_P4(self, x, b, c, d, e):
        """Calculate log-logistic curve (4-parameter model) at a given point"""
        f = c + (d - c) / (1 + np.exp(b * (np.log(x) - np.log(e))))
        return f

    def fit(self, x = None, y = None, summary = True, keep_summary = False, param_constraint = None, n_dec = 6):
        """Estimate parameters (b, c, d, e) of the log-logistic curve from data"""

        ### Model data input ###
        if self.x is None and x is None:
            raise ValueError("Warning: No valid parameter provided for the X-axis. Please ensure that the parameter supplied is a numeric array containing valid numerical values.")
        if self.y is None and y is None:
            raise ValueError("Warning: No valid parameter provided for the Y-axis. Please ensure that the parameter supplied is a numeric array containing valid numerical values.")          
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
            
        ### Model boundary constraints ###

        # For fixed boundary value constraints #
        if len(np.shape(self.param_constraint)) == 1:
            lower_bound = np.where(self.param_constraint == np.inf, -np.inf, self.param_constraint - 1e-14)
            upper_bound = np.where(self.param_constraint == np.inf, np.inf, self.param_constraint + 1e-14)
            mod_bounds = (np.array(lower_bound), np.array(upper_bound))

        # Interval boundary value constraints #
        elif len(np.shape(self.param_constraint)) == 2:
            lower_bound = np.where(self.param_constraint[0] == np.inf, -np.inf, self.param_constraint[0] - 1e-14)
            upper_bound = np.where(self.param_constraint[1] == np.inf, np.inf, self.param_constraint[1] + 1e-14)
            mod_bounds = (np.array(lower_bound), np.array(upper_bound))

        # No constraints #
        else:
            mod_bounds = (-np.inf, np.inf)

        ### Model fitting ###
        
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        params, covariance = curve_fit(self.logistic_P4, x_data, y_data, bounds = mod_bounds)
        warnings.filterwarnings("default", category=RuntimeWarning)

        ### Parameter extraction, standard error estimates and residual standard error of the model ###

        # Model parameters #
        self.params = params

        # Standard eror of estimates #
        self.std_error = np.sqrt(np.diag(covariance))

        # Residual standard error of model #
        self.residuals = self.data[self.y] - self.predict()
        self.n_y_data = len(self.data[self.y]) 
        self.n_params = len(self.params) 
        self.RSE = np.sqrt(np.sum(self.residuals**2) / (self.n_y_data - self.n_params))

        ### Model summary table ###
        
        if summary == True:
            summary_params = pd.DataFrame({'Parameter': ['b', 'c', 'd', 'e'],
                                           'Estimate': np.round(self.params, decimals = n_dec),
                                           'Std. Error': np.round(self.std_error, decimals = n_dec),
                                           't-value': np.round(self.params / self.std_error, decimals = n_dec),
                                           'p-value': np.round((1 - stats.t(df = len(y_data) - len(self.params)).cdf(x = self.params / self.std_error)) * 2, decimals = n_dec)
                                            })
        if keep_summary == True:
            return summary_params
        else:
            print(summary_params)
            print()
            print('Residual Standard Error (RSE):', np.round(self.RSE, decimals = n_dec),'   Degrees of Freedom:', len(y_data) - len(self.params))
          
    def predict(self, x = None):
        """Predict output of log-logistic curve"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        if x is None:
            x_pred = self.data[self.x]
        else:
            x_pred = x
        b, c, d, e = self.params
        return self.logistic_P4(x_pred, b, c, d, e)
