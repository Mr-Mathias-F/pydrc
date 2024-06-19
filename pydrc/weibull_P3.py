from .dose_response import DoseResponse

class WeibullP3Model(DoseResponse):
    def weibull_P3(self, x, b, d, e):
        """Calculate three-parameter Weibull function"""
        f = (d - 0) * np.exp(-np.exp(b * (np.log(x) - e)))
        return f
