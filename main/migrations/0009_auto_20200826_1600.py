# Generated by Django 3.0.6 on 2020-08-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200814_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
