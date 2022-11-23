import datetime
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, mixins, views

from .models import Specification, Request, Offer
from .serializers import SpecificationSerializer, RequestSerializer, RequestOfferSerializer,OfferSerializer
from .utils import render_to_pdf


class SpecificationsViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    my_tags = ['Specification']
    
    
class SpecificationsPDFExportView(views.APIView):
    my_tag = ['Specification']
    
    def get(self, request):
        data = {
            'specification': Specification.objects.all()
        }
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
    
    def get_serializer_class(self):
        if self.action == 'list':
            return RequestOfferSerializer
        else:
            return RequestSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    my_tags = ['Offer']