from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('Female', 'Female'),
    ('Male', 'Male')
)

SPORT = (
    ('Socer', 'Socer'),
    ('Badminton', 'Badminton'),
    ('Swimming', 'Swimming'),
    ('Running', 'Running')
)

# Create your models here.
class UserProfile(models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,choices=GENDER)


class Sport(models.Model):
    member = models.ManyToManyField(UserProfile)
    sport = models.CharField(max_length=100,choices=GENDER)
