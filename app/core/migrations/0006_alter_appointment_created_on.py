# Generated by Django 3.2.6 on 2021-08-29 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_time_appointment_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
