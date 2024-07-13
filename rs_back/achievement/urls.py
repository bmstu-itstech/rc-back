from rs_back.achievement.router import AchievementViewSet
from django.urls import path

app_name = 'rs_back.achievement'
urlpatterns = [
    path('', AchievementViewSet.as_view())
]
