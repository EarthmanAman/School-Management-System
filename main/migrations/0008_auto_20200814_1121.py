# Generated by Django 3.0.6 on 2020-08-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200813_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='main.Subject'),
        ),
    ]