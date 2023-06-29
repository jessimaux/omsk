import datetime

from django.http import HttpResponse
from rest_framework import viewsets, views, generics, status, mixins, filters
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *
from .resources import *
from .services import *


IMPORT_EXTENSIONS = ('application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductGuide.objects.all()
    serializer_class = ProductGuideSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['article', 'name']
    ordering_fields = '__all__'
    ordering = ['id']
    my_tags = ['ProductsGuide']
    
    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = ProductService().create(serializer.validated_data, request.user.id)
        return Response(ProductGuideSerializer(result).data, 
                        status=status.HTTP_201_CREATED)
        
    def update(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = ProductService().update(kwargs['pk'], serializer.validated_data, request.user.id)
        return Response(ProductGuideSerializer(result).data, 
                        status=status.HTTP_200_OK)
        
    def destroy(self, request: Request, *args, **kwargs):
        ProductService().destroy(kwargs['pk'], request.user.id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, pagination_class=LimitOffsetPagination)
    def search(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(method='get', responses={200: ''})
    @action(detail=False, pagination_class=None, filter_backends=None, serializer_class=None)
    def export_xlsx(self, request: Request, *args, **kwargs):
        product_resource = ProductGuideResource()
        dataset = product_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xls"'
        return response

    @action(detail=False, methods=['post'], serializer_class=ProductGuideImportSerializer)
    def import_xlsx(self, request: Request):
        serializer_class = self.get_serializer(data=request.data)
        if 'file' not in request.FILES or not serializer_class.is_valid():
            return Response({'non_field_errors': 'Файл не выбран.'}, status=status.HTTP_400_BAD_REQUEST)
        elif request.FILES['file'].content_type not in IMPORT_EXTENSIONS:
            return Response({'non_field_errors': 'Выбран некорректный формат файла.'}, status=status.HTTP_400_BAD_REQUEST)

        result = ProductService().import_xlsx(request.FILES.get('file'))

        return Response({"message": "Файл успешно импортирован.",
                        "details": result},
                        status=status.HTTP_200_OK)


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = PartnerGuide.objects.all()
    serializer_class = PartnerGuideSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['id']
    my_tags = ['PartnersGuide']
    
    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = PartnerService().create(serializer.validated_data, request.user.id)
        return Response(PartnerGuideSerializer(result).data,
                        status=status.HTTP_201_CREATED)

    def update(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = PartnerService().update(kwargs['pk'], serializer.validated_data, request.user.id)
        return Response(PartnerGuideSerializer(result).data,
                        status=status.HTTP_200_OK)
        
    def destroy(self, request: Request, *args, **kwargs):
        PartnerService().destroy(kwargs['pk'], request.user.id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, pagination_class=None)
    def select(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(method='get', responses={200: ''})
    @action(detail=False, pagination_class=None, filter_backends=None, serializer_class=None)
    def export_xlsx(self, request: Request):
        response = HttpResponse(PartnerService().export_xlsx(),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xls"'
        return response
    
    @action(detail=False, methods=['post'], serializer_class=PartnerGuideImportSerializer)
    def import_xlsx(self, request: Request):
        serializer_class = self.get_serializer(data=request.data)
        if 'file' not in request.FILES or not serializer_class.is_valid():
            return Response({'non_field_errors': 'Файл не выбран.'}, status=status.HTTP_400_BAD_REQUEST)
        elif request.FILES['file'].content_type not in IMPORT_EXTENSIONS:
            return Response({'non_field_errors': 'Выбран некорректный формат файла.'}, status=status.HTTP_400_BAD_REQUEST)
        PartnerService().import_xlsx(request.FILES.get('file'))
        return Response({'message': 'Файл успешно загружен.'}, status=status.HTTP_200_OK)


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = ProviderGuide.objects.all()
    serializer_class = ProviderGuideSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['id']
    my_tags = ['ProvidersGuide']

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = ProviderService().create(serializer.validated_data, request.user.id)
        return Response(ProviderGuideSerializer(result).data,
                        status=status.HTTP_201_CREATED)

    def update(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = ProviderService().update(kwargs['pk'], serializer.validated_data, request.user.id)
        return Response(ProviderGuideSerializer(result).data,
                        status=status.HTTP_200_OK)
        
    def destroy(self, request: Request, *args, **kwargs):
        ProviderService().destroy(kwargs['pk'], request.user.id)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    @action(detail=False, pagination_class=None)
    def select(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @swagger_auto_schema(method='get', responses={200: ''})
    @action(detail=False, pagination_class=None, filter_backends=None, serializer_class=None)
    def export_xlsx(self, request: Request, *args, **kwargs):
        response = HttpResponse(ProviderService().export_xlsx(), 
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xls"'
        return response
    
    @action(detail=False, methods=['post'], pagination_class=None, filter_backends=None, serializer_class=ProviderGuideImportSerializer)
    def import_xlsx(self, request: Request, *args, **kwargs):
        serializer_class = self.get_serializer(data=request.data)
        if 'file' not in request.FILES or not serializer_class.is_valid():
            return Response({'non_field_errors': 'Файл не выбран.'}, status=status.HTTP_400_BAD_REQUEST)
        elif request.FILES['file'].content_type not in IMPORT_EXTENSIONS:
            return Response({'non_field_errors': 'Выбран некорректный формат файла.'}, status=status.HTTP_400_BAD_REQUEST)
        ProviderService().import_xlsx(request.FILES.get('file'))
        return Response({'message': 'Файл успешно импортирован.'}, status=status.HTTP_200_OK)
