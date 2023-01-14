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

    def update(self, instance, validated_data):
        purchases = validated_data.pop('purchases')
        super().update(instance, validated_data)
        
        for purchase_item in purchases:
            if PurchaseOffer.objects.filter(id=purchase_item['id']):
                purchase_item_obj = PurchaseOffer.objects.get(id=purchase_item['id'])
                for attr, value in purchase_item.items():
                    setattr(purchase_item_obj, attr, value)
                purchase_item_obj.save()
        return instance
    