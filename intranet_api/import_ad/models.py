from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class SilvaUser(User):
    """
    This class represents a user in the Silva database.
    Such user comes from Active Directory
    """

    # The user's phone number
    phone = models.CharField(max_length=50, null=True)
    # The user's mobile phone number
    mobile = models.CharField(max_length=50, null=True)
    # The user's site
    site = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = "Silva User"
        verbose_name_plural = "Silva Users"
