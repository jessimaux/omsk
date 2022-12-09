from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Project
from .serializers import ProjectSerializer
from .utils import excel_report


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = PageNumberPagination
    my_tags = ['Project']
    
    
class ProjectRegistrationExportView(views.APIView):
    my_tags = ['Project']

    def get(self, request, *args, **kwargs):
        try:
            project_obj = Project.objects.get(id=kwargs['pk'])
            response = HttpResponse(excel_report(project_obj), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Access-Control-Expose-Headers'] = "Content-Disposition"
            response['Content-Disposition'] = 'attachment; filename="myexport.xlsx"'
            return response
        except Project.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) 