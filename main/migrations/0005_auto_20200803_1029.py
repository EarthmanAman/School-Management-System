# Generated by Django 3.0.6 on 2020-08-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200803_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id_no',
            field=models.IntegerField(),
        ),
    ]