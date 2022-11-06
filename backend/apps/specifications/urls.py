from django.urls import path, re_path, include
from rest_framework import routers

from .views import SpecificationsViewSet, RequestViewSet, OfferViewSet

router = routers.SimpleRouter()
router.register(r'specifications', SpecificationsViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'offers', OfferViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
