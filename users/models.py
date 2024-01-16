from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  # Add your custom fields if any
  is_seller = models.BooleanField(default=False)

  class Meta:
      # Add this to avoid clashes with the default 'auth' app's User model
      app_label = 'users'

CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'

class SellerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add seller-specific fields

class BuyerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add buyer-specific fields
