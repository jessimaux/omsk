from rest_framework import viewsets, views, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from .models import Purchase
from .serializers import PurchaseSerializer
from .utils import excel_report


class PurchaseViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
  queryset = Purchase.objects.all()
  serializer_class = PurchaseSerializer
  permission_classes = [IsAuthenticated]
  my_tags = ['Purchase']
  
  
class PurchaseExportView(views.APIView):
    permission_classes = [IsAuthenticated]
    my_tags = ['Purchase']

    def get(self, request, *args, **kwargs):
        try:
            purchase_obj = Purchase.objects.get(id=kwargs['pk'])
            response = HttpResponse(excel_report(purchase_obj), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Access-Control-Expose-Headers'] = "Content-Disposition"
            response['Content-Disposition'] = 'attachment; filename="myexport.xlsx"'
            return response
        except Purchase.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) 