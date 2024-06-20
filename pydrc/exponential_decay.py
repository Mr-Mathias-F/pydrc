from .dose_response import DoseResponse

class ExponentialDecayModel(DoseResponse):
    def model_function(self, x, c, d, e):
        """Calculate exponential decay model"""
        return c + (d - c) * np.exp(-x / e)
