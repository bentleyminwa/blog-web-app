from django.contrib.auth.models import AbstractUser
from django.db import models


# custom user model
class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'    # specifies name of the field on the user model to be used as unique identifier
    REQUIRED_FIELDS = ('username',)


    def __str__(self):
        return self.email 