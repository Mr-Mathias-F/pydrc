from .dose_response import DoseResponse

class MichaelisMentenModel(DoseResponse):
    def model_function(self, x, v_max, k_m):
        """Calculate Michaelis-Menten"""
        return (v_max * x) / (k_m + x)
