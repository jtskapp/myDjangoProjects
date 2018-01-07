from django.db import models
from django.contrib.auth.models import User

HIGHEST_EDUCATION = (('Primary', 'Primary'),
              ('Secondary', 'Secondary'),
              ('High School', 'High School'),
              ('Post Grad', 'Post Grad'),
              ('Poly', 'Poly'))

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=False)
    highest_education = models.CharField(max_length=100,choices=HIGHEST_EDUCATION, default='NA',blank=True)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
