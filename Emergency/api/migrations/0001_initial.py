# Generated by Django 3.0.5 on 2021-05-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceEmergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(max_length=11)),
                ('complain', models.CharField(max_length=500)),
                ('date', models.DateField(max_length=12)),
            ],
        ),
    ]
