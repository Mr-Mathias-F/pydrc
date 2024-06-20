from .dose_response import DoseResponse

class NecModel(DoseResponse):
    def model_function(self, x, c, b, d, e, b_2, d_2, e_2, I):
        """Calculate the no effect concentration model"""
        return c + (d - c) * np.exp(-b * (x - e) * I * (x - e)) + ((d_2) / (1 + np.exp(b_2 * (np.log(x)) - np.log(e_2))))
