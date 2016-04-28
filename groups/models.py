from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from gametest.models import Game

class Group(models.Model):
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
        return str(self.group_id)

    def __unicode__(self):
        return str(self.name)


    def get_absolute_url(self):
        return reverse('groups:detail', kwargs={'pk': self.pk})

class UserGroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Surrogate key for django
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)  # Field name made lowercase.
    group = models.ForeignKey(Group, models.DO_NOTHING, db_column='GROUP_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERS_GROUPS'
        unique_together = (('user', 'group'),)

    def __str__(self):
        return str(self.id)

class Instances(models.Model):
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    instance_location = models.CharField(db_column='INSTANCE_Location', max_length=20)  # Field name made lowercase.
    group = models.ForeignKey(Group, models.DO_NOTHING, db_column='GROUP_ID')  # Field name made lowercase.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID', blank=True, null=True)  # Field name made lowercase.
    instance = models.AutoField(db_column='INSTANCE_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INSTANCES'
        unique_together = (('group', 'instance'),)

    def __str__(self):
        return self.group.name + ' - ' + self.game.name + ' - ' + self.instance_location

    def get_absolute_url(self):
        return reverse('groups:InstanceDetails', kwargs={'instance_id': self.pk})

class Blogpost(models.Model):
    text = models.TextField(db_column='Text')  # Field name made lowercase.
    bp_time = models.DateTimeField(db_column='BP_Time')  # Field name made lowercase.
    is_public = models.IntegerField(db_column='Is_public')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    post_id = models.AutoField(db_column='POST_ID', primary_key=True)  # Field name made lowercase.
    group = models.ForeignKey('Group', related_name= 'group', db_column='GROUP_ID')  # Field name made lowercase.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BLOGPOST'
        unique_together = (('post_id', 'group', 'user'),)

    def __str__(self):
        return str(self.post_id) + ' - ' + self.group.name + ' - ' + str(self.user)

    def get_absolute_url(self):
        return reverse('groups:BlogpostDetails', kwargs={'bp_id': self.pk})