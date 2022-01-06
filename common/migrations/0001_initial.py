# Generated by Django 3.2.10 on 2022-01-05 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('permissions', models.ManyToManyField(to='auth.Permission')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='common.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
    ]
