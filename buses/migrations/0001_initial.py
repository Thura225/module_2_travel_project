# Generated by Django 4.2.4 on 2023-08-26 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start_point', models.CharField(choices=[('Yangon', 'Yangon'), ('Mandalay', 'Mandalay'), ('Taunggyi', 'Taunggyi'), ('Bagan', 'Bagan'), ('Mawlamyine', 'Mawlamyine')], max_length=20)),
                ('end_point', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('deperture_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]