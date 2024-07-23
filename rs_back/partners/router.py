from rest_framework.response import Response
from rest_framework.views import APIView

from rs_back.partners.models import Partner
from rs_back.partners.serializers import PartnerSerializer


class PartnerViewSet(APIView):
    """
    API view для партнёров
    Возвращает json всех партнёров в порядке их создания
    """

    def get(self, request, format=None):
        partners = Partner.get_all_objects_by_id()
        serializer = PartnerSerializer(instance=partners, many=True)
        data = {
            'count': len(partners),
            'partners': serializer.data
        }
        return Response(data)
