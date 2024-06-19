from .dose_response import DoseResponse

class LogisticP3Model(DoseResponse):
    def logistic_P3(self, x, b, c, e):
        """Calculate log-logistic curve (3-parameter model) at a given point"""
        f = c + (1 - c) / (1 + np.exp(b * (np.log(x) - e)))
        return f
