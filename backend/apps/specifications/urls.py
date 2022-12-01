from django.urls import path, re_path, include
from rest_framework import routers

from .views import SpecificationsViewSet, RequestViewSet, OfferViewSet, SpecificationsPDFExportView

router = routers.SimpleRouter()
router.register(r'specifications', SpecificationsViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'offers', OfferViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/export_pdf/', SpecificationsPDFExportView.as_view(), name='export-pdf')
]
