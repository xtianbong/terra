from django.db import models
from django.forms import ModelForm

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=64,unique=True)
    max_temp=models.IntegerField()
    min_temp=models.IntegerField()
    max_hum=models.IntegerField()
    min_hum=models.IntegerField()
    fan_int=models.IntegerField()
    fan_dur=models.IntegerField()
    applied=models.BooleanField(default=False)

    def __str__(self):
        return self.name

