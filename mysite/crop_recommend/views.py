from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import pickle


# Loading crop recommendation model

crop_recommendation_model_path = 'crop_recommend/recommend_model/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

# Create your views here.
def crop_prediction(request):
    N = 83
    P = 80
    K = 60
    temperature = 28
    humidity = 70.3
    ph = 7.0
    rainfall = 150.9
    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    my_prediction = crop_recommendation_model.predict(data)
    final_prediction = my_prediction[0]

    return HttpResponse(final_prediction)