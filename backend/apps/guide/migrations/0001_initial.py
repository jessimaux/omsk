# Generated by Django 4.1.2 on 2022-10-28 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecificationGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specification_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specification_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_by_order', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('tx', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('total', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_created_by', to=settings.AUTH_USER_MODEL)),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.specificationguide')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProviderGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sphere', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('inn', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('contact_fio', models.CharField(max_length=255)),
                ('contact_role', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='provider_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='provider_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_by_order', models.CharField(max_length=255)),
                ('article', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=1023)),
                ('price_rrc', models.FloatField(default=0)),
                ('price_buy', models.FloatField(default=0)),
                ('link', models.URLField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_tech', models.TextField(blank=True, null=True)),
                ('description_add', models.TextField(blank=True, null=True)),
                ('recommendation', models.CharField(max_length=1023)),
                ('provider', models.CharField(max_length=255)),
                ('nds', models.PositiveIntegerField(default=0)),
                ('available', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('inn', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('contact_fio', models.CharField(max_length=255)),
                ('contact_role', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partner_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partner_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OfferGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('total', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offer_created_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.productguide')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.requestguide')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offer_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
