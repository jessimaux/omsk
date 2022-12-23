from rest_framework import serializers

from .models import Specification, Request, Offer
from apps.guide.serializers import ProductGuideSerializer
        
        
class OfferSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    product_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    class Meta:
        model = Offer
        depth = 1
        exclude = ['request']
        

class RequestSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    offers = OfferSerializer(many=True, source='offer_set')
    
    class Meta:
        model = Request
        exclude = ['specification']
                
        
class SpecificationSerializer(serializers.ModelSerializer):
    requests = RequestSerializer(many=True, source='request_set')
    
    class Meta:
        model = Specification
        exclude = ['project']
        
    def create(self, validated_data, project_id=None):
        requests = validated_data.pop('request_set')
        specification_obj = Specification.objects.create(project_id=project_id, **validated_data)
        
        for request in requests:
            offers = request.pop('offer_set')
            request_obj = Request.objects.create(specification=specification_obj, **request)
            for offer in offers:
                offer_obj = Offer.objects.create(request=request_obj, **offer)
                
        return specification_obj
    
    def update(self, instance, validated_data):
        requests = validated_data.pop('request_set')
        super().update(instance, validated_data)
        requests_from_db = Request.objects.filter(specification_id=instance.id).values_list('id', flat=True)
        requests_id_pool = []
        
        for request in requests:
            offers = request.pop('offer_set')
            offers_id_pool = []
            
            if "id" in request.keys() and Request.objects.filter(id=request['id']).exists():
                request_obj = Request.objects.get(id=request['id'])
                request_obj.str_by_order = request.get('str_by_order', request_obj.str_by_order)
                request_obj.name = request.get('name', request_obj.name)
                request_obj.tx = request.get('tx', request_obj.tx)
                request_obj.amount = request.get('amount', request_obj.amount)
                request_obj.price = request.get('price', request_obj.price)
                request_obj.save()
            else:
                request_obj = Request.objects.create(specification_id=instance.id, **request)

            offers_from_db = Offer.objects.filter(request_id=request_obj.id).values_list('id', flat=True)
            requests_id_pool.append(request_obj.id)
                
            for offer in offers:
                if "id" in offer.keys() and Offer.objects.filter(id=offer['id']).exists():
                    offer_obj = Offer.objects.get(id=offer['id'])
                    offer_obj.article = offer.get('article', offer_obj.article)
                    offer_obj.name = offer.get('name', offer_obj.name)
                    offer_obj.price = offer.get('price', offer_obj.price)
                    offer_obj.count = offer.get('count', offer_obj.count)
                    offer_obj.product_id = offer.get('product_id', offer_obj.product_id)
                    offer_obj.save()
                else:
                    offer_obj = Offer.objects.create(request_id=request_obj.id, **offer)
                
                offers_id_pool.append(offer_obj.id)
                    
            for offer_id in offers_from_db:
                if offer_id not in offers_id_pool:
                    Offer.objects.filter(id=offer_id).delete()
                    
        for request_id in requests_from_db:
            if request_id not in requests_id_pool:
                Request.objects.filter(id=request_id).delete()
        
        return instance
    
    
class SpecificationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'