from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_support = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    def __str__(self) :
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='static/users/%Y/%m/%d/', default='static/default.png', blank=True, null= True)
    
    def __str__(self):
        return f'Profile for user {self.user.username}'