# Generated by Django 4.2.4 on 2023-08-29 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buses', '0003_alter_bus_end_point_alter_bus_start_point'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_people', models.IntegerField()),
                ('bus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='buses.bus')),
                ('buyer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]