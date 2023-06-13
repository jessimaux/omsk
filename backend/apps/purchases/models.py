from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.specifications.models import Offer
from omsk.utils import prevent_recursion


class Purchase(models.Model):
    project = models.OneToOneField('projects.Project', on_delete=models.CASCADE)
    company_from = models.CharField(max_length=255, blank=True, null=True)
    project_inner_no = models.CharField(max_length=255, blank=True, null=True)
    project_registration_no = models.CharField(max_length=255, blank=True, null=True)
    bill = models.CharField(max_length=255, blank=True, null=True)

class PurchaseOffer(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='purchases', on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    price_buy = models.FloatField(default=0)
    nds_base = models.PositiveIntegerField(default=0)
    nds_sell = models.PositiveIntegerField(default=0)
    delivery_period = models.CharField(max_length=255, blank=True, null=True)
    prepayment = models.CharField(max_length=255, blank=True, null=True)
    bill_income = models.CharField(max_length=255, blank=True, null=True)
    bill_income_complete = models.CharField(max_length=255, blank=True, null=True)
    warehouse_delivery_date = models.CharField(max_length=255, blank=True, null=True)
    