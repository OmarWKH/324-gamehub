from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Game(models.Model):
    game_id = models.AutoField(primary_key=True, db_column='GAME_ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    poster = models.FileField(db_column='Poster', blank=True, null=True)  # Field name made lowercase.
    no_of_players = models.CharField(db_column='No_of_players', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    no_of_sessions = models.CharField(db_column='No_of_sessions', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_group = models.CharField(db_column='Age_group', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    competitve_level = models.CharField(db_column='Competitve_level', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
    	return self.name

    def __unicode__(self):
    	return self.name

    class Meta:
        managed = False
        db_table = 'GAME'


class BoardGame(models.Model):
    pieces = models.CharField(db_column='Pieces', max_length=20, blank=True, null=True)  # Field name made lowercase.
    game = models.ForeignKey('Game', models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.

    def __str__(self):
        return self.game.name

    def __unicode__(self):
        return self.game.name

    @classmethod
    def type(self):
        return self.__name__

    class Meta:
        managed = False
        db_table = 'BOARD_GAME'


class CardGame(models.Model):
#class CardGame(Game):
    cards_type = models.CharField(db_column='Cards_type', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    game = models.ForeignKey('Game', models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.
    #game_fk = models.OneToOneField('Game', models.DO_NOTHING, db_column='GAME_ID', primary_key=True, parent_link=True)  # Field name made lowercase.

    @classmethod
    def type(self):
        return self.__name__

    class Meta:
        managed = False
        db_table = 'CARD_GAME'


class PhysicalGame(models.Model):
    physical_requirements = models.TextField(db_column='Physical_requirements', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.

    @classmethod
    def type(self):
        return self.__name__

    class Meta:
        managed = False
        db_table = 'PHYSICAL_GAME'


class TabletopRpg(models.Model):
    narrative_authority = models.CharField(db_column='Narrative_authority', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    settings = models.TextField(db_column='Settings', blank=True, null=True)  # Field name made lowercase.
    style_of_play = models.CharField(db_column='Play_Style', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    components = models.CharField(db_column='Components', max_length=20, blank=True, null=True)  # Field name made lowercase.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.

    @classmethod
    def type(self):
        return self.__name__

    class Meta:
        managed = False
        db_table = 'TABLETOP_RPG'


class VideoGame(models.Model):
    system_requirements = models.TextField(db_column='System_requirements', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.

    @classmethod
    def type(self):
        return self.__name__

    class Meta:
        managed = False
        db_table = 'VIDEO_GAME'


class Platform(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Surrogate key for django
    os = models.CharField(db_column='OS', max_length=20)  # Field name made lowercase.
    game = models.ForeignKey('VideoGame', models.DO_NOTHING, db_column='GAME_ID')  # Field name made lowercase.

    @classmethod
    def type(self):
        return self.__name__

    class Meta:
        managed = False
        db_table = 'PLATFORM'
        unique_together = (('game', 'os'),)


class Type(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Surrogate key for django
    genre = models.CharField(db_column='Genre', max_length=20, blank=False)  # Field name made lowercase.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID')  # Field name made lowercase.

    @classmethod
    def type(self):
        return self.__name__

    class Meta:
        managed = False
        db_table = 'TYPE'
        unique_together = (('game', 'genre'),)


class List(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Surrogate key for django
    note = models.CharField(db_column='Note', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ownership = models.IntegerField(db_column='Ownership')  # Field name made lowercase.
    skill = models.CharField(db_column='Skill', max_length=20, blank=True, null=True)  # Field name made lowercase.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID')  # Field name made lowercase.
    # user = models.ForeignKey('', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @classmethod
    def type(self):
        return self.__name__

    class Meta:
        managed = False
        db_table = 'LIST'
        unique_together = (('game', 'user'),)
