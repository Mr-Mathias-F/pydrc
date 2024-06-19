from .dose_response import DoseResponse

class ExponentialDecayModel(DoseResponse):
    def exponential_decay(self, x, c, d, e):
        """Calculate exponential decay model"""
        f = c + (d - c) * np.exp(-x / e)
        return f
