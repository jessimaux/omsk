import datetime
from typing import Callable

import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from django.contrib.auth.models import User
from apps.purchases.models import *


pytestmark = pytest.mark.django_db


class TestPurchase:
    endpoint = '/api/purchases/'

    def test_get_nonauth(self, api_client: APIClient):
        purchase_obj = baker.make(Purchase)
        response = api_client.get(self.endpoint+f'{purchase_obj.id}/export_xlsx/')
        assert response.status_code == 401

    def test_get_auth(self, auto_login_user: Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        purchase_obj = baker.make(Purchase)
        response = api_client.get(self.endpoint+f'{purchase_obj.id}/export_xlsx/')
        assert response.status_code == 200

    def test_put(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        purchaseoffer_obj = baker.make(PurchaseOffer)
        data = {
            "company_from": "Test",
            "project_inner_no": "Test",
            "project_registration_no": "Test",
            "bill": "Test",
            "purchases": [
                {
                    "id": purchaseoffer_obj.id,
                    "status": "Test",
                    "isbn": "Test",
                    "country": "Test",
                    "price_buy": 0,
                    "nds_base": 0,
                    "nds_sell": 0,
                    "delivery_period": "Test",
                    "prepayment": "Test",
                    "bill_income": "Test",
                    "bill_income_complete": "Test",
                    "warehouse_delivery_date": "Test"
                }
            ]
        }
        response = api_client.put(self.endpoint+f'{purchaseoffer_obj.purchase.id}/', data=data, format='json')
        assert response.status_code == 200

    def test_export(self, auto_login_user:  Callable[..., tuple[APIClient, User]]):
        api_client, user = auto_login_user()
        purchase_obj = baker.make(Purchase)
        response = api_client.get(self.endpoint+f'{purchase_obj.id}/export_xlsx/')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        assert response.headers['content-disposition'] == f'attachment; filename="{datetime.date.today()}.xlsx"'
