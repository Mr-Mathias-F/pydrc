from .dose_response import DoseResponse

class WeibullP4Model(DoseResponse):
    def model_function(self, x, b, c, d, e):
        """Calculate four-parameter Weibull function"""
        return c + (d - c) * np.exp(-np.exp(b * (np.log(x) - np.log(e))))
