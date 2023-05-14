import unittest
import numpy as np
from .views import crop_recommendation_model

class TestCropRecommendation(unittest.TestCase):
    def output(self,N, P, K, temperature, humidity, ph, rainfall):
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        return final_prediction
    def test_recommendation(self):
        self.assertEqual(self.output(41,69,82,20.02,16.63,6.715,68.97), 'chickpea')