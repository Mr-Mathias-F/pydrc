from .dose_response import DoseResponse

class GompertzModel(DoseResponse):
    def model_function(self, x, b, c, d, e):
        """Calculate Gompertz model"""
        return c + (d - c) * np.exp(-np.exp(b * (x - e)))
