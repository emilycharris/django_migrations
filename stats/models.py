from django.db import models

# Create your models here.

class Player(models.Model):
    player_name = models.CharField(max_length=30)
    player_class = models.CharField(max_length=2)
    player_position = models.CharField(max_length=1)
    player_height = models.CharField(max_length=5)
    player_points = models.FloatField(max_length=5)
    player_rebounds = models.FloatField(max_length=5)
    player_assists = models.FloatField(max_length=5)

    def __str__(self):
        return self.player_name



