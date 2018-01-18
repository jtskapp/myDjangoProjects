from django.contrib import admin
from django import forms
from basic.models import (Member,
        Order,
        Profile,
        Server,
        IPPool,
        Nic)


class NicAdmin(admin.ModelAdmin):
    readonly_fields = ('ip',)
    list_display =  ('server', 'model', 'slot', 'ip')
    fieldsets = (
        (None, {
            'fields': ('server', 'model', 'slot')
        }),
        ('Advanced options', {
            'fields': ('ip',)
        })
    )


class IPPoolAdmin(admin.ModelAdmin):
    list_display =  ('server', 'ip', 'in_used')
    fieldsets = (
        (None, {
            'fields': ('server', 'ip','in_used')
        }),
    )

# Register your models here.
admin.site.register(Member)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Server)
admin.site.register(IPPool,IPPoolAdmin)
admin.site.register(Nic,NicAdmin)
