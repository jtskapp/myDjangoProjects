# Generated by Django 2.0 on 2018-01-18 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_auto_20180118_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nic',
            name='ip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nicips', to='basic.IPPool'),
        ),
    ]
