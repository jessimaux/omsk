from django.urls import path, re_path, include
from rest_framework import routers

from .views import ProductViewSet, PartnerViewSet, ProviderViewSet, SpecificationViewSet, RequestViewSet, OfferViewSet, \
    ProductExportView, ProductImportView

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'providers', ProviderViewSet)
router.register(r'specifications', SpecificationViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'offers', OfferViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/export', ProductExportView.as_view(), name='product-export'),
    path('products/import', ProductImportView.as_view({'post': 'create'}))
  ]
