from django.db import models

class Posts(models.Model):
    name = models.CharField(max_length=500)
    post = models.CharField(max_length=1000)
    time = models.CharField(max_length=255)
