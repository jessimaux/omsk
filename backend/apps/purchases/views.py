import datetime

from rest_framework import viewsets, views, mixins, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema

from .models import Purchase
from .serializers import *
from .services import *


class PurchaseViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    my_tags = ['Purchase']

    def update(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = PurchaseService().update(kwargs['pk'], serializer.validated_data)
        return Response(PurchaseSerializer(result).data,
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(method='get', responses={200: ''})
    @action(detail=False, url_path='(?P<pk>[^/.]+)/export_xlsx', pagination_class=None, filter_backends=None, serializer_class=None)
    def export_xlsx(self, request: Request, *args, **kwargs):
        response = HttpResponse(PurchaseService().export_xlsx(kwargs['pk']),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xlsx"'
        return response
