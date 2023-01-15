from django.db import models


class Specification(models.Model):
    project = models.OneToOneField('projects.Project', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    guide = models.BooleanField(default=False)


class Request(models.Model):
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    str_by_order = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=1023, null=True, blank=True)
    tx = models.TextField(blank=True, null=True)
    amount = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)
    

class Offer(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    product = models.ForeignKey('guide.ProductGuide', related_name='product', on_delete=models.SET_NULL, null=True)
    article = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=1023, null=True, blank=True)
    count = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)