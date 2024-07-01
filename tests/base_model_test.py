import unittest
import numpy as np

class BaseModelTest(unittest.TestCase):
    
    def setUp(self):
        self.x_data = np.array([1, 2, 3, 4, 5])
        self.y_data = np.array([2, 3, 5, 7, 11])
        self.initial_guess = [1, 1, 1, 1]
        self.model = None

    def test_model_fit(self):
        self.model.fit(self.x_data, self.y_data, initial_guess=self.initial_guess)
        self.assertIsNotNone(self.model.params)
    
    def test_model_predict(self):
        self.model.fit(self.x_data, self.y_data, initial_guess=self.initial_guess)
        predictions = self.model.predict(self.x_data)
        self.assertEqual(len(predictions), len(self.x_data))

