from .dose_response import DoseResponse

class LogisticP4Model(DoseResponse):
    def logistic_P4(self, x, b, c, d, e):
        """Calculate log-logistic curve (4-parameter model) at a given point"""
        f = c + (d - c) / (1 + np.exp(b * (np.log(x) - np.log(e))))
        return f
