from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)
    department = models.CharField(max_length=250)
    account_image = models.ImageField(default='default.png', 
                                      upload_to='account_images')


    def __str__(self) -> str:
        return f"{self.user.username}'s account"
