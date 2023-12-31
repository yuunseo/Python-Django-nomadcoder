# Generated by Django 4.2.3 on 2023-07-13 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.commonmodel')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=250)),
                ('explanation', models.TextField()),
            ],
            bases=('common.commonmodel',),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.commonmodel')),
                ('country', models.CharField(default='한국', max_length=50)),
                ('name', models.CharField(default='', max_length=250)),
                ('city', models.CharField(default='서울', max_length=80)),
                ('address', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pekrs', models.ManyToManyField(to='experiences.perk')),
            ],
            bases=('common.commonmodel',),
        ),
    ]
