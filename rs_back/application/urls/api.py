from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.urls import include, path


def version(_: WSGIRequest) -> JsonResponse:
    return JsonResponse({"version": settings.VERSION})


urlpatterns = [
    path('version/', version),
    path('news/', include('rs_back.news.urls')),
    path('achievements/', include('rs_back.achievement.urls')),
    path('partners/', include('rs_back.partners.urls')),
    path('', include('rs_back.hardathon.urls')),
    path('', include('rs_back.events.urls')),
]
