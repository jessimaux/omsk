from django.db import models

from apps.projects.models import Project
from apps.guide.models import ProductGuide


class Specification(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Request(models.Model):
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    str_by_order = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    tx = models.CharField(max_length=255, blank=True, null=True)
    amount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)


class Offer(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductGuide, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)