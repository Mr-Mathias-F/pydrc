import unittest
from pydrc.logistic_P4 import LogisticP4Model
from tests.base_model_test import BaseModelTest

class TestLogisticP4Model(BaseModelTest):
    
    def setUp(self):
        super().setUp()
        self.model = LogisticP4Model()
