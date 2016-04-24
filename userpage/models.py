from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings



class Game1(models.Model):
    game_id = models.AutoField(primary_key=True, db_column='GAME_ID')  # Field name made lowercase.
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

class List1(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Surrogate key for django
    note = models.CharField(db_column='Note', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ownership = models.IntegerField(db_column='Ownership')  # Field name made lowercase.
    skill = models.CharField(db_column='Skill', max_length=20, blank=True, null=True)  # Field name made lowercase.
    game = models.ForeignKey(Game1, models.DO_NOTHING, db_column='GAME_ID')  # Field name made lowercase.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    class Meta:
        managed = False
        db_table = 'LIST'
        unique_together = (('game', 'user'),)

class Group1(models.Model):
    group_id = models.AutoField(db_column='GROUP_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=20)  # Field name made lowercase.
    is_public = models.IntegerField(db_column='Is_public')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    class Meta:
        managed = False
        db_table = 'GROUPS'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups:detail', kwargs={'pk': self.pk})

class UserGroup1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Surrogate key for django
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    group = models.ForeignKey(Group1, models.DO_NOTHING, db_column='GROUP_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERS_GROUPS'
        unique_together = (('user', 'group'),)
