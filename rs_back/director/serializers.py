from rest_framework import serializers

from rs_back.director.models import Director


class DirectorSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор
    @details Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Director
        fields = ('fio', 'email', 'role', 'photo')
