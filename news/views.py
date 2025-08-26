from django.shortcuts import render
from .models import News

def news_list(request):
    news = News.objects.order_by('-date')
    return render(request, 'news_list.html', {'news': news})
