# Generated by Django 2.0 on 2018-01-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0009_auto_20180118_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nic',
            name='ip',
            field=models.GenericIPAddressField(blank=True, default='0.0.0.0', null=True),
        ),
    ]
