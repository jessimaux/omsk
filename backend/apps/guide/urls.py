from django.urls import path, re_path, include
from rest_framework import routers

from .views import ProductViewSet, PartnerViewSet, ProviderViewSet, ProductExportView, ProductImportView, \
  ProviderExportView, ProviderImportView, PartnerExportView, PartnerImportView
from apps.specifications.views import GuideSpecificationsViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'providers', ProviderViewSet)
router.register(r'specifications', GuideSpecificationsViewSet)

urlpatterns = [
    path('products/export/', ProductExportView.as_view(), name='products-export'),
    path('products/import/', ProductImportView.as_view(), name='products-import'),
    path('partners/export/', PartnerExportView.as_view(), name='partners-export'),
    path('partners/import/', PartnerImportView.as_view(), name='partners-import'),
    path('providers/export/', ProviderExportView.as_view(), name='providers-export'),
    path('providers/import/', ProviderImportView.as_view(), name='providers-import'),
    path('', include(router.urls)),
  ]
