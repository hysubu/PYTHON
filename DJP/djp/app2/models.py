from django.db import models

# Create your models here.
class Data2(models.Model):
    SrNo = models.IntegerField(default=False)
    Name = models.CharField(max_length=200)
    Gmail = models.EmailField(max_length=200)
    Age = models.IntegerField(default=False)
    Mark = models.IntegerField(default=False)
