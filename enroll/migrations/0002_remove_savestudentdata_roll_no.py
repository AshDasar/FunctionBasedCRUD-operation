# Generated by Django 4.0.5 on 2022-09-18 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savestudentdata',
            name='roll_no',
        ),
    ]
