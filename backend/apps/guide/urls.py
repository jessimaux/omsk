from django.urls import path, re_path, include
from rest_framework import routers

from omsk.utils import CustomRouter
from .views import *

router = CustomRouter()
router.register(r'products', ProductViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'providers', ProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),
  ]
    