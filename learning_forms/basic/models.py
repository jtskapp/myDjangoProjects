from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    country = models.CharField(
        'County of Origin',
        max_length=100,
        blank=False,
        default='Singapore',
        help_text='Enter Country Of Origin')
    city = models.CharField('City Name',
        max_length=100,
        blank=False,
        default='Singapore',
        help_text='Enter City'
        )

    def __str__(self):
        return '{}, {}'.format(self.user.username,self.country)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profiles.save()


class Server(models.Model):
    name = models.CharField(max_length=20,blank=True)
    data_center = models.CharField(max_length=100,blank=True)
    ip = models.GenericIPAddressField(default='0.0.0.0', null=True, blank=True)
    subnet = models.GenericIPAddressField(default='0.0.0.0', null=True, blank=True)
    gateway = models.GenericIPAddressField(default='0.0.0.0', null=True, blank=True)

    def __str__(self):
        return self.name

class IPPool(models.Model):
    server = models.ForeignKey(Server,on_delete=models.CASCADE, related_name='ips')
    ip = models.GenericIPAddressField(default='0.0.0.0', null=True, blank=True)
    in_used = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.ip


class Nic(models.Model):
    server = models.ForeignKey(Server,on_delete=models.CASCADE, related_name='nics')
    model = models.CharField(max_length=100,blank=True)
    slot = models.SmallIntegerField(blank=True,null=True)
    ip = models.GenericIPAddressField(default='0.0.0.0',
                null=True,
                blank=True)

    def __str__(self):
        return self.model


@receiver(post_save, sender=Nic)
def save_nic_setting(sender, instance, created, **kwargs):
    is_assigned = False
    if created:
        ip_list = IPPool.objects.filter(server=instance.server.id)
        for ippool in ip_list:
            print(ippool.ip)
            if not ippool.in_used:
                instance.ip = ippool.ip
                instance.save()
                ippool.in_used = True
                ippool.save()
                is_assigned = False
                break
