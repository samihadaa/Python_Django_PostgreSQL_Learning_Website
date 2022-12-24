from django.db import models
from django.urls import reverse
# Create your models here.

class Course(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=500)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.summary

  