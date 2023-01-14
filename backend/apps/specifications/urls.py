from django.urls import path, re_path, include
from rest_framework import routers

from .views import SpecificationExportView

router = routers.SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/export/', SpecificationExportView.as_view(), name='specification-export')
]
