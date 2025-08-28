from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    restaurantID = models.IntegerField()#음식점사업자등록번호
    #totalScore = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)


