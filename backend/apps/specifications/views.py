from django.shortcuts import render
from rest_framework import viewsets, mixins

from .models import Specification, Request, Offer
from .serializers import SpecificationSerializer, RequestSerializer, RequestOfferSerializer,OfferSerializer


class SpecificationsViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    my_tags = ['Specification']


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    my_tags = ['Request']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return RequestOfferSerializer
        else:
            return RequestSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    my_tags = ['Offer']