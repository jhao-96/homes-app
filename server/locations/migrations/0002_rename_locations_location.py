# Generated by Django 5.0.6 on 2024-05-18 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Locations',
            new_name='Location',
        ),
    ]