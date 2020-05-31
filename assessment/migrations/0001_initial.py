# Generated by Django 3.0.6 on 2020-05-31 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.FloatField()),
                ('assess', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assessment.Assess')),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Pupil')),
            ],
        ),
        migrations.CreateModel(
            name='AssessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('school_grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institution.SchoolGrade')),
            ],
        ),
        migrations.AddField(
            model_name='assess',
            name='assess_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assessment.AssessType'),
        ),
        migrations.AddField(
            model_name='assess',
            name='grade_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institution.GradeSubject'),
        ),
    ]