from django.db import models

class Students(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  age = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  religion = models.CharField(max_length=255)
  contact = models.CharField(max_length=255)
  
