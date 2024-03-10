from scipy.optimize import curve_fit

class MichaelisMenten:
    def __init__(self):
        self.params = None

    def michaelis_menten(self, x, v_max, k_m):
        """Calculate Michaelis-Menten"""
        v_0 = (v_max * x) / (k_m + x)
        return v_0

    def fit(self, x_data, y_data):
        """Estimate parameters (v_max, k_m)"""
        params, _ = curve_fit(self.michaelis_menten, x_data, y_data)
        self.params = params

    def predict(self, x):
        """Predict the rate of the Michaelis-Menten equation"""
        if self.params is None:
            raise ValueError("Parameters not estimated. Call fit() first.")
        v_max, k_m = self.params
        return self.michaelis_menten(x, v_max, k_m)
