from django.contrib.auth.models import Permission
from django.db import models
from django.contrib.auth.models import (AbstractUser)
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone_number = PhoneNumberField()
    country = CountryField()
    company_name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('username', 'email',)

    def __str__(self):
        return self.email
