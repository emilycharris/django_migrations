# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 17:44
from __future__ import unicode_literals

from django.db import migrations
from stats.models import Player

def add_data(stats, schema_editor):
    Player.objects.create(player_name="Grayson Allen", player_class="FR", player_position="G", player_height='6-4',
                          player_points=4.4, player_rebounds=1.0, player_assists=0.4),
    Player.objects.create(player_name="Quinn Cook", player_class="SR", player_position="G", player_height="6-2",
                          player_points=15.3, player_rebounds=3.4, player_assists=2.6),
    Player.objects.create(player_name="Amile Jefferson", player_class="JR", player_position="F", player_height="6-9",
                          player_points=6.1, player_rebounds=5.8, player_assists=0.8),
    Player.objects.create(player_name="Matt Jones", player_class="SO", player_position="G", player_height="6-5",
                          player_points=6.0, player_rebounds=2.3, player_assists=1.0),
    Player.objects.create(player_name="Tyus Jones", player_class="FR", player_position="G", player_height="6-1",
                          player_points=11.8, player_rebounds=3.5, player_assists=5.6),
    Player.objects.create(player_name="Sean Kelly", player_class="SR", player_position="G", player_height="6-3",
                          player_points=0, player_rebounds=0, player_assists=0.2),
    Player.objects.create(player_name="Semi Ojeleye", player_class="SO", player_position="F", player_height="6-8",
                          player_points=3.0, player_rebounds=2.3, player_assists=0.2),
    Player.objects.create(player_name="Jahlil Okafor", player_class="FR", player_position="C", player_height="6-11",
                          player_points=17.3, player_rebounds=8.5, player_assists=1.3),
    Player.objects.create(player_name="Nick Pagliuca", player_class="SO", player_position="G", player_height="6-3",
                          player_points=0.3, player_rebounds=0.4, player_assists=0.1),
    Player.objects.create(player_name="Marshall Plumlee", player_class="JR", player_position="C", player_height="7-0",
                          player_points=2.2, player_rebounds=2.4, player_assists=0.3),
    Player.objects.create(player_name="Rasheed Sulaimon", player_class="JR", player_position="G", player_height="6-5",
                          player_points=7.5, player_rebounds=2.0, player_assists=1.8),
    Player.objects.create(player_name="Justise Winslow", player_class="FR", player_position="F", player_height="6-6",
                          player_points=12.6, player_rebounds=6.5, player_assists=2.1)

class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
