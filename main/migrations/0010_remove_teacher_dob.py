# Generated by Django 3.0.6 on 2020-08-26 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200826_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='dob',
        ),
    ]
