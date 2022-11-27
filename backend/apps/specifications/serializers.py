from rest_framework import serializers

from .models import Specification, Request, Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
        

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class RequestOfferSerializer(serializers.ModelSerializer):
    offer = OfferSerializer(many=True, source="offer_set")
    
    class Meta:
        model = Request
        fields = '__all__'
                

class SpecificationRetrieveSerializer(serializers.ModelSerializer):
    requestOffer = RequestOfferSerializer(many=True, source="request_set")
    
    class Meta:
        model = Specification
        fields = '__all__'
        
        
class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'