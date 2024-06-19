from .dose_response import DoseResponse

class GompertzModel(DoseResponse):
    def gompertz_model(self, x, b, c, d, e):
        """Calculate Gompertz model"""
        f = c + (d - c) * np.exp(-np.exp(b * (x - e)))
        return f
