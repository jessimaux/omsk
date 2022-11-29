from rest_framework import serializers

from .models import Project
from apps.specifications.serializers import SpecificationSerializer, RequestSerializer
from apps.specifications.models import Specification


class ProjectSerializer(serializers.ModelSerializer):
    specification = SpecificationSerializer()
    
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(default=serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()
    
    class Meta:
        model = Project
        fields = '__all__'
        
    def create(self, validated_data):
        specifcation = validated_data.pop('specification')
        project_obj = Project.objects.create(**validated_data)
        SpecificationSerializer().create(validated_data=specifcation, project_id=project_obj.id)
        return project_obj
    
    def update(self, instance, validated_data):
        specifcation = validated_data.pop('specification')
        super().update(instance, validated_data)
        try:
            specification_obj = Specification.objects.get(project_id=instance.id)
        except Specification.DoesNotExist:
            serializers.ValidationError("Project doesnt have specification. Contact the system administrator.")
        SpecificationSerializer().update(instance=specification_obj, validated_data=specifcation)
        return instance
        