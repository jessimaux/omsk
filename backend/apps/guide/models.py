from django.contrib.auth.models import User
from django.db import models


class PartnerGuide(models.Model):
    name = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(default=0)

    # log section
    created_by = models.ForeignKey(User, related_name="partner_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="partner_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContactPartner(models.Model):
    partner = models.ForeignKey(PartnerGuide, related_name='contact_partner', on_delete=models.CASCADE)
    fio = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    

class ProviderGuide(models.Model):
    sphere = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(default=0)

    # log section
    created_by = models.ForeignKey(User, related_name="provider_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="provider_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContactProvider(models.Model):
    provider = models.ForeignKey(ProviderGuide, related_name='contact_provider', on_delete=models.CASCADE)
    fio = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    

class ProductGuide(models.Model):
    str_by_order = models.CharField(max_length=255)
    article = models.CharField(max_length=255)
    name = models.CharField(max_length=1023)
    price_rrc = models.FloatField()
    price_buy = models.FloatField()
    link = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_tech = models.TextField(blank=True, null=True)
    description_add = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)
    provider = models.ForeignKey(ProviderGuide, on_delete=models.CASCADE)
    nds = models.PositiveIntegerField()
    available = models.PositiveIntegerField()

    # log section
    created_by = models.ForeignKey(User, related_name="product_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="product_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)