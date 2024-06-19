from .dose_response import DoseResponse

class HillEquationModel(DoseResponse):
    def hill_eq(self, x, k_a, l, n):
        """Calculate Hill equation"""
        t = 1 / (1 + (k_a / l) ** n)
        return t
