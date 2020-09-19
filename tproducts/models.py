from django.db import models


class TProduct(models.Model):
    name =models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length = 255)
    stock = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='products/')
    contact = models.CharField(max_length=255, default=0)
