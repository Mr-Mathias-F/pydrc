from .dose_response import DoseResponse

class LogisticP2Model(DoseResponse):
    def model_function(self, x, b, e):
        """Calculate log-logistic curve (2-parameter model) at a given point"""
        return 1 / (1 + np.exp(b * (np.log(x) - np.log(e))))
