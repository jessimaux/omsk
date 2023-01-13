import datetime

from django.http import HttpResponse
from rest_framework import viewsets, views, generics, status, mixins
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from tablib import Dataset

from .models import ProductGuide, PartnerGuide, ProviderGuide
from .serializers import ProductGuideSerializer, PartnerGuideSerializer, ProviderGuideSerializer, \
    ProductGuideImportSerializer, PartnerGuideImportSerializer, ProviderGuideImportSerializer
from .resources import ProductGuideResource, PartnerGuideResource, ProviderGuideResource
from .utils import import_partners, export_partners, export_providers, import_providers, check_xlsx_file_import


class ProductSearchAPIView(generics.ListAPIView):
    """
    View for get list of products for select product in specification
    """
    queryset = ProductGuide.objects.all()
    serializer_class = ProductGuideSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['article', 'name']
    my_tags = ['ProductsGuide']


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


class ProductExportView(views.APIView):
    permission_classes = [IsAuthenticated]
    my_tags = ['ProductsGuide']

    def get(self, request):
        product_resource = ProductGuideResource()
        dataset = product_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xls"'
        return response


class ProductImportView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductGuideImportSerializer
    my_tags = ['ProductsGuide']
    
    def create(self, request):
        serializer_class = self.get_serializer(data=request.data)
        if check_xlsx_file_import(request, serializer_class):
            try:
                file_uploaded = request.FILES.get('file')
                product_resource = ProductGuideResource()
                dataset = Dataset()
                dataset.load(file_uploaded.read())

                # Test the data import, if it's ok - finally import it
                result = product_resource.import_data(dataset, dry_run=True)
                if not result.has_errors():
                    product_resource.import_data(dataset, dry_run=False)
                else:
                    return Response({'non_field_errors': result}, status=status.HTTP_400_BAD_REQUEST)
            except IOError:                
                return Response({'non_field_errors': 'Файл содержит некорректные данные.'}, status=status.HTTP_400_BAD_REQUEST)
           
        return Response({"success": "Файл успешно загружен."}, status=status.HTTP_201_CREATED)


class PartnerSelectAPIView(generics.ListAPIView):
    """ 
    View for get list of partner for input-select 
    """
    queryset = PartnerGuide.objects.all()
    serializer_class = PartnerGuideSerializer
    permission_classes = [IsAuthenticated]
    my_tags = ['PartnersGuide']
    
    
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


class PartnerExportView(views.APIView):
    permission_classes = [IsAuthenticated]
    my_tags = ['PartnersGuide']

    def get(self, request):
        response = HttpResponse(export_partners(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xls"'
        return response


class PartnerImportView(generics.CreateAPIView):
    serializer_class = PartnerGuideImportSerializer
    permission_classes = [IsAuthenticated]
    my_tags = ['PartnersGuide']

    def create(self, request):
        serializer_class = self.get_serializer(data=request.data)
        if check_xlsx_file_import(request, serializer_class):
            file_uploaded = request.FILES.get('file')
            try:
                import_partners(file_uploaded.file)
            except Exception:
                return Response({'non_field_errors': 'Файл содержит некорректные данные.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Файл успешно загружен.'}, status=status.HTTP_201_CREATED)
    

class ProviderSelectAPIView(generics.ListAPIView):
    """ 
    View for get list of provider for input-select 
    """
    queryset = ProviderGuide.objects.all()
    serializer_class = ProviderGuideSerializer
    permission_classes = [IsAuthenticated]
    my_tags = ['ProvidersGuide']
    
    
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


class ProviderExportView(views.APIView):
    permission_classes = [IsAuthenticated]
    my_tags = ['ProvidersGuide']

    def get(self, request):
        response = HttpResponse(export_providers(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xls"'
        return response


class ProviderImportView(generics.CreateAPIView):
    serializer_class = ProviderGuideImportSerializer
    permission_classes = [IsAuthenticated]
    my_tags = ['ProvidersGuide']
    

    def create(self, request):
        serializer_class = self.get_serializer(data=request.data)
        if check_xlsx_file_import(request, serializer_class):
            file_uploaded = request.FILES.get('file')
            try:
                import_providers(file_uploaded.file)
            except Exception:
                return Response({'non_field_errors': 'Файл содержит некорректные данные.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': 'Файл успешно загружен.'}, status=status.HTTP_201_CREATED)

