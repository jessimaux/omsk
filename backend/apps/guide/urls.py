from django.urls import path, re_path, include
from rest_framework import routers

from .views import *
from apps.specifications.views import GuideSpecificationsViewSet, GuideSpecificationsSelectAPIView

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'providers', ProviderViewSet)
router.register(r'specifications', GuideSpecificationsViewSet)

urlpatterns = [
    path('specifications/select/', GuideSpecificationsSelectAPIView.as_view(), name='specification-select'),
    path('', include(router.urls)),
  ]
    