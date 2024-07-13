from django.urls import path

from rs_back.events.router import ClassicEventViewSet, QuestionnaireViewSet

app_name = 'rs_back.events'
urlpatterns = [
    path('classic_events/<int:pk>/', ClassicEventViewSet.as_view()),
    path('classic_events/', ClassicEventViewSet.as_view()),
    path('questionnaire/<int:pk>/', QuestionnaireViewSet.as_view()),
    path('questionnaire/', QuestionnaireViewSet.as_view()),
]
