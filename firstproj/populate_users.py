import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproj.settings')

#Setup Django
import django
django.setup()


## FAKE Database
import random
from firstapp.models import User
from faker import Faker

fake = Faker()

def populateusers(n=5):
    for user in range(n):
        #create the fake data
        fake_firstname = fake.first_name()
        fake_lastname = fake.last_name()
        fake_email = fake.email()

        print("Populate User Number {}".format(user))
        u = User.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,email=fake_email)[0]


if __name__ == '__main__':
    print("Start Populating Fake Data")
    populateusers(50)
    print("End Populating Fake Data")
