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
    accessories = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'accessories'


class Action(models.Model):
    actionno = models.AutoField(db_column='actionNo', primary_key=True)  # Field name made lowercase.
    id = models.ForeignKey('Meminform', models.DO_NOTHING, db_column='id')
    anotherid = models.CharField(max_length=12)
    postno = models.ForeignKey('Post', models.DO_NOTHING, db_column='postNo')  # Field name made lowercase.
    likes = models.BooleanField()
    message = models.CharField(max_length=100, blank=True, null=True)

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
    clothes = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'clothes'


class Coat(models.Model):
    coatno = models.CharField(db_column='coatNo', primary_key=True, max_length=8)  # Field name made lowercase.
    coat = models.CharField(max_length=8)

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
    userid = models.CharField(max_length=12, blank=True, null=True)
    memfoid = models.ForeignKey('Meminform', models.DO_NOTHING, db_column='memFoid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'follow'


class Friends(models.Model):
    frno = models.AutoField(db_column='FrNo', primary_key=True)  # Field name made lowercase.
    memno = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='memNo')  # Field name made lowercase.
    memfrno = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='memFrNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friends'


class Group(models.Model):
    groupno = models.CharField(db_column='groupNo', max_length=8)  # Field name made lowercase.
    group = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'group'


class Meminform(models.Model):
    id = models.AutoField()
    account = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='account')
    userid = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=12)
    gender = models.CharField(max_length=2)
    birth = models.DateField(blank=True, null=True)
    mempic = models.CharField(max_length=255, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memInform'


class Memgroup(models.Model):
    memgroupno = models.IntegerField(db_column='memgroupNo')  # Field name made lowercase.
    id = models.IntegerField()
    groupno = models.IntegerField(db_column='groupNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memgroup'


class Pants(models.Model):
    pantsno = models.CharField(db_column='pantsNo', primary_key=True, max_length=8)  # Field name made lowercase.
    pants = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'pants'


class Post(models.Model):
    account = models.IntegerField(blank=True, null=True)
    userid = models.ForeignKey(Meminform, models.DO_NOTHING, db_column='userid', blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField()
    word = models.CharField(max_length=255, blank=True, null=True)
    styleno = models.ForeignKey('Style', models.DO_NOTHING, db_column='styleNo', blank=True, null=True)  # Field name made lowercase.
    accessoriesno = models.ForeignKey(Accessories, models.DO_NOTHING, db_column='accessoriesNo', blank=True, null=True)  # Field name made lowercase.
    clothesno = models.ForeignKey(Clothes, models.DO_NOTHING, db_column='clothesNo', blank=True, null=True)  # Field name made lowercase.
    coatno = models.ForeignKey(Coat, models.DO_NOTHING, db_column='coatNo', blank=True, null=True)  # Field name made lowercase.
    pantsno = models.ForeignKey(Pants, models.DO_NOTHING, db_column='pantsNo', blank=True, null=True)  # Field name made lowercase.
    shoesno = models.ForeignKey('Shoes', models.DO_NOTHING, db_column='shoesNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'post'


class Postanalysisview(models.Model):
    id = models.IntegerField()
    account = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='account', blank=True, null=True)
    userid = models.CharField(max_length=12, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField()
    word = models.CharField(max_length=255, blank=True, null=True)
    styleno = models.ForeignKey('Style', models.DO_NOTHING, db_column='styleNo', blank=True, null=True)  # Field name made lowercase.
    accessoriesno = models.ForeignKey(Accessories, models.DO_NOTHING, db_column='accessoriesNo', blank=True, null=True)  # Field name made lowercase.
    clothesno = models.ForeignKey(Clothes, models.DO_NOTHING, db_column='clothesNo', blank=True, null=True)  # Field name made lowercase.
    coatno = models.ForeignKey(Coat, models.DO_NOTHING, db_column='coatNo', blank=True, null=True)  # Field name made lowercase.
    pantsno = models.ForeignKey(Pants, models.DO_NOTHING, db_column='pantsNo', blank=True, null=True)  # Field name made lowercase.
    shoesno = models.ForeignKey('Shoes', models.DO_NOTHING, db_column='shoesNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'postAnalysisView'


class Postcount(models.Model):
    postcountno = models.AutoField(db_column='postcountNo', primary_key=True)  # Field name made lowercase.
    postcount = models.IntegerField(db_column='postCount')  # Field name made lowercase.
    id = models.IntegerField()
    styleno = models.CharField(db_column='styleNo', max_length=8)  # Field name made lowercase.
    accessoriesno = models.CharField(db_column='accessoriesNo', max_length=8)  # Field name made lowercase.
    clothesno = models.CharField(db_column='clothesNo', max_length=8)  # Field name made lowercase.
    coatno = models.CharField(db_column='coatNo', max_length=8)  # Field name made lowercase.
    pantsno = models.CharField(db_column='pantsNo', max_length=8)  # Field name made lowercase.
    shoesno = models.CharField(db_column='shoesNo', max_length=8)  # Field name made lowercase.
    persent = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'postcount'


class Refollows(models.Model):
    refollowsno = models.IntegerField(db_column='refollowsNo')  # Field name made lowercase.
    id = models.IntegerField()
    anotherid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'refollows'


class Reposts(models.Model):
    repostsno = models.IntegerField(db_column='repostsNo')  # Field name made lowercase.
    id = models.IntegerField()
    postno = models.IntegerField(db_column='postNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reposts'


class Searchrecord(models.Model):
    searchrecordno = models.AutoField(db_column='searchrecordNo')  # Field name made lowercase.
    id = models.IntegerField()
    postno = models.IntegerField(db_column='postNo')  # Field name made lowercase.
    styleno = models.CharField(db_column='styleNo', max_length=8)  # Field name made lowercase.
    accessoriesno = models.CharField(db_column='accessoriesNo', max_length=8)  # Field name made lowercase.
    clothesno = models.CharField(db_column='clothesNo', max_length=8)  # Field name made lowercase.
    coatno = models.CharField(db_column='coatNo', max_length=8)  # Field name made lowercase.
    pantsno = models.CharField(db_column='pantsNo', max_length=8)  # Field name made lowercase.
    shoesno = models.CharField(db_column='shoesNo', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'searchrecord'


class Shoes(models.Model):
    shoesno = models.CharField(db_column='shoesNo', primary_key=True, max_length=8)  # Field name made lowercase.
    shoes = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'shoes'


class Style(models.Model):
    styleno = models.CharField(db_column='styleNo', primary_key=True, max_length=8)  # Field name made lowercase.
    style = models.CharField(max_length=8)

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


class Usersentencecount(models.Model):
    usersentencecountno = models.AutoField(db_column='usersentenceCountNo')  # Field name made lowercase.
    account = models.IntegerField(blank=True, null=True)
    usersentence = models.CharField(db_column='userSentence', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usersentencecount = models.IntegerField(db_column='userSentenceCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userSentenceCount'


class Websentence(models.Model):
    websentenceno = models.AutoField(db_column='websentenceNo')  # Field name made lowercase.
    web = models.CharField(max_length=100, blank=True, null=True)
    webtitle = models.CharField(max_length=100, blank=True, null=True)
    sentence = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'websentence'
