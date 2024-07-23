from rest_framework import serializers

from rs_back.hardathon.models import Hardathon, Project
from rs_back.partners.models import Partner


class HardathonSerializer(serializers.ModelSerializer):
    """
    Сериализатор
    Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Hardathon
        fields = ('id', 'title', 'photo',)


class HardathonByIdSerializer(serializers.ModelSerializer):
    """
    Сериализатор для одной записи
    Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Hardathon
        fields = ('id', 'title', 'photo', 'photo_album_url',
                  'documents_url', 'location',
                  'date_for_accepting_applications',
                  'closing_date_for_applications',
                  'summing_up_date', 'main_organizer_photo',
                  'main_organizer_word', 'competition_task',)


class DetailProjectSerializer(serializers.ModelSerializer):
    """
    Сериализатор
    Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'competition_rules',
                  'implementation_scale', 'photo',)


class HardathonProjectsSerializer(serializers.ModelSerializer):
    """
    Сериализатор
    Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Project
        fields = ('id', 'title',)


class HardathonPartnersSerializer(serializers.ModelSerializer):
    """
    Сериализатор
    Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Partner
        fields = ('id', 'title', 'link', 'photo')
