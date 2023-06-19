import datetime
from typing import Callable

import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from openpyxl import Workbook

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

    def test_delete(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        contact_obj = baker.make(ContactPartner)
        response = api_client.delete(self.endpoint+f'{contact_obj.partner.id}/')
        assert response.status_code == 204
        
    def test_export(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        response = api_client.get(self.endpoint+'export_xlsx/')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        assert response.headers['content-disposition'] == f'attachment; filename="{datetime.date.today()}.xls"'

    # TODO: create xls file here
    def test_import(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        contact_obj = baker.make(ContactPartner)
        with open('tests/guide/files/guide_partner_import.xls', 'rb') as f:
            response = api_client.post(self.endpoint+'import_xlsx/', data={'file': f})
        assert response.status_code == 200


class TestProviderGuide:
    endpoint = '/api/guide/providers/'

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
            'sphere': 'Test',
            'inn': 'Test',
            'region': 'Test',
            'discount': 0
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201

    def test_put(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        contact_obj = baker.make(ContactProvider)
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
            'sphere': 'Test',
            'inn': 'Test',
            'region': 'Test',
            'discount': 0
        }
        response = api_client.put(self.endpoint+f'{contact_obj.provider.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_delete(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        contact_obj = baker.make(ContactProvider)
        response = api_client.delete(self.endpoint+f'{contact_obj.provider.id}/')
        assert response.status_code == 204

    def test_export(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        response = api_client.get(self.endpoint+'export_xlsx/')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        assert response.headers['content-disposition'] == f'attachment; filename="{datetime.date.today()}.xls"'

    # TODO: create xls file here
    def test_import(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        contact_obj = baker.make(ContactProvider)
        with open('tests/guide/files/guide_provider_import.xls', 'rb') as f:
            response = api_client.post(self.endpoint+'import_xlsx/', data={'file': f})
        assert response.status_code == 200
        
        
class TestProductGuide:
    endpoint = '/api/guide/products/'
    
    def test_get_nonauth(self, api_client: APIClient):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_get_auth(self, auto_login_user: Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    def test_post(self, auto_login_user: Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        contact_obj = baker.make(ContactProvider)
        data = {
            'provider_id': contact_obj.provider.id,
            'name': 'Test',
            'article': 'Test',
            'str_by_order': 'Test',
            'price_rrc': 0,
            'price_buy': 0,
            'link': 'Test',
            'country': 'Test',
            'description': 'Test',
            'description_tech': 'Test',
            'description_add': 'Test',
            'recommendation': 'Test',
            'nds': 0,
            'available': 0
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201

    def test_put(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        product_obj = baker.make(ProductGuide)
        data = {
            'provider_id': product_obj.provider.id,
            'name': 'Test',
            'article': 'Test',
            'str_by_order': 'Test',
            'price_rrc': 0,
            'price_buy': 0,
            'link': 'Test',
            'country': 'Test',
            'description': 'Test',
            'description_tech': 'Test',
            'description_add': 'Test',
            'recommendation': 'Test',
            'nds': 0,
            'available': 0
        }
        response = api_client.put(self.endpoint+f'{product_obj.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_delete(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        product_obj = baker.make(ProductGuide)
        response = api_client.delete(self.endpoint+f'{product_obj.id}/')
        assert response.status_code == 204

    def test_export(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        response = api_client.get(self.endpoint+'export_xlsx/')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/vnd.ms-excel'
        assert response.headers['content-disposition'] == f'attachment; filename="{datetime.date.today()}.xls"'

    def test_import(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        contact_obj = baker.make(ContactProvider)
        wb = Workbook()
        ws = wb.active
        header = ['id', 'str_by_order', 'article', 'name', 'price_rrc', 'price_buy', 'link', 'country',
                  'description', 'description_tech', 'description_add',	'recommendation', 'provider', 'nds',
                  'available']
        data = ['', 'string', 'string', 'string', 0, 0, 'string', 'string', 'string', 'string', 'string',
                'string', contact_obj.provider.id, 2147483647, 2147483647]
        ws.append(header)
        ws.append(data)
        wb.save('tests/guide/files/guide_product_import.xls')
        with open('tests/guide/files/guide_product_import.xls', 'rb') as f:
            response = api_client.post(self.endpoint+'import_xlsx/', data={'file': f})
        assert response.status_code == 200