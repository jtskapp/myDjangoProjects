from django.contrib import admin
from firstapp.models import Topic, WebPage, RecordAccess, User

# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(RecordAccess)
admin.site.register(User)
