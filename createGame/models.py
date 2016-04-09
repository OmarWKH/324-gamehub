from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Game(models.Model):
    game_id = models.IntegerField(db_column='GAME_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    poster = models.TextField(db_column='Poster', blank=True, null=True)  # Field name made lowercase.
    no_of_players = models.CharField(db_column='No_of_players', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    no_of_sessions = models.CharField(db_column='No_of_sessions', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_group = models.CharField(db_column='Age_group', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    competitve_level = models.CharField(db_column='Competitve_level', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'GAME'
		
