# Generated by Django 4.2.3 on 2023-07-13 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_rename_catogory_category'),
        ('experiences', '0002_alter_perk_details_alter_perk_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='categoryy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
    ]
