from __future__ import unicode_literals

from django.db import models


class Blogpost(models.Model):
    text = models.TextField(db_column='Text')  # Field name made lowercase.
    bp_time = models.DateTimeField(db_column='BP_Time')  # Field name made lowercase.
    is_public = models.IntegerField(db_column='Is public')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    post_id = models.IntegerField(db_column='POST_ID')  # Field name made lowercase.
    group = models.ForeignKey('Group', related_name= 'group', db_column='GROUP_ID')  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BLOGPOST'
        unique_together = (('post_id', 'group', 'user'),)


class BoardGame(models.Model):
    pieces = models.CharField(db_column='Pieces', max_length=20, blank=True, null=True)  # Field name made lowercase.
    game = models.ForeignKey('Game', models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOARD GAME'


class CardGame(models.Model):
    cards_type = models.CharField(db_column='Cards type', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    game = models.ForeignKey('Game', models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARD GAME'


class ChatChannel(models.Model):
    cc_name = models.CharField(db_column='CC_Name', max_length=20)  # Field name made lowercase.
    group = models.ForeignKey('Group', models.DO_NOTHING, db_column='GROUP_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHAT_CHANNEL'
        unique_together = (('cc_name', 'group'),)


class ChatMessage(models.Model):
    text = models.TextField(db_column='Text')  # Field name made lowercase.
    cm_time = models.DateTimeField(db_column='CM_Time')  # Field name made lowercase.
    cm_id = models.IntegerField(db_column='CM_ID')  # Field name made lowercase.
    user = models.ForeignKey('User', related_name='user', db_column='USER_ID')  # Field name made lowercase.
    cc_name = models.ForeignKey(ChatChannel, related_name='chat_cc_name', db_column='CC_Name')  # Field name made lowercase.
    group = models.ForeignKey(ChatChannel, related_name='chat_group', db_column='GROUP_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHAT_MESSAGE'
        unique_together = (('cm_id', 'user', 'cc_name', 'group'),)


class Comments(models.Model):
    text = models.TextField(db_column='Text')  # Field name made lowercase.
    c_time = models.DateTimeField(db_column='C_Time')  # Field name made lowercase.
    c_id = models.IntegerField(db_column='C_ID')  # Field name made lowercase.
    commentor = models.ForeignKey('User', models.DO_NOTHING, db_column='COMMENTOR_ID')  # Field name made lowercase.
    post = models.ForeignKey(Blogpost, related_name='comment_post', db_column='POST_ID')  # Field name made lowercase.
    group = models.ForeignKey(Blogpost, related_name='comment_group', db_column='GROUP_ID')  # Field name made lowercase.
    post_writer = models.ForeignKey(Blogpost, related_name='comment_post_writer', db_column='POST_WRITER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMMENTS'
        unique_together = (('c_id', 'commentor', 'post', 'group', 'post_writer'),)


class Game(models.Model):
    game_id = models.IntegerField(db_column='GAME_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    poster = models.TextField(db_column='Poster', blank=True, null=True)  # Field name made lowercase.
    no_of_players = models.CharField(db_column='No of players', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    no_of_sessions = models.CharField(db_column='No of sessions', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_group = models.CharField(db_column='Age group', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    competitve_level = models.CharField(db_column='Competitve level', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'GAME'


class Group(models.Model):
    group_id = models.IntegerField(db_column='GROUP_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=20)  # Field name made lowercase.
    is_public = models.IntegerField(db_column='Is public')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    max_no_of_users = models.BigIntegerField(db_column='Max No of user', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GROUPS'


class Instances(models.Model):
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    instance_location = models.CharField(db_column='INSTANCE_Location', max_length=20)  # Field name made lowercase.
    group = models.ForeignKey(Group, models.DO_NOTHING, db_column='GROUP_ID')  # Field name made lowercase.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID', blank=True, null=True)  # Field name made lowercase.
    instance = models.ForeignKey(Group, related_name='instances_instance', db_column='INSTANCE_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INSTANCES'
        unique_together = (('group', 'instance'),)


class List(models.Model):
    note = models.CharField(db_column='Note', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ownership = models.IntegerField(db_column='Ownership')  # Field name made lowercase.
    skill = models.CharField(db_column='Skill', max_length=20, blank=True, null=True)  # Field name made lowercase.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID')  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LIST'
        unique_together = (('game', 'user'),)


class PhysicalGame(models.Model):
    physical_requirements = models.TextField(db_column='Physical requirements', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PHYSICAL GAME'


class Platform(models.Model):
    os = models.CharField(db_column='OS', max_length=20)  # Field name made lowercase.
    game = models.ForeignKey('VideoGame', models.DO_NOTHING, db_column='GAME_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLATFORM'
        unique_together = (('game', 'os'),)


class Report(models.Model):
    report_id = models.IntegerField(db_column='REPORT_ID')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    reporter = models.ForeignKey('User', related_name='reports_reporter', db_column='REPORTER_ID')  # Field name made lowercase.
    reported = models.ForeignKey('User', related_name='reported', db_column='REPORTED_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REPORTS'
        unique_together = (('report_id', 'reporter', 'reported'),)


class TabletopRpg(models.Model):
    narritive_authority = models.CharField(db_column='Narritive authority', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    settings = models.TextField(db_column='Settings', blank=True, null=True)  # Field name made lowercase.
    style_of_play = models.CharField(db_column='Style of play', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    components = models.CharField(db_column='Components', max_length=20, blank=True, null=True)  # Field name made lowercase.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TABLETOP RPG'


class Tag(models.Model):
    tag = models.CharField(db_column='TAG', max_length=20)  # Field name made lowercase.
    post = models.ForeignKey(Blogpost, related_name='tag_post', db_column='POST_ID')  # Field name made lowercase.
    group = models.ForeignKey(Blogpost, related_name='tag_group', db_column='GROUP_ID')  # Field name made lowercase.
    user = models.ForeignKey(Blogpost, related_name='tag_user', db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAG'
        unique_together = (('post', 'group', 'user'),)


class Type(models.Model):
    genre = models.CharField(db_column='Genre', max_length=20)  # Field name made lowercase.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TYPE'
        unique_together = (('game', 'genre'),)


class User(models.Model):
    user_id = models.IntegerField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.EmailField(db_column='Email', max_length=20)  # Field name made lowercase.
    is_public = models.IntegerField(db_column='Is public')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nickname = models.CharField(db_column='Nickname', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    is_blocked = models.IntegerField(db_column='Is blocked')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_admin = models.IntegerField(db_column='Is Admin')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_moderator = models.IntegerField(db_column='Is Moderator')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'USERS'


class UserGroup(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    group = models.ForeignKey(Group, models.DO_NOTHING, db_column='GROUP_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERS_GROUPS'
        unique_together = (('user', 'group'),)


class VideoGame(models.Model):
    system_requirements = models.TextField(db_column='System requirements', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    game = models.ForeignKey(Game, models.DO_NOTHING, db_column='GAME_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VIDEO GAME'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroup(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'