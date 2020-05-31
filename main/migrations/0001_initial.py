# Generated by Django 3.0.6 on 2020-05-31 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('one', 'GRADE ONE'), ('two', 'GRADE TWO'), ('three', 'GRADE TWO'), ('four', 'GRADE TWO'), ('five', 'GRADE TWO'), ('six', 'GRADE TWO')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nemis_no', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(default='kenya', max_length=100)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Others')], max_length=2)),
                ('religion', models.CharField(choices=[('atheists', 'Atheists'), ("baha'i", "Baha'i"), ('buddhism', 'Buddhism'), ('christianity', 'Christianity'), ('hinduism', 'Hinduism'), ('islam', 'Islam'), ('jainism', 'Jainism'), ('judaism', 'Judaism'), ('shintoism', 'Shintoism'), ('sikhism', 'Sikhism'), ('syncretic', 'Syncretic'), ('taoism', 'Taoism'), ('tradition', 'Tradition'), ('zoroastrianism', 'Zoroastrianism')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject_type', models.CharField(choices=[('ex', 'Extracurriculum'), ('su', 'Subject')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.IntegerField()),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('phone_no', models.IntegerField()),
                ('dob', models.DateField()),
                ('subjects', models.ManyToManyField(to='main.Subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]