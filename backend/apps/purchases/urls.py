from django.urls import path, re_path, include
from rest_framework import routers

from apps.purchases import views

router = routers.SimpleRouter()
router.register(r'', views.PurchaseViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('<int:pk>/export/', views.PurchaseExportView.as_view(), name='purchase-export'),
]
