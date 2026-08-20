from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField( max_length=100)
    contact = models.CharField(max_length=12)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user} - {self.location}'
     