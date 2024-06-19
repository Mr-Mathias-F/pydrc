from .dose_response import DoseResponse

class LogisticP2Model(DoseResponse):
    def logistic_P2(self, x, b, e):
        """Calculate log-logistic curve (2-parameter model) at a given point"""
        f = 1 / (1 + np.exp(b * (np.log(x) - np.log(e))))
        return f
