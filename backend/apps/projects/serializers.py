from rest_framework import serializers

from .models import Project
from apps.specifications.serializers import SpecificationSerializer


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(default=serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()
    
    class Meta:
        model = Project
        fields = '__all__'
        
        
class ProjectGetSerializer(ProjectSerializer):
    specification = SpecificationSerializer()