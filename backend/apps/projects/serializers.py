from rest_framework import serializers, fields

from .models import Project, File
from apps.specifications.serializers import SpecificationSerializer, RequestSerializer
from apps.specifications.models import Specification
from apps.purchases.models import Purchase
from apps.purchases.serializers import PurchaseSerializer


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = File


class ProjectSerializer(serializers.ModelSerializer):
    specification = SpecificationSerializer()
    purchase = PurchaseSerializer(read_only=True)
    purchase_id = fields.IntegerField(source='purchase.id', read_only=True)
    partner_id = fields.IntegerField()
    files = FileSerializer(many=True, required=False, read_only=True)
    
    created_by = serializers.CharField(default=serializers.CreateOnlyDefault(default=serializers.CurrentUserDefault()), read_only=True)
    updated_by = serializers.CharField(default=serializers.CurrentUserDefault(), read_only=True)
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()
    
    class Meta:
        model = Project
        fields = '__all__'
        depth = 1
        
    def create(self, validated_data):
        specifcation = validated_data.pop('specification')
        project_obj = Project.objects.create(**validated_data)
        SpecificationSerializer().create(validated_data=specifcation, project_id=project_obj.id)
        return project_obj
    
    def update(self, instance, validated_data):
        if not self.partial:
            specifcation = validated_data.pop('specification')
        super().update(instance, validated_data)
        if not self.partial:
            try:
                specification_obj = Specification.objects.get(project_id=instance.id)
            except Specification.DoesNotExist:
                serializers.ValidationError("Project doesnt have specification. Contact the system administrator.")
            SpecificationSerializer().update(instance=specification_obj, validated_data=specifcation)
        return instance
        
