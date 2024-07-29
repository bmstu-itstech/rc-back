from django.urls import path

from rs_back.achievement.router import AchievementViewSet

app_name = 'rs_back.achievement'
urlpatterns = [
    path('', AchievementViewSet.as_view()),
]
