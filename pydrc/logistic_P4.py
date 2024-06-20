from .dose_response import DoseResponse

class LogisticP4Model(DoseResponse):
    def model_function(self, x, b, c, d, e):
        """Calculate log-logistic curve (4-parameter model) at a given point"""
        return c + (d - c) / (1 + np.exp(b * (np.log(x) - np.log(e))))
