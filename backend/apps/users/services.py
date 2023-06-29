from django.contrib.auth.models import UserManager, User
from django.contrib.auth.hashers import make_password


class UserService:
    def create(self, user_data: dict) -> User:
        user_obj = User.objects.create_user(**user_data)
        return user_obj

    def update(self, user_id: int, user_data: dict) -> User:
        user_obj = User.objects.get(id=user_id)
        for attribute, value in user_data.items():
            if attribute == 'password':
                user_obj.password = make_password(value)
            else:
                setattr(user_obj, attribute, value)
        user_obj.save()
        return user_obj
    
    def get_me(self, user_id: int) -> User:
        return User.objects.get(id=user_id)
    