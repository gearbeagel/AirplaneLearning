from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class LeeriApprentices(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    progress = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
