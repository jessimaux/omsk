from django.urls import path, re_path, include
from rest_framework import routers

from omsk.utils import CustomRouter
from .views import *

router = CustomRouter()
router.register(r'projects', ProjectsViewSet)
router.register(r'projects-files', ProjectFileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
