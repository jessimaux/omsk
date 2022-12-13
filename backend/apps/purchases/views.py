from rest_framework import viewsets, views, mixins

from .models import Purchase
from .serializers import PurchaseSerializer


class PurchaseViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
  queryset = Purchase.objects.all()
  serializer_class = PurchaseSerializer
  my_tags = ['Purchase']
  