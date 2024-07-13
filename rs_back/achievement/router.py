from rest_framework.response import Response
from rest_framework.views import APIView

from rs_back.achievement.models import Achievement
from rs_back.achievement.serializers import AchievementSerializer


class AchievementViewSet(APIView):
    """!
    @brief API view для достижений
    @details Возвращает json всех достижений в порядке их создания
    """

    def get(self, request, format=None):
        achievements = Achievement.get_all_objects_by_id()
        serializer = AchievementSerializer(instance=achievements, many=True)
        data = {
            'count': len(achievements),
            'data': serializer.data
        }
        return Response(data)
