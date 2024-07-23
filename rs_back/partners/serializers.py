from rest_framework import serializers

from rs_back.partners.models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    """
    Сериализатор
    Нужен для преобразования сложных типов данных в json
    """

    class Meta:
        model = Partner
        fields = ('id', 'title', 'link', 'photo')
