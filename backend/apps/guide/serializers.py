from rest_framework import serializers

from .models import ProductGuide, PartnerGuide, ProviderGuide, ContactPartner, ContactProvider


class ContactPartnerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ContactPartner
        exclude = ['partner']
    
        
class ContactProviderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ContactProvider
        exclude = ['provider']
        

class ProductGuideSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField(read_only=True)
    provider_id = serializers.IntegerField()
    
    # logs
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = ProductGuide
        fields = '__all__'


class ProductGuideImportSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)


class PartnerGuideSerializer(serializers.ModelSerializer):
    contacts = ContactPartnerSerializer(many=True, source='contact_partner')
    
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = PartnerGuide
        fields = '__all__'
    
    
class PartnerGuideImportSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)


class ProviderGuideSerializer(serializers.ModelSerializer):
    contacts = ContactProviderSerializer(many=True, source='contact_provider', required=False)
    
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = ProviderGuide
        fields = '__all__'
    
    
class ProviderGuideImportSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)
