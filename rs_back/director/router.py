from rest_framework import routers, viewsets

from rs_back.director.models import Director
from rs_back.director.serializers import DirectorSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    """
    Роутер для руководителей
    Нужен для автоматической маршрутизации
    """
    queryset = Director.get_all_objects_by_id()
    serializer_class = DirectorSerializer


router = routers.DefaultRouter()
router.register(r'', DirectorViewSet)
