from rest_framework import serializers

from .models import Log


class LogSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    
    class Meta:
        model = Log
        fields = '__all__'