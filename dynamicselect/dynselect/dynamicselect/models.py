from django.db import models

# Create your models here.
class Continent(models.Model):
 name = models.CharField(max_length=255)

 def __str__(self):
  return self.name

class Country(models.Model):
 continent = models.ForeignKey(Continent,on_delete=models.CASCADE,related_name='country')
 name = models.CharField(max_length=255)

 def __str__(self):
  return self.name

class Location(models.Model):
 continent = models.ForeignKey(Continent,on_delete=models.CASCADE,related_name='location')
 country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='location')
 city = models.CharField(max_length=50)
 street = models.CharField(max_length=100)

 def __str__(self):
  return self.city
