from django.conf import settings
from django.conf.urls.static import static
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.urls import include, path, re_path
from django.views.static import serve


def version(_: WSGIRequest) -> JsonResponse:
    return JsonResponse({"version": settings.VERSION})


urlpatterns = [
    path('version/', version),
    path('news/', include('news.urls')),
    path('achievements/', include('achievement.urls')),
    path('partners/', include('partners.urls')),
    path('', include('hardathon.urls')),
    path('', include('events.urls')),

]

if settings.DEBUG and not settings.LOCAL_MEDIA:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

if settings.LOCAL_MEDIA:
    urlpatterns += [
        re_path(
            r"^dj_media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
        re_path(
            r"^dj_static/(?P<path>.*)$",
            serve,
            {"document_root": settings.STATIC_ROOT},
        ),
    ]

