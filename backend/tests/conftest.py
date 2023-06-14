from typing import Callable

import pytest
import uuid
from rest_framework.test import APIClient
from django.contrib.auth.models import User
   

@pytest.fixture
def api_client() -> APIClient:
   return APIClient()

@pytest.fixture
def create_user(db, django_user_model) -> User:
  def make_user(**kwargs):
      kwargs['password'] = 'userpassword'
      if 'username' not in kwargs:
          kwargs['username'] = str(uuid.uuid4())
      return django_user_model.objects.create_user(**kwargs)
  return make_user

@pytest.fixture
def auto_login_user(db, api_client, create_user) -> tuple[APIClient, User]:
  def make_auto_login(user=None):
      if user is None:
          user = create_user()
      api_client.force_authenticate(user=user)
      return api_client, user
  return make_auto_login