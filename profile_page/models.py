from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email