from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50,blank=False,unique=True)
    email_address = models.EmailField(blank=False,unique=True)
    nickname = models.CharField(max_length=20,blank=False,unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    def __str__(self):
        return "{}, {}".format(self.name,self.nickname)

class Order(models.Model):
    member = models.ForeignKey(Member,related_name="members",on_delete=models.CASCADE)
    description = models.CharField(max_length=200,blank=False)
    url = models.URLField(blank=False)
    quantity = models.IntegerField(
                default=1,
                validators=[MaxValueValidator(100), MinValueValidator(1)]
                )
    size = models.CharField(max_length=20,blank=True)
    color = models.CharField(max_length=20,blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def price(self):
        return "$%s" % self.price

    def __str__(self):
        return "{}, {}".format(self.description,self.member.name)
