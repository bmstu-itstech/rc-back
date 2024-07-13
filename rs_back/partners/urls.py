from django.urls import path

from rs_back.partners.router import PartnerViewSet

app_name = 'rs_back.partners'
urlpatterns = [
    path('', PartnerViewSet.as_view())
]
