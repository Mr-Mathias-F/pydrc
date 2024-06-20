from .dose_response import DoseResponse

class HillEquationModel(DoseResponse):
    def model_function(self, x, k_a, l, n):
        """Calculate Hill equation"""
        return 1 / (1 + (k_a / l) ** n)
