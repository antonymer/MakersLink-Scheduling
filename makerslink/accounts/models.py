import logging
logger = logging.getLogger(__name__)

from django.core.validators import RegexValidator
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    # Field required to create user, used when creating users from teminal
    REQUIRED_FIELDS = ['slackId']
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    objects = UserManager()
    
    slackIdValid = RegexValidator(r'^((?!@).)*$', 'Ange ditt slacknamn utan @-tecken.', 
            code='invalid_slackId')
    
    email = models.EmailField(unique=True, verbose_name="E-post")
    slackId = models.CharField(max_length=100, verbose_name="Slacknamn", unique=True, blank=False, null=False, validators=[slackIdValid])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_registration_complete = models.BooleanField(default=False)

    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
