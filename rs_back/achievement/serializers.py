from rest_framework import serializers

from rs_back.achievement.models import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор
    @details Нужен для преобразовывания сложных типов данных в json
    """

    class Meta:
        model = Achievement
        fields = ('id', 'title', 'description', 'photo_album_url',
                  'link_to_media', 'photo')
