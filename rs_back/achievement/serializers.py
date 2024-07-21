from rest_framework import serializers

from rs_back.achievement.models import Achievement, AchievementOrder


class DetailAchievementSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор
    @details Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Achievement
        fields = ('id', 'title', 'description', 'photo_album_url',
                  'link_to_media', 'photo',)


class AchievementOrderSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор
    @details Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = AchievementOrder
        fields = ('order', 'achievement',)

    achievement = DetailAchievementSerializer(required=True)
