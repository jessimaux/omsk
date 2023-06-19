from rest_framework import serializers, fields

from .models import Purchase, PurchaseOffer
from apps.specifications.serializers import OfferSerializer


class PurchaseOfferSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = PurchaseOffer
        depth = 2
        exclude = ['purchase']


class PurchaseSerializer(serializers.ModelSerializer):
    purchases = PurchaseOfferSerializer(many=True)
    
    class Meta:
        model = Purchase
        exclude = ['project']


class PurchaseInputSerializer(serializers.Serializer):
    project_id = serializers.IntegerField()