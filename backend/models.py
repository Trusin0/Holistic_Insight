# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import secrets 
import datetime
import pytz
from django.db import IntegrityError

tz = pytz.timezone('Asia/Shanghai')  # 东八区


class Aim(models.Model):
    aim_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    average_time = models.FloatField(blank=True, null=True)
    play_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aim'


class Chimpanzee(models.Model):
    chi_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    attempt_times = models.IntegerField(blank=True, null=True)
    play_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'chimpanzee'


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    play_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'color'


class Competition(models.Model):
    com_id = models.AutoField(primary_key=True)
    usr1 = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    usr2 = models.ForeignKey('Usr', models.DO_NOTHING, related_name='competition_usr2_set', blank=True, null=True)
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    winner = models.IntegerField(blank=True, null=True)
    play_time = models.DateField(blank=True, null=True)
    game1 = models.ForeignKey('Game', models.DO_NOTHING, blank=True, null=True)
    game2 = models.ForeignKey('Game', models.DO_NOTHING, related_name='competition_game2_set', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'competition'


class Friendlist(models.Model):
    friendlist_id = models.AutoField(primary_key=True)
    friend1 = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    friend2_id = models.IntegerField(blank=True, null=True)
    establish_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'friendlist'


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    test_type = models.CharField(max_length=20, blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'game'


class Number(models.Model):
    num_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    play_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'number'


class React(models.Model):
    react_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    react_time = models.FloatField(blank=True, null=True)
    play_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'react'


class Schulte(models.Model):
    schulte_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    block_size = models.IntegerField(blank=True, null=True)
    error_times = models.IntegerField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    play_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'schulte'


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    session_key = models.CharField(unique=True, max_length=64)
    expire_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'session'



class Sight(models.Model):
    sight_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    play_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sight'


class Usr(models.Model):
    usr_id = models.AutoField(primary_key=True)
    pass_field = models.CharField(db_column='pass', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    usr_name = models.CharField(max_length=20, blank=True, null=True)
    MBTI_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usr'

    def create_session(self):
        session = Session(usr=self)
        # 存在时区问题，后面再看看
        session.create_time = datetime.datetime.now(tz)
        session.expire_time = session.create_time + datetime.timedelta(days=1)
        session.session_key = secrets.token_hex(16)
        while True:
            try:
                session.save()
                break
            except IntegrityError:
                session.session_key = secrets.token_hex(16)

        return session.session_key
