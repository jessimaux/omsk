from import_export import resources
from .models import ProductGuide, PartnerGuide, ProviderGuide


class ProductGuideResource(resources.ModelResource):
    class Meta:
        model = ProductGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')
        
        
class PartnerGuideResource(resources.ModelResource):
    class Meta:
        model = PartnerGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')
        

class ProviderGuideResource(resources.ModelResource):
    class Meta:
        model = ProviderGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')