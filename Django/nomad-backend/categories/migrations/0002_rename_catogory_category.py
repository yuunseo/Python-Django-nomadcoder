# Generated by Django 4.2.3 on 2023-07-13 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_alter_perk_details_alter_perk_explanation'),
        ('common', '0001_initial'),
        ('rooms', '0004_alter_amenity_options'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catogory',
            new_name='Category',
        ),
    ]
