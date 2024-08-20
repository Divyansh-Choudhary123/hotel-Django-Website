from django.db import models

# Create your models here.
class Abc (models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    
class Calander (models.Model):
    calander = models.CharField(max_length=50)
    # dropdown = models.CharField(max_length=50)