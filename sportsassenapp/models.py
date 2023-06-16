from django.db import models

   
class Comparison(models.Model):
    comp_name = models.CharField(max_length=200, null=True)
    comp_url = models.URLField(max_length=200, null=True)
    comp_img = models.ImageField(upload_to='basketball_essentials', null=True)
    comp_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    comp_price_index = models.CharField(blank=True, max_length=100)

class BasketballEssential(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='basketball_essentials')
    coupons = models.CharField(max_length=200, blank=True)
    benefits = models.CharField(max_length=400, blank=True)
    stars = models.DecimalField(blank=True, max_digits=3, decimal_places=2)
    brand = models.CharField(max_length=200, blank=True)
    material = models.CharField(max_length=200, blank=True)
    url = models.URLField(max_length=200)
    sale = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=300, blank=True)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    comparison = models.ManyToManyField(Comparison, blank=True)
    
    



    def formatted_description(self):
        return self.description.replace('\n', '<br>')


    def __str__(self):
        return self.name
    
     
    #1
 

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

