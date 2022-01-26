from django.contrib.auth.models import Permission
from django.db import models

from users.models import User


class TimeStampedModel(models.Model):
    """
    Abstract Time Stamp Model for all Models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)


class Role(TimeStampedModel):
    """
    Each Role have a Multiple Permissions
    """
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return f"{self.name} - {self.permissions.count()}"


class Project(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_author')

    def __str__(self):
        return f"{self.name} - {self.creator.username}"


class ProjectUser(TimeStampedModel):
    """
    Each Project contain Multiple User
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'user',)

    def __str__(self):
        return f"{self.project.name} - {self.user.username} - {self.role.name}"


class ProviderCategory(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, help_text="CRM")


class Provider(TimeStampedModel):
    Source = 'Source'
    Target = 'Target'
    PROVIDER_TYPE = (
        (Source, 'Source'),
        (Target, 'Target'),
    )
    name = models.CharField(max_length=255, help_text="Accelo")
    category = models.ForeignKey(ProviderCategory, on_delete=models.CASCADE)
    connection_type = models.CharField(max_length=255, null=True, blank=True)
    default_ado_net_provider = models.CharField(max_length=255, help_text="System.Data.CData.API")
    integration_type = models.CharField(max_length=20, choices=PROVIDER_TYPE, default=Source)
    is_dialect = models.BooleanField(default=False)
    is_dialect_over_ado_net = models.BooleanField(default=False)
    is_dialect_over_odbc = models.BooleanField(default=False)
    logo_url = models.CharField(max_length=255, help_text="Accelo.apip")
    real_provider = models.CharField(max_length=255, help_text="Generic ADO.NET")
