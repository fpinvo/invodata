# Generated by Django 3.2.10 on 2022-01-06 08:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectuser',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='projectuser',
            unique_together={('project', 'user')},
        ),
    ]
