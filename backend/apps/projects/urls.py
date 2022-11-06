from django.urls import path, re_path, include
from rest_framework import routers

from .views import ProjectsViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
