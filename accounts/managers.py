from django.db import models
from django.db.models import Q
from django.contrib.auth.base_user import BaseUserManager

class CustomerManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="customer")




