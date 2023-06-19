from django.urls import path, re_path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'specifications', SpecificationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
