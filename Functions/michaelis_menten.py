from scipy.optimize import curve_fit

class MichaelisMenten:
    def __init__(self):
        """Initialize a MichaelisMentenModel instance with parameters set to None"""
        self.params = None

    def michaelis_menten(self, x, v_max, k_m):
        """Calculate the Michaelis-Menten rate at a given point"""
        v_0 = (v_max * x) / (k_m + x)
        return v_0

    def fit(self, x_data, y_data):
        """Estimate the parameters (v_max, k_m) of the Michaelis-Menten equation from data"""
        params, _ = curve_fit(self.michaelis_menten, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the rate of the Michaelis-Menten equation for a given input using estimated parameters"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        v_max, k_m = self.params
        return self.michaelis_menten(x, v_max, k_m)
