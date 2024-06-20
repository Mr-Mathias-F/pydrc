from .dose_response import DoseResponse

class ARModel(DoseResponse):
    def model_function(self, x, c, d, e):
        """Calculate asymptotic regression model"""
        return c + (d - c) * (1 - np.exp(-x / e))
