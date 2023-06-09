import datetime

from django.http import HttpResponse
from rest_framework import viewsets, views, mixins, status, filters, generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from .services import *
from .models import *
from .serializers import *
    
    
class GuideSpecificationsViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.filter(guide=True)
    serializer_class = SpecificationSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['id']
    my_tags = ['SpecificationGuide']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return SpecificationsListSerializer
        return SpecificationSerializer
    
    @action(detail=False, pagination_class=None, filter_backends=None, serializer_class=GuideSpecificationSerializer)
    def select(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @swagger_auto_schema(method='get', responses={200: ''})
    @action(detail=False, pagination_class=None, filter_backends=None, serializer_class=None)
    def report_xlsx(self, request: Request, *args, **kwargs):
        response = HttpResponse(SpecificationService().report_xlsx(kwargs['pk'], request.query_params), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xlsx"'
        return response
