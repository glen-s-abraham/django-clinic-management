# Generated by Django 3.2.6 on 2021-08-29 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210829_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='time',
            new_name='created_on',
        ),
    ]