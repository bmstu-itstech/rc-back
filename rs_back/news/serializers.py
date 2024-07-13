from rest_framework import serializers

from rs_back.news.models import News


class NewsSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор
    @details Нужен для преобразовывания сложных типов данных в json
    """

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'new_url', 'photo')
