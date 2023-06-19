from rest_framework import serializers, fields

from .models import Project, File
from apps.specifications.serializers import SpecificationSerializer, RequestSerializer
from apps.specifications.models import Specification


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = File


# TODO: replace to service
class ProjectListSerializer(serializers.ModelSerializer):
    total_bill = fields.SerializerMethodField()
    total_complete = fields.SerializerMethodField()
    bill = fields.SerializerMethodField()
    first_products = serializers.SerializerMethodField(read_only=True)
    partner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def get_total_bill(self, obj):
        total = 0
        requests = obj.specification.requests.all()
        for request in requests:
            for offer in request.offers.all():
                total += offer.price * offer.count * request.amount
        return total

    def get_total_complete(self, obj):
        total = 0
        purchase_offers = obj.purchase.purchases.all()
        for purchase_offer in purchase_offers:
            if purchase_offer.status == 'Отгружен':
                total += purchase_offer.offer.price * purchase_offer.offer.count * purchase_offer.offer.request.amount
        return total

    def get_bill(self, obj):
        return obj.purchase.bill

    def get_first_products(self, obj):
        products = []
        requests = Specification.objects.get(project_id=obj.id).requests.all()
        count = 0
        for request in requests:
            for offer in request.offers.all():
                products.append(offer.name)
                count += 1
                if count >= 3:
                    break
        return products


class ProjectSerializer(serializers.ModelSerializer):
    specification = SpecificationSerializer()
    partner = serializers.StringRelatedField(read_only=True)
    partner_id = fields.IntegerField()
    purchase_id = fields.IntegerField(source='purchase.id', read_only=True)
    files = FileSerializer(many=True, required=False, read_only=True)

    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = Project
        fields = '__all__'
