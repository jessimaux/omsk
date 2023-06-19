import datetime
from typing import Callable

import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from django.contrib.auth.models import User
from apps.guide.models import PartnerGuide, ProductGuide
from apps.specifications.models import Offer
from apps.projects.models import Project


pytestmark = pytest.mark.django_db


class TestProjects:
    endpoint = '/api/projects/'

    def test_get_nonauth(self, api_client: APIClient):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    def test_get_auth(self, auto_login_user: Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    def test_post(self, auto_login_user: Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        partner_obj = baker.make(PartnerGuide)
        product_obj = baker.make(ProductGuide)
        data = {
            'name': 'Test',
            'status': 'Test',
            'partner_id': partner_obj.id,
            'company_name': 'Test',
            'company_inn': 'Test',
            'company_city': 'Test',
            'company_region': 'Test',
            'company_children': 0,
            'reg_no': 'Test',
            'nds': True,
            'commentary': 'Test',
            'delivery_date': '1995-01-01',
            'contract': False,
            'specification': {
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
        }
        response = api_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 201

    def test_put(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        partner_obj = baker.make(PartnerGuide)
        project_obj = baker.make(Project, partner_id=partner_obj.id)
        offer_obj = baker.make(Offer, request__specification__project_id=project_obj.id)
        data = {
            'name': 'Test',
            'status': 'Test',
            'partner_id': project_obj.partner.id,
            'company_name': 'Test',
            'company_inn': 'Test',
            'company_city': 'Test',
            'company_region': 'Test',
            'company_children': 0,
            'reg_no': 'Test',
            'nds': True,
            'commentary': 'Test',
            'delivery_date': '1995-01-01',
            'contract': False,
            'specification': {
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
        }
        response = api_client.put(
            self.endpoint+f'{offer_obj.request.specification.project.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_delete(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        project_obj = baker.make(Project)
        response = api_client.delete(self.endpoint+f'{project_obj.id}/')
        assert response.status_code == 204

    def test_report_registration(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        partner_obj = baker.make(PartnerGuide)
        project_obj = baker.make(Project, partner_id=partner_obj.id)
        offer_obj = baker.make(Offer, request__specification__project_id=project_obj.id)
        response = api_client.get(self.endpoint+f'{project_obj.id}/report_registration/')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        assert response.headers['content-disposition'] == f'attachment; filename="{datetime.date.today()}.xlsx"'
