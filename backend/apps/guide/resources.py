from import_export import resources
from .models import ProductGuide


class ProductGuideResource(resources.ModelResource):
    class Meta:
        model = ProductGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')