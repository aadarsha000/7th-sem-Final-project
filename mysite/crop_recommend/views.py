from django.shortcuts import render, redirect
from django.http import HttpResponse
import numpy as np
import pandas as pd
import pickle
from django.contrib.auth.decorators import login_required

from .forms import condition_input

# Loading crop recommendation model

crop_recommendation_model_path = 'crop_recommend/recommend_model/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, 'crop_recommend/index.html')


# predicting crop from the input
def crop_prediction(request):
    if request.method == "POST":
        form = condition_input(request.POST)
        if form.is_valid():
            N = float(form.cleaned_data['nitrogen'])
            P = float(form.cleaned_data['phosphorous'])
            K = float(form.cleaned_data['pottasium'])
            temperature = float(form.cleaned_data['temperature'])
            humidity = float(form.cleaned_data['humidity'])
            ph = float(form.cleaned_data['ph'])
            rainfall = float(form.cleaned_data['rainfall'])
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]
            return render(request, 'crop_recommend/result.html', {'final_prediction':final_prediction})
    form = condition_input(request.POST)
    return render(request, 'crop_recommend/forms.html', {'forms':form})