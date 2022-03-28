from django.db import models
from django.contrib.auth.models import AbstractUser

class bmiapi(models.Model):
    Gender =  models.CharField(max_length=256,unique=True)
    HeightCm = models.FloatField()  
    WeightKg =models.FloatField()
    #bmi = models.FloatField(null=True)
    
    
    def bmi(self):
        return self.WeightKg / self.HeightCm ** 2
