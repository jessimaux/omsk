import datetime
from typing import Callable

import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from openpyxl import Workbook

from django.contrib.auth.models import User
from apps.guide.models import ProductGuide
from apps.specifications.models import *


pytestmark = pytest.mark.django_db


class TestSpecification:
    endpoint = '/api/specifications/'

    def test_get_nonauth(self, api_client: APIClient):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_get_auth(self, auto_login_user: Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    def test_post(self, auto_login_user: Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        product_obj = baker.make(ProductGuide)
        data = {
            'name': 'Test',
            'description': 'Test',
            'guide': True,
            'requests': [
                {
                    'str_by_order': 'Test',
                    'name': 'Test',
                    'tx': 'Test',
                    'amount': 0,
                    'price': 0,
                    'offers': [
                        {
                            'name': 'Test',
                            'article': 'Test',
                            'product_id': product_obj.id,
                            'count': 0,
                            'price': 0
                        }
                    ]
                }
            ]
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201

    def test_put(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        offer_obj = baker.make(Offer)
        data = {
            'name': 'Test',
            'description': 'Test',
            'guide': True,
            'requests': [
                {
                    'str_by_order': 'Test',
                    'name': 'Test',
                    'tx': 'Test',
                    'amount': 0,
                    'price': 0,
                    'offers': [
                        {
                            'name': 'Test',
                            'article': 'Test',
                            'product_id': None,
                            'count': 0,
                            'price': 0
                        }
                    ]
                }
            ]
        }
        response = api_client.put(self.endpoint+f'{offer_obj.request.specification.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_delete(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        specification_obj = baker.make(Specification, guide=True)
        response = api_client.delete(self.endpoint+f'{specification_obj.id}/')
        assert response.status_code == 204

    def test_report_xlsx(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        specification_obj = baker.make(Specification)
        response = api_client.get(self.endpoint+f'{specification_obj.id}/report_xlsx/')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        assert response.headers['content-disposition'] == f'attachment; filename="{datetime.date.today()}.xlsx"'
