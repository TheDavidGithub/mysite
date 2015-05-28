from django.db import models

# Create your models here.
class Car(models.Model):
    city = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    types = models.CharField(max_length=50)
    car_time = models.CharField(max_length=30)
    mileage = models.CharField(max_length=30)
    car_price = models.CharField(max_length=30)
    image_url = models.CharField(max_length=200)
    car_url = models.CharField(max_length=200)
    model = models.CharField(max_length=300)
    transmission_mode = models.CharField(max_length=50)
    have_accident = models.CharField(max_length=10)
