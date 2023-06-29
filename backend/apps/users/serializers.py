from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'username': {'read_only': True},
            'password': {'write_only': True, 'required': False}
        }
