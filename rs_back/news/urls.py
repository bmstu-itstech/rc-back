from django.urls import path
from rs_back.news.router import NewsViewSet

app_name = 'rs_back.news'
urlpatterns = [
    path('', NewsViewSet.as_view())
]
