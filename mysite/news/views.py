from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup
import requests
from .models import News
from django.views.generic import ListView



URL = "https://english.onlinekhabar.com/tag/nepal-agriculture"

all_news = []


def scrape_page(url):
    page = requests.get(URL)
    soap = BeautifulSoup(page.content, 'html.parser')
    get_data(soap)


def get_data(soap):
    div_news = soap.find('div', class_="listical-news-big")
    div_news_post = div_news.find_all('div', class_="ok-news-post ltr-post")

    for elem in div_news_post:
        news_div = elem.select('div h2 a')
        for i in news_div:
            heading = i.string
            link = i.get("href")
            new = {'heading': heading, 'link': link}
            all_news.append(new)


def main():
    scrape_page(URL)
    return all_news


def news_scrap(request):
    main()
    News.objects.all().delete()
    for data in all_news:
        news = News(heading=data['heading'], links=data['link'])
        news.save()
    return HttpResponse('ok')

# def all_news(request):
#     news = News.objects.all()
#     return render(request, 'news/all_news.html', {'news':news})

class All_news(ListView):
    model = News
    paginate_by = 5
    template_name = 'news/all_news.html'
    context_object_name = 'news'
