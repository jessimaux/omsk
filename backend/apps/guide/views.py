import datetime

from django.http import HttpResponse
from rest_framework import viewsets, views, generics, status
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from tablib import Dataset

from .models import ProductGuide, PartnerGuide, ProviderGuide
from .serializers import ProductGuideSerializer, PartnerGuideSerializer, ProviderGuideSerializer, \
    ProductGuideImportSerializer, PartnerGuideImportSerializer, ProviderGuideImportSerializer
from .resources import ProductGuideResource, PartnerGuideResource, ProviderGuideResource


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductGuide.objects.all()
    serializer_class = ProductGuideSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['article', 'name']
    my_tags = ['ProductsGuide']


class ProductExportView(views.APIView):
    my_tags = ['ProductsGuide']

    def get(self, request):
        product_resource = ProductGuideResource()
        dataset = product_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xls"'
        return response


class ProductImportView(generics.CreateAPIView):
    my_tags = ['ProductsGuide']
    serializer_class = ProductGuideImportSerializer

    def create(self, request):
        serializer_class = self.get_serializer(data=request.data)
        if 'file' not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            file_uploaded = request.FILES.get('file')
            person_resource = ProductGuideResource()
            dataset = Dataset()
            dataset.load(file_uploaded.read())

            # Test the data import
            result = person_resource.import_data(dataset, dry_run=True, raise_errors=True)
            if not result.has_errors():
                # Actually import now
                person_resource.import_data(dataset, dry_run=False)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        return Response(status=status.HTTP_201_CREATED)


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = PartnerGuide.objects.all()
    serializer_class = PartnerGuideSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['id']
    my_tags = ['PartnersGuide']


class PartnerExportView(views.APIView):
    my_tags = ['PartnersGuide']

    def get(self, request):
        partner_resource = PartnerGuideResource()
        dataset = partner_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xls"'
        return response


class PartnerImportView(generics.CreateAPIView):
    my_tags = ['PartnersGuide']
    serializer_class = PartnerGuideImportSerializer

    def create(self, request):
        serializer_class = self.get_serializer(data=request.data)
        if 'file' not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            file_uploaded = request.FILES.get('file')
            person_resource = PartnerGuideResource()
            dataset = Dataset()
            dataset.load(file_uploaded.read())

            # Test the data import
            result = person_resource.import_data(dataset, dry_run=True, raise_errors=True)
            if not result.has_errors():
                # Actually import now
                person_resource.import_data(dataset, dry_run=False)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        return Response(status=status.HTTP_201_CREATED)
    

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = ProviderGuide.objects.all()
    serializer_class = ProviderGuideSerializer
    pagination_class = PageNumberPagination
    my_tags = ['ProvidersGuide']


class ProviderExportView(views.APIView):
    my_tags = ['ProvidersGuide']

    def get(self, request):
        provider_resource = ProviderGuideResource()
        dataset = provider_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xls"'
        return response


class ProviderImportView(generics.CreateAPIView):
    my_tags = ['ProvidersGuide']
    serializer_class = ProviderGuideImportSerializer

    def create(self, request):
        serializer_class = self.get_serializer(data=request.data)
        if 'file' not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            file_uploaded = request.FILES.get('file')
            person_resource = ProviderGuideResource()
            dataset = Dataset()
            dataset.load(file_uploaded.read())

            # Test the data import
            result = person_resource.import_data(dataset, dry_run=True, raise_errors=True)
            if not result.has_errors():
                # Actually import now
                person_resource.import_data(dataset, dry_run=False)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        return Response(status=status.HTTP_201_CREATED)
