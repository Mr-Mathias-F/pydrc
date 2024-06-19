from .dose_response import DoseResponse

class WeibullP4Model(DoseResponse):
    def weibull_P4(self, x, b, c, d, e):
        """Calculate four-parameter Weibull function"""
        f = c + (d - c) * np.exp(-np.exp(b * (np.log(x) - np.log(e))))
        return f
