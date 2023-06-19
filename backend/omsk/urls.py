from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('api/auth/', include('djoser.urls')),
   path('api/auth/', include('djoser.urls.authtoken')),

   path('api/', include('apps.projects.urls')),
   path('api/guide/', include('apps.guide.urls')),
   path('api/', include('apps.purchases.urls')),
   path('api/', include('apps.specifications.urls')),

   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
