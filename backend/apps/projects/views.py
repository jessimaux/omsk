from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, views, status, filters, generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Project, File
from .serializers import ProjectSerializer, FileSerializer
from .utils import excel_report


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['id']
    my_tags = ['Project']
    
    
class ProjectRegistrationExportView(views.APIView):
    permission_classes = [IsAuthenticated]
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
    
    
class ProjectFileUploadAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    my_tags = ['ProjectFiles']
    
    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist("files")
        project = request.data['project']
        if 'files' not in request.FILES:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            for file in files:
                file_obj = File.objects.create(file=file, 
                                               name=file.name,
                                               project_id=project)
                
            return Response(status=status.HTTP_201_CREATED)
        

class ProjectFileDeleteAPIView(generics.DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]
    my_tags = ['ProjectFiles']
    