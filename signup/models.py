from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='first_name', max_length=20)
    last_name = models.CharField(db_column='last_name', max_length=20)
    location = models.CharField(db_column='Location', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.EmailField(db_column='Email', max_length=20)  # Field name made lowercase.
    is_public = models.IntegerField(db_column='Is_public')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nickname = models.CharField(db_column='Nickname', max_length=20, unique=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    is_blocked = models.IntegerField(db_column='Is_blocked')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_admin = models.IntegerField(db_column='Is_Admin')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_moderator = models.IntegerField(db_column='Is_Moderator')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'USERS'