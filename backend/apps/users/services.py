from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework.generics import get_object_or_404

from apps.logs.services import LogService


class UserService:
    def __init__(self) -> None:
        self.log_service = LogService()
       
    @transaction.atomic 
    def create(self, user_data: dict, created_by_id: int) -> User:
        user_obj = User.objects.create_user(**user_data)
        self.log_service.create(obj_type='User',
                                obj_id=user_obj.id,
                                action='Create',
                                created_by_id=created_by_id)
        return user_obj

    @transaction.atomic
    def update(self, user_id: int, user_data: dict, created_by_id: int) -> User:
        user_obj = User.objects.get(id=user_id)
        for attribute, value in user_data.items():
            if attribute == 'password':
                user_obj.password = make_password(value)
            else:
                setattr(user_obj, attribute, value)
        user_obj.save()
        self.log_service.create(obj_type='User',
                                obj_id=user_obj.id,
                                action='Update',
                                created_by_id=created_by_id)
        return user_obj
    
    @transaction.atomic
    def destroy(self, user_id: int, created_by_id: int):
        partner_obj = get_object_or_404(User.objects.filter(id=user_id))
        partner_obj.delete()
        self.log_service.create(obj_type='User',
                                obj_id=user_id,
                                action='Delete',
                                created_by_id=created_by_id)
    
    def get_me(self, user_id: int) -> User:
        return User.objects.get(id=user_id)
    