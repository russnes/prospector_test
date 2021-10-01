from django.db import models


# Create your models here.
class MyModel(models.Model):
    attr = models.CharField(max_length=255)
