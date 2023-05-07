from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    GENDER = (
        ("M","Male"),
        ("F", "Female"),
        ("O", "Other")
    )
    gender = models.CharField(max_length=1,choices=GENDER)
    

