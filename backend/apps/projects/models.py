from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.guide.models import PartnerGuide
from apps.purchases.models import Purchase
from apps.specifications.models import Specification
from omsk.utils import prevent_recursion


class Project(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_inn = models.CharField(max_length=255, null=True, blank=True)
    company_city = models.CharField(max_length=255, null=True, blank=True)
    company_region = models.CharField(max_length=255, null=True, blank=True)
    company_children = models.PositiveIntegerField(default=0)
    partner = models.ForeignKey(PartnerGuide, on_delete=models.SET_NULL, null=True)
    reg_no = models.CharField(max_length=255, null=True, blank=True)
    nds = models.BooleanField(default=False)

    # general section
    commentary = models.TextField(blank=True, null=True)

    # in table editional
    delivery_date = models.DateField(default='2000-01-01')
    contract = models.BooleanField(default=False)

    # log section
    created_by = models.ForeignKey(User, related_name="project_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name="project_updated_by", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class File(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=1023)
    file = models.FileField(upload_to='media/')
    
# on project create send signal to create purchase on project
@receiver(post_save, sender=Project)
def create_purchase_and_specification(sender, instance, created, **kwargs):
    if created:
        Purchase.objects.create(project_id=instance.id)
