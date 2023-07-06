from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,  PermissionsMixin

class ExtensionData(models.Model):
    option_name = models.CharField()
    option_value = models.IntegerField()
    display_index = models.IntegerField()

class Payload(models.Model):
    product_id = models.IntegerField()
    category_code = models.CharField(max_length=255)
    provider_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    is_balloon = models.BooleanField()
    cost_markup_type = models.CharField(max_length=255)
    is_finance = models.BooleanField()
    extension_data = models.ManyToManyField(ExtensionData)