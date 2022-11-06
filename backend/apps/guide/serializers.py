from rest_framework import serializers
from .models import ProductGuide, PartnerGuide, ProviderGuide, SpecificationGuide, OfferGuide, RequestGuide


class ProductGuideSerializer(serializers.ModelSerializer):
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
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = PartnerGuide
        fields = '__all__'


class ProviderGuideSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = ProviderGuide
        fields = '__all__'


class SpecificationGuideSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = SpecificationGuide
        fields = '__all__'


class RequestGuideSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = RequestGuide
        fields = '__all__'


class OfferGuideSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = OfferGuide
        fields = '__all__'