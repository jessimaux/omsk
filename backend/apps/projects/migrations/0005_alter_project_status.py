# Generated by Django 4.1.2 on 2022-11-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_identify_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]
