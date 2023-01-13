import datetime

from django.http import HttpResponse
from rest_framework import viewsets, views, mixins, status, filters, generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Specification, Request, Offer
from .serializers import SpecificationSerializer, RequestSerializer, OfferSerializer, SpecificationsListSerializer
from .utils import excel_report
    

class GuideSpecificationsSelectAPIView(generics.ListAPIView):
    """
    View for input-select Specification
    """
    queryset = Specification.objects.filter(guide=True)
    serializer_class = SpecificationSerializer
    permission_classes = [IsAuthenticated]
    my_tags = ['SpecificationGuide']
    
    
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
    
    
class SpecificationExportView(views.APIView):
    my_tags = ['Specification']

    def get(self, request, *args, **kwargs):
        try:
            specification_obj = Specification.objects.get(id=kwargs['pk'])
            response = HttpResponse(excel_report(specification_obj, params=request.query_params), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Access-Control-Expose-Headers'] = "Content-Disposition"
            response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xlsx"'
            return response
        except Specification.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) 


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    my_tags = ['Request']


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]
    my_tags = ['Offer']
    