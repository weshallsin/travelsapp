# Generated by Django 2.0.2 on 2018-03-21 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180321_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extra',
            name='alt_mob',
        ),
    ]
