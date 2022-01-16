from django.db import models

# Create your models here.
class Review(models.Model):
    objects = models.Manager()
    Name=models.CharField(max_length=20)
    Product_name=models.CharField(max_length=20)
    Review=models.CharField(max_length=100)
    Rating=models.IntegerField()
    Recommendation=models.CharField(max_length=3)

