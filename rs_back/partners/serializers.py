from rs_back.partners.models import Partner
from rest_framework import serializers


class PartnerSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор
    @details Нужен для преобразовывания сложных типов данных в json
    """
    class Meta:
        model = Partner
        fields = ('id', 'title', 'link', 'photo')
