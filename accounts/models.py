from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

# Create your models here.
class UserProfile(models.Model):
    bio=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to="media")  