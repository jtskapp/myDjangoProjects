# Generated by Django 2.0 on 2018-01-07 13:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('contact_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('quantity', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('size', models.CharField(blank=True, max_length=20)),
                ('color', models.CharField(blank=True, max_length=20)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='basic.Member')),
            ],
        ),
    ]
