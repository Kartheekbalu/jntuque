from django.db import models
from datetime import datetime

# Create your models here.
class upload(models.Model):
    username=models.CharField(max_length=100,default='kk')
    pic=models.ImageField(upload_to='images/')
    subject=models.CharField(max_length=100,default='0')
    branch=models.CharField(max_length=10,default='0')
    regulation=models.CharField(max_length=5,default='R00')
    year=models.IntegerField(default=0000)
    date=models.DateTimeField(default=datetime.now)
