from .dose_response import DoseResponse

class ARModel(DoseResponse):
    def ar_model(self, x, c, d, e):
        """Calculate asymptotic regression model"""
        f = c + (d - c) * (1 - np.exp(-x / e))
        return f
