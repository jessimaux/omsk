from typing import Callable

import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from django.contrib.auth.models import User
from apps.guide.models import *


pytestmark = pytest.mark.django_db


class TestPartnerGuide:
    endpoint = '/api/guide/partners/'

    def test_get_nonauth(self, api_client: APIClient):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_get_auth(self, auto_login_user: Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    def test_post(self, auto_login_user: Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        data = {
            'contacts': [
                {
                    'fio': 'Test',
                    'role': 'Test',
                    'phone': 'Test',
                    'email': 'Test'
                }
            ],
            'name': 'Test',
            'inn': 'Test',
            'region': 'Test',
            'discount': 0
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201

    def test_put(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        contact_obj = baker.make(ContactPartner)
        data = {
            'contacts': [
                {
                    'id': contact_obj.id,
                    'fio': 'Test',
                    'role': 'Test',
                    'phone': 'Test',
                    'email': 'Test'
                }
            ],
            'name': 'Test',
            'inn': 'Test',
            'region': 'Test',
            'discount': 0
        }
        response = api_client.put(self.endpoint+f'{contact_obj.partner.id}/', data=data, format='json')
        assert response.status_code == 200