from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


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
        return self.name

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
        return str(self.user)