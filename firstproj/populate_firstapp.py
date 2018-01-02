import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproj.settings')

#Setup Django
import django
django.setup()

## FAKE Database
import random
from firstapp.models import Topic,RecordAccess,WebPage
from faker import Faker

fake = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Forum', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):

    for entry in range(n):
        print("Populate Entry Number {}".format(entry))

        #get random topic for the entry
        top = add_topic()

        #create the fake data
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        #Create new WebPage entry
        webpage = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #Create new RecordAccess entry
        recordaccess = RecordAccess.objects.get_or_create(name=webpage,last_access=fake_date)[0]


if __name__ == '__main__':
    print("Start Populating Fake Data")
    populate(20)
    print("End Populating Fake Data")
