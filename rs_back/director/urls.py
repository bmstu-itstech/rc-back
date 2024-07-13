from django.urls import include, path

from rs_back.director.router import router

app_name = 'rs_back.director'
urlpatterns = [
    path('', include(router.urls))
]
