from django.db import models

class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100) 

    def __str__(self):
        return self.username

# models.py
from django.db import models
