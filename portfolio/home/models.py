from django.db import models

# Create your models here.
#to create a model we do that through class in python

class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phone = models.CharField(max_length=10)
  password = models.CharField(max_length=15)
  def __str__(self):
    return self.name + "--" + self.email
