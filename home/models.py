from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    email = models.EmailField(unique=True, max_length=128)
    # Email attribute, which is a unique field

    pfp = models.ImageField(null=True, blank=True, default='/images/person.jpeg', upload_to="images/")
    # Media attribute, used to store multi-media files, profile pictures

    balance = models.DecimalField(max_digits=14, decimal_places=2, default=00.00)
    # Store user currency in decimal, perform mathematical and logical calculations
    

    def __str__(self):
    # Specify the string representation of an instance
        return self.email

