from django.db import models

from apps.projects.models import Project
from apps.specifications.models import Offer


class Purchase(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    company_from = models.CharField(max_length=255)
    inner_registration_no = models.CharField(max_length=255)
    bill = models.CharField(max_length=255)

    # total section
    total_purchase = models.FloatField(default=0)
    total_rent_percentage = models.FloatField(default=0)
    total_rent_currency = models.FloatField(default=0)


class PurchaseOffer(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    nds = models.PositiveIntegerField(default=0)
    rent_percentage = models.FloatField(default=0)
    rent_currency = models.FloatField(default=0)
    delivery_period = models.DateField(default="2000-01-01")
    prepayment = models.BooleanField(default=False)
    bill_income = models.CharField(max_length=255)
    bill_income_complete = models.BooleanField(default=False)
    warehouse_income_date = models.DateField(default="2000-01-01")
