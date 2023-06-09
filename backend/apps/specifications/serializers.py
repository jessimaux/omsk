from rest_framework import serializers

from .models import Specification, Request, Offer
        
        
class OfferSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    product_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    class Meta:
        model = Offer
        depth = 1
        exclude = ['request']
        

class GuideOfferSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    class Meta:
        model = Offer
        depth = 1
        exclude = ['request', 'id']
        
        
class RequestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    offers = OfferSerializer(many=True, source='offer_set')
    
    class Meta:
        model = Request
        exclude = ['specification']
                

class GuideRequestSerializer(serializers.ModelSerializer):
    offers = GuideOfferSerializer(many=True, source='offer_set')
    
    class Meta:
        model = Request
        exclude = ['specification', 'id']
        
        
class GuideSpecificationSerializer(serializers.ModelSerializer):
    requests = GuideRequestSerializer(many=True, source='request_set')
    
    class Meta:
        model = Specification
        exclude = ['project']
        
                
class SpecificationSerializer(serializers.ModelSerializer):
    requests = RequestSerializer(many=True, source='request_set')
    
    class Meta:
        model = Specification
        exclude = ['project']
    
    
class SpecificationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'