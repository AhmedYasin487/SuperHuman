from django.db import models
from django.contrib.auth.models import User,PermissionsMixin


class User(User,PermissionsMixin):

    def __str__(self):
        return self.name


# Create your models here.
