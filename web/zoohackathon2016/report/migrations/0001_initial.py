# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('event_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('report_type', models.CharField(choices=[('A', 'Shop/Market'), ('B', 'Restaraunt/Eatery'), ('C', 'Live Animal Display'), ('D', 'Poaching'), ('E', 'Other')], max_length=2)),
                ('device_id', models.CharField(max_length=50)),
            ],
        ),
    ]
