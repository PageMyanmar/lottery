from django.db import models

# Create your models here.
class LotteryModel(models.Model):
    name = models.CharField(max_length=200)
    featured_image = models.ImageField()
    
    