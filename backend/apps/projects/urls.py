from django.urls import path, re_path, include
from rest_framework import routers

from .views import ProjectsViewSet, ProjectRegistrationExportView, ProjectFileUploadAPIView, ProjectFileDeleteAPIView

router = routers.SimpleRouter()
router.register(r'', ProjectsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/registration-form/', ProjectRegistrationExportView.as_view(), name='project-registration-form'),
    path('file/upload/', ProjectFileUploadAPIView.as_view(), name='project-file-upload'),
    path('file/<int:pk>/delete/', ProjectFileDeleteAPIView.as_view(), name='project-file-delete')
]
