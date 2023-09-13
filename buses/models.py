from django.db import models
from datetime import date

POINT = (
    ('Yangon','Yangon'),
    ('Mandalay','Mandalay'),
    ('Taunggyi','Taunggyi'),
    ('Bagan','Bagan'),
    ('Mawlamyine','Mawlamyine')
)



# Create your models here.
class Bus(models.Model):
    name = models.CharField(max_length=20)
    start_point = models.CharField(max_length=20,choices=POINT)
    end_point = models.CharField(max_length=20,choices=POINT)
    price = models.IntegerField()
    deperture_date = models.DateField(default=date.today)