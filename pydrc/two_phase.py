from .dose_response import DoseResponse

class TwoPhaseModel(DoseResponse):
    def model_function(self, x, c, b_1, b_2, d_1, d_2, e_1, e_2):
        """Calculate two-phase function"""
        return c + ((d_1 - c) / (1 + np.exp(b_1 * (np.log(x) - np.log(e_1))))) + (d_2 / (1 + np.exp(b_2 * (np.log(x) - np.log(e_2)))))
