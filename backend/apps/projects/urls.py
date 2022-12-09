from django.urls import path, re_path, include
from rest_framework import routers

from .views import ProjectsViewSet, ProjectRegistrationExportView

router = routers.SimpleRouter()
router.register(r'', ProjectsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/registration-form/', ProjectRegistrationExportView.as_view(), name='project-registration-form')
]
