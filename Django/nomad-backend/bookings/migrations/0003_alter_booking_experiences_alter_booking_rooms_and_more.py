# Generated by Django 4.2.3 on 2023-07-14 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_alter_room_amenities_alter_room_categoryy_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0003_experience_categoryy'),
        ('bookings', '0002_alter_booking_experience_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='experiences',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='experiences.experience'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='rooms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]
