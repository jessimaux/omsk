import datetime

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, views, status, filters, generics, mixins
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from .models import Project, File
from .serializers import ProjectSerializer, FileSerializer, ProjectListSerializer
from .services import *


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

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectSerializer
    
    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = ProjectService().create(serializer.validated_data, request.user.id)
        return Response(ProjectSerializer(result).data,
                        status=status.HTTP_201_CREATED)
        
    def update(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=kwargs.get('partial'))
        serializer.is_valid(raise_exception=True)
        result = ProjectService().update(kwargs['pk'], serializer.validated_data, request.user.id, kwargs.get('partial'))
        return Response(ProjectSerializer(result).data,
                        status=status.HTTP_200_OK)
        
    def destroy(self, request: Request, *args, **kwargs):
        ProjectService().destroy(kwargs['pk'], request.user.id)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    @swagger_auto_schema(method='get', responses={200: ''})
    @action(detail=False, url_path='(?P<pk>[^/.]+)/report_registration', pagination_class=None, filter_backends=None, serializer_class=None)
    def report_registration(self, request: Request, *args, **kwargs):
        response = HttpResponse(ProjectService().export_registration_form(
            kwargs['pk']), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Access-Control-Expose-Headers'] = "Content-Disposition"
        response['Content-Disposition'] = f'attachment; filename="{datetime.date.today()}.xlsx"'
        return response


class ProjectFileViewSet(mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [IsAuthenticated]
    my_tags = ['ProjectFiles']
    

    @swagger_auto_schema(responses={200: ''})
    def create(self, request: Request, *args, **kwargs):
        files = request.FILES.getlist("files")
        project_id = request.data['project']
        if 'files' not in request.FILES:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            ProjectFileService().create(project_id, files)
            return Response(status=status.HTTP_201_CREATED)
        
    @swagger_auto_schema(responses={200: ''})
    def destroy(self, request: Request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
