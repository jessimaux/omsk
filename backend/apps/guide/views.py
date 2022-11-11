import datetime

from django.http import HttpResponse
from rest_framework import viewsets, mixins, views, generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Q
from tablib import Dataset

from .models import ProductGuide, PartnerGuide, ProviderGuide, SpecificationGuide, RequestGuide, OfferGuide
from .serializers import ProductGuideSerializer, PartnerGuideSerializer, ProviderGuideSerializer, SpecificationGuideSerializer, \
    RequestGuideSerializer, OfferGuideSerializer, ProductGuideImportSerializer
from .resources import ProductGuideResource


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductGuide.objects.all()
    serializer_class = ProductGuideSerializer
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
    my_tags = ['PartnersGuide']


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = ProviderGuide.objects.all()
    serializer_class = ProviderGuideSerializer
    my_tags = ['ProvidersGuide']


class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = SpecificationGuide.objects.all()
    serializer_class = SpecificationGuideSerializer
    my_tags = ['SpecificationsGuide']


class RequestViewSet(viewsets.ModelViewSet):
    queryset = RequestGuide.objects.all()
    serializer_class = RequestGuideSerializer
    my_tags = ['RequestsGuide']


class OfferViewSet(viewsets.ModelViewSet):
    queryset = OfferGuide.objects.all()
    serializer_class = OfferGuideSerializer
    my_tags = ['OffersGuide']