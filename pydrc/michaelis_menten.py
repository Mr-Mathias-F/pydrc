from .dose_response import DoseResponse

class MichaelisMentenModel(DoseResponse):
    def michaelis_menten(self, x, v_max, k_m):
        """Calculate Michaelis-Menten"""
        v_0 = (v_max * x) / (k_m + x)
        return v_0
