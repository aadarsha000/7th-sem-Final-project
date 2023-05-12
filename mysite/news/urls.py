from django.urls import path
from .views import news_scrap, All_news

urlpatterns =[
    path('news/scrap', news_scrap, name="news_scrap"),
    path('news/all', All_news.as_view(), name="all_news"),
]