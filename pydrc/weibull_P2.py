from .dose_response import DoseResponse

class WeibullP2Model(DoseResponse):
    def model_function(self, x, b, e):
        """Calculate two-parameter Weibull function"""
        return np.exp(-np.exp(b * (np.log(x) - e)))
