from .dose_response import DoseResponse

class WeibullP3Model(DoseResponse):
    def model_function(self, x, b, d, e):
        """Calculate three-parameter Weibull function"""
        return (d - 0) * np.exp(-np.exp(b * (np.log(x) - e)))
