from rs_back.director.models import Director
from rs_back.director.serializers import DirectorSerializer
from rest_framework import routers, viewsets


class DirectorViewSet(viewsets.ModelViewSet):
    """!
    @brief Роутер для руководителей
    @details Нужен для автоматической маршрутизации
    @param queryset Список всех объектов из базы данных
    @param serializer_class Сериализатор
    """
    queryset = Director.get_all_objects_by_id()
    serializer_class = DirectorSerializer


router = routers.DefaultRouter()
router.register(r'', DirectorViewSet)
