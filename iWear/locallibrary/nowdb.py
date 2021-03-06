# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accessories(models.Model):
    accessoriesno = models.CharField(db_column='accessoriesNo', primary_key=True, max_length=8)  # Field name made lowercase.
    accessories = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'accessories'


class Action(models.Model):
    actionno = models.AutoField(db_column='actionNo', primary_key=True)  # Field name made lowercase.
    memno = models.IntegerField(db_column='memNo')  # Field name made lowercase.
    postno = models.IntegerField(db_column='postNo')  # Field name made lowercase.
    likes = models.BooleanField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'action'


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


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=12)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'user', 'group', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Clothes(models.Model):
    clothesno = models.CharField(db_column='clothesNo', primary_key=True, max_length=8)  # Field name made lowercase.
    clothes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'clothes'


class Coat(models.Model):
    coatno = models.CharField(db_column='coatNo', primary_key=True, max_length=8)  # Field name made lowercase.
    coat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'coat'


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


class Follow(models.Model):
    fono = models.AutoField(db_column='FoNo', primary_key=True)  # Field name made lowercase.
    memno = models.IntegerField(db_column='memNo')  # Field name made lowercase.
    memfono = models.IntegerField(db_column='memFoNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'follow'


class Friends(models.Model):
    frno = models.AutoField(db_column='FrNo', primary_key=True)  # Field name made lowercase.
    memno = models.ForeignKey('Meminform', models.DO_NOTHING, db_column='memNo')  # Field name made lowercase.
    memfrno = models.ForeignKey('Meminform', models.DO_NOTHING, db_column='memFrNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friends'


class Meminform(models.Model):
    account = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='account')
    name = models.CharField(max_length=12)
    gender = models.CharField(max_length=2, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    mempic = models.CharField(max_length=100, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memInform'


class Pants(models.Model):
    pantsno = models.CharField(db_column='pantsNo', primary_key=True, max_length=8)  # Field name made lowercase.
    pants = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pants'


class Post(models.Model):
    id = models.ForeignKey('self', models.DO_NOTHING, db_column='id', primary_key=True)
    account = models.CharField(max_length=8)
    photo = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)  # This field type is a guess.
    styleno = models.ForeignKey('Style', models.DO_NOTHING, db_column='styleNo', blank=True, null=True)  # Field name made lowercase.
    accessoriesno = models.ForeignKey(Accessories, models.DO_NOTHING, db_column='accessoriesNo', blank=True, null=True)  # Field name made lowercase.
    clothesno = models.ForeignKey(Clothes, models.DO_NOTHING, db_column='clothesNo', blank=True, null=True)  # Field name made lowercase.
    coatno = models.ForeignKey(Coat, models.DO_NOTHING, db_column='coatNo', blank=True, null=True)  # Field name made lowercase.
    pantsno = models.ForeignKey(Pants, models.DO_NOTHING, db_column='pantsNo', blank=True, null=True)  # Field name made lowercase.
    shoesno = models.ForeignKey('Shoes', models.DO_NOTHING, db_column='shoesNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'post'
        unique_together = (('id', 'id'),)


class Shoes(models.Model):
    shoesno = models.CharField(db_column='shoesNo', primary_key=True, max_length=8)  # Field name made lowercase.
    shoes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'shoes'


class Style(models.Model):
    styleno = models.CharField(db_column='styleNo', primary_key=True, max_length=8)  # Field name made lowercase.
    style = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'style'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
