import random
import string

from django.contrib.auth.models import AbstractUser, User
from django.db import models

from modules.models import Language


def generate_random_password(length=12):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def get_random_profile_pic():
    profile_pics = [
        '/static/plushik_flower.png',
        '/static/plushik_knife.png'
    ]
    return random.choice(profile_pics)


class Profile(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    progress = models.FloatField(default=0)
    profile_pic_url = models.ImageField(upload_to='uploads/', default=get_random_profile_pic)
    learner_type = models.CharField(max_length=50, choices=[("A rookie! (Beginner)", "Beginner"),
                                                    ("A pookie! (Skilled)", "Skilled"),
                                                    ("A smart cookie! (Advanced)", "Advanced")],
                                                    default='An avid learner!')
    chosen_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    groups = models.ManyToManyField('auth.Group', related_name='profile_set')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='profile_set')

    def __str__(self):
        return self.email