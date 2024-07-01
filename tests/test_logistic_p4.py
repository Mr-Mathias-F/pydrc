import pytest
import numpy as np
from doseresponse.models.logistic import LogisticP4Model

def test_logistic_p4_model_fit():
    x_data = np.array([1, 2, 3, 4, 5])
    y_data = np.array([2, 3, 5, 7, 11])
    model = LogisticP4Model()
    model.fit(x_data, y_data, initial_guess=[1, 1, 1, 1])
    assert model.params is not None

def test_logistic_p4_model_predict():
    x_data = np.array([1, 2, 3, 4, 5])
    y_data = np.array([2, 3, 5, 7, 11])
    model = LogisticP4Model()
    model.fit(x_data, y_data, initial_guess=[1, 1, 1, 1])
    predictions = model.predict(x_data)
    assert len(predictions) == len(x_data)

