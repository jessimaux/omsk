from django.urls import path, re_path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
