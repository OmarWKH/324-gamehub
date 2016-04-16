# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(db_column='GAME_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('poster', models.FileField(blank=True, db_column='Poster', null=True, upload_to=b'')),
                ('no_of_players', models.CharField(blank=True, db_column='No_of_players', max_length=20, null=True)),
                ('duration', models.IntegerField(blank=True, db_column='Duration', null=True)),
                ('no_of_sessions', models.CharField(blank=True, db_column='No_of_sessions', max_length=20, null=True)),
                ('age_group', models.CharField(blank=True, db_column='Age_group', max_length=20, null=True)),
                ('competitve_level', models.CharField(blank=True, db_column='Competitve_level', max_length=20, null=True)),
            ],
            options={
                'db_table': 'GAME',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('os', models.CharField(db_column='OS', max_length=20)),
            ],
            options={
                'db_table': 'PLATFORM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('genre', models.CharField(db_column='Genre', max_length=20)),
            ],
            options={
                'db_table': 'TYPE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BoardGame',
            fields=[
                ('pieces', models.CharField(blank=True, db_column='Pieces', max_length=20, null=True)),
                ('game', models.ForeignKey(db_column='GAME_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='gametest.Game')),
            ],
            options={
                'db_table': 'BOARD_GAME',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CardGame',
            fields=[
                ('cards_type', models.CharField(blank=True, db_column='Cards_type', max_length=20, null=True)),
                ('game_fk', models.OneToOneField(db_column='GAME_ID', on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, primary_key=True, serialize=False, to='gametest.Game')),
            ],
            options={
                'db_table': 'CARD_GAME',
                'managed': False,
            },
            bases=('gametest.game',),
        ),
        migrations.CreateModel(
            name='PhysicalGame',
            fields=[
                ('physical_requirements', models.TextField(blank=True, db_column='Physical_requirements', null=True)),
                ('game', models.ForeignKey(db_column='GAME_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='gametest.Game')),
            ],
            options={
                'db_table': 'PHYSICAL_GAME',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TabletopRpg',
            fields=[
                ('narrative_authority', models.CharField(blank=True, db_column='Narrative_authority', max_length=20, null=True)),
                ('settings', models.TextField(blank=True, db_column='Settings', null=True)),
                ('style_of_play', models.CharField(blank=True, db_column='Play_Style', max_length=20, null=True)),
                ('components', models.CharField(blank=True, db_column='Components', max_length=20, null=True)),
                ('game', models.ForeignKey(db_column='GAME_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='gametest.Game')),
            ],
            options={
                'db_table': 'TABLETOP_RPG',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('system_requirements', models.TextField(blank=True, db_column='System_requirements', null=True)),
                ('game', models.ForeignKey(db_column='GAME_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='gametest.Game')),
            ],
            options={
                'db_table': 'VIDEO_GAME',
                'managed': False,
            },
        ),
    ]