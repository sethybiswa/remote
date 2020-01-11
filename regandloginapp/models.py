from django.db import models

# Create your models here.
class RegistrationData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField(max_length=8)
