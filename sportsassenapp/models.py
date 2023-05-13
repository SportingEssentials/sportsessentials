from django.db import models

from django.db import models

class BasketballEssential(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='basketball_essentials')
    rating = models.IntegerField()
    coupons = models.CharField(max_length=200, blank=True)
    benefits = models.CharField(max_length=400, blank=True)
    stars = models.DecimalField(blank=True, max_digits=3, decimal_places=2)
    brand = models.CharField(max_length=200, blank=True)
    material = models.CharField(max_length=200, blank=True)

    def formatted_description(self):
        return self.description.replace('\n', '<br>')


    def __str__(self):
        return self.name
    
     
    
 

class SoccerEssential(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='soccer_essentials')
    rating = models.IntegerField()
    coupons = models.CharField(max_length=200)
    benefits = models.CharField(max_length=400)
    stars = models.IntegerField()
    brand = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    def __str__(self):
        return self.name

