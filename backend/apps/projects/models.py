from django.contrib.auth.models import User
from django.db import models

from apps.guide.models import PartnerGuide
# TODO: add core app, add files and images


class Project(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_inn = models.CharField(max_length=255)
    company_city = models.CharField(max_length=255)
    company_region = models.CharField(max_length=255)
    company_children = models.PositiveIntegerField(default=0)
    partner = models.ForeignKey(PartnerGuide, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=255)
    nds = models.BooleanField(default=False)

    # general section
    commentary = models.TextField(blank=True, null=True)

    # log section
    created_by = models.ForeignKey(User, related_name="project_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="project_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# TODO: Need to check with customer (in Project or not)
class RegistrationForm(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    diller_fio = models.CharField(max_length=255)
    diller = models.CharField(max_length=255)
    auction_price = models.FloatField(default=0)
    auction_date = models.DateField(default="2000-01-01")
    project_link = models.URLField(blank=True, null=True)
    announcement_date = models.DateField(default="2000-01-01")
    auction_no = models.PositiveIntegerField(default=0)
