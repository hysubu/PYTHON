from django.db import models

# Create your models here.

class Data(models.Model):
    SrNo = models.IntegerField(default=False)
    Name = models.CharField(max_length=200)
    Gmail = models.EmailField(max_length=200)
    Age = models.IntegerField(max_length=100)
    Add = models.CharField(default=False)
