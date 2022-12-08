import datetime

from django.http import HttpResponse
from rest_framework import viewsets, views, mixins, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Specification, Request, Offer
from .serializers import SpecificationSerializer, RequestSerializer, OfferSerializer
from .utils import render_to_pdf, excel_report


class SpecificationsViewSet(mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    my_tags = ['Specification']
    

class GuideSpecificationsViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.filter(guide=True)
    serializer_class = SpecificationSerializer
    pagination_class = PageNumberPagination
    my_tags = ['SpecificationGuide']
    
    
class SpecificationExportView(views.APIView):
    my_tags = ['Specification']

    def get(self, request, *args, **kwargs):
        try:
            specification_obj = Specification.objects.get(id=kwargs['pk'])
            response = HttpResponse(excel_report(specification_obj, params=request.query_params), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Access-Control-Expose-Headers'] = "Content-Disposition"
            response['Content-Disposition'] = 'attachment; filename="myexport.xlsx"'
            return response
        except Specification.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

        
    
class SpecificationsPDFExportView(views.APIView):
    my_tag = ['Specification']
    
    def get(self, request, *args, **kwargs):
        try:
            data = {
                'specification': Specification.objects.get(id=kwargs['pk'])
            }
        except Specification.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        pdf = render_to_pdf('specifications/pdf.html', data)
        
        if pdf:
            response = HttpResponse(pdf, content_type = 'application/pdf')
            # response['Access-Control-Expose-Headers'] = "Content-Disposition"
            # response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.pdf"'
            return response


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    my_tags = ['Request']


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    my_tags = ['Offer']