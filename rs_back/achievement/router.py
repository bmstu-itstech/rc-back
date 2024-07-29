from rest_framework.response import Response
from rest_framework.views import APIView

from rs_back.achievement.models import AchievementOrder
from rs_back.achievement.serializers import AchievementOrderSerializer


class AchievementViewSet(APIView):
    """!
    @brief API view для достижений
    @details Возвращает json всех достижений по порядку
    """

    def get(self, request, format=None):
        order = AchievementOrder.get_all_objects_by_order()
        serializer = AchievementOrderSerializer(instance=order, many=True)
        data = {
            'count': len(order),
            'data': serializer.data
        }
        return Response(data)
