from django.contrib.auth.models import AbstractUser
from django.db import models

class LeeriApprentices(AbstractUser):
    progress = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='leeriapprentices_groups',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='leeriapprentices_permissions',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email
