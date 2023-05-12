from django.urls import path
from .views import crop_prediction, index
urlpatterns = [
    path('', index, name='home'),
    path('crop/predict', crop_prediction, name='predict'),
]
