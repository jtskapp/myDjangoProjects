from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.topic_name

class WebPage(models.Model):
        topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
        name = models.CharField(max_length=200, unique=True)
        url = models.URLField(unique=True)

        def __str__(self):
            return self.name

class RecordAccess(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    last_access = models.DateField()

    def __str__(self):
        return str(self.last_access)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "{0}, {1}".format(self.first_name, self.last_name)
