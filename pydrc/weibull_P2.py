from .dose_response import DoseResponse

class WeibullP2Model(DoseResponse):
    def weibull_P2(self, x, b, e):
        """Calculate two-parameter Weibull function"""
        f = np.exp(-np.exp(b * (np.log(x) - e)))
        return f
