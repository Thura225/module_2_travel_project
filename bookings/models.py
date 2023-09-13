from django.db import models
from buses.models import Bus
from django.contrib.auth.models import User

# Create your models here.
class Bookings(models.Model):
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    people = models.IntegerField()
    credit_card = models.CharField(max_length=20,default=None)
