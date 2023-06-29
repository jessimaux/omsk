from rest_framework import viewsets, filters, status, mixins
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.models import User

from .serializers import *
from .services import *
from .models import *


class LogViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['-id']
    my_tags = ['Logs']

    @action(detail=False, url_path='(?P<pk>[^/.]+)')
    def get_by_user_id(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Log.objects.filter(created_by_id=kwargs['pk']))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

        