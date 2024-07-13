from rs_back.director.router import router
from django.urls import include, path

app_name = 'rs_back.director'
urlpatterns = [
    path('', include(router.urls))
]
