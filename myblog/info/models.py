from django.db import models
class Data (models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=225)


# Create your models here.
