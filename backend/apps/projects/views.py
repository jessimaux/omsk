from django.shortcuts import render
from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer, ProjectGetSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectGetSerializer
        else:
            return ProjectSerializer
        