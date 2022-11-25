from django.contrib.auth.models import User
from django.db import models


class PartnerGuide(models.Model):
    name = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(default=0)
    contact_fio = models.CharField(max_length=255)
    contact_role = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)

    # log section
    created_by = models.ForeignKey(User, related_name="partner_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="partner_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProviderGuide(models.Model):
    sphere = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(default=0)
    contact_fio = models.CharField(max_length=255)
    contact_role = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)

    # log section
    created_by = models.ForeignKey(User, related_name="provider_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="provider_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductGuide(models.Model):
    str_by_order = models.CharField(max_length=255)
    article = models.CharField(max_length=255)
    name = models.CharField(max_length=1023)
    price_rrc = models.FloatField(default=0)
    price_buy = models.FloatField(default=0)
    link = models.URLField(max_length=255)
    country = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    description_tech = models.TextField(blank=True, null=True)
    description_add = models.TextField(blank=True, null=True)
    recommendation = models.CharField(max_length=1023)
    provider = models.ForeignKey(ProviderGuide, on_delete=models.CASCADE)
    nds = models.PositiveIntegerField(default=0)
    available = models.PositiveIntegerField(default=0)

    # log section
    created_by = models.ForeignKey(User, related_name="product_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="product_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class SpecificationGuide(models.Model):
    name = models.CharField(max_length=255)

    # log section
    created_by = models.ForeignKey(User, related_name="specification_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="specification_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RequestGuide(models.Model):
    specification = models.ForeignKey(SpecificationGuide, on_delete=models.CASCADE)
    str_by_order = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    tx = models.CharField(max_length=255, blank=True, null=True)
    amount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)

    # log section
    created_by = models.ForeignKey(User, related_name="request_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="request_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OfferGuide(models.Model):
    request = models.ForeignKey(RequestGuide, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductGuide, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)

    # log section
    created_by = models.ForeignKey(User, related_name="offer_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="offer_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)