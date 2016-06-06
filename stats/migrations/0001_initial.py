# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=30)),
                ('player_class', models.CharField(max_length=2)),
                ('player_position', models.CharField(max_length=1)),
                ('player_height', models.CharField(max_length=5)),
                ('player_points', models.FloatField(max_length=5)),
                ('player_rebounds', models.FloatField(max_length=5)),
                ('player_assists', models.FloatField(max_length=5)),
            ],
        ),
    ]