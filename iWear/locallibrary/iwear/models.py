# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User, Group, Permission


class Accessories(models.Model):
    accessoriesno = models.CharField(db_column='accessoriesNo', primary_key=True, max_length=8)  # Field name made lowercase.
    accessories = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.accessories

    class Meta:
        managed = False
        db_table = 'accessories'


class Action(models.Model):
    actionno = models.CharField(db_column='actionNo', primary_key=True, max_length=8)  # Field name made lowercase.
    memno = models.ForeignKey('Meminform', models.DO_NOTHING, db_column='memNo')  # Field name made lowercase.
    postno = models.ForeignKey('Post', models.DO_NOTHING, db_column='postNo')  # Field name made lowercase.
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
    last_login = models.DateTimeField(null=True, auto_now=True)
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'auth_user'


class Clothes(models.Model):
    clothesno = models.CharField(db_column='clothesNo', primary_key=True, max_length=8)  # Field name made lowercase.
    clothes = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.clothes

    class Meta:
        managed = False
        db_table = 'clothes'


class Coat(models.Model):
    coatno = models.CharField(db_column='coatNo', primary_key=True, max_length=8)  # Field name made lowercase.
    coat = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.coat

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
    userid = models.ForeignKey('Meminform', models.DO_NOTHING, related_name='follow_userid', db_column='userid')
    memfoid = models.ForeignKey('Meminform', models.DO_NOTHING, db_column='memFoid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'follow'


class Friends(models.Model):
    frno = models.AutoField(db_column='FrNo', primary_key=True)  # Field name made lowercase.
    memno = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='memNo', related_name='friend_user_id')  # Field name made lowercase.
    memfrno = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='memFrNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friends'


class Meminform(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='account')
    userid = models.CharField(primary_key=True, max_length=12)
    # password = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=12)  # This field type is a guess.
    male = 'M'
    female = 'F'
    GENDER_CHOICES = (
        (male, '男'),
        (female, '女'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=male)
    birth = models.DateField(blank=True, null=True)
    # mail = models.TextField(blank=True, null=True)  # This field type is a guess.
    mempic = models.ImageField(upload_to='mempics',blank=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.userid

    class Meta:
        managed = False
        db_table = 'memInform'


class Pants(models.Model):
    pantsno = models.CharField(db_column='pantsNo', primary_key=True, max_length=8)  # Field name made lowercase.
    pants = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.pants

    class Meta:
        managed = False
        db_table = 'pants'


class Post(models.Model):
    account = models.IntegerField(blank=True, null=True)
    # account = models.(AuthUser, models.DO_NOTHING, db_column='account')
    userid = models.CharField(max_length=12, blank=True, null=True)
    # userid = models.ForeignKey(Meminform, models.DO_NOTHING, db_column='userid', blank=True, null=True)
    time = models.DateTimeField(auto_now=True)
    word = models.TextField(blank=True, null=True)  # This field type is a guess.
    photo = models.ImageField(upload_to='photos',blank=True)
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
    account = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='account', blank=True, null=True)
    userid = models.CharField(max_length=12, blank=True, null=True)
    photo = models.ImageField(upload_to='photos',blank=True)
    time = models.DateTimeField()
    word = models.CharField(max_length=255, blank=True, null=True)
    styleno = models.ForeignKey('Style', models.DO_NOTHING, db_column='styleNo', blank=True, null=True)  # Field name made lowercase.
    accessoriesno = models.ForeignKey(Accessories, models.DO_NOTHING, db_column='accessoriesNo', blank=True, null=True)  # Field name made lowercase.
    clothesno = models.ForeignKey(Clothes, models.DO_NOTHING, db_column='clothesNo', blank=True, null=True)  # Field name made lowercase.
    coatno = models.ForeignKey(Coat, models.DO_NOTHING, db_column='coatNo', blank=True, null=True)  # Field name made lowercase.
    pantsno = models.ForeignKey(Pants, models.DO_NOTHING, db_column='pantsNo', blank=True, null=True)  # Field name made lowercase.
    shoesno = models.ForeignKey('Shoes', models.DO_NOTHING, db_column='shoesNo', blank=True, null=True)  # Field name made lowercase.
    ownaccount = models.IntegerField(db_column='ownAccount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'postAnalysisView'
    

class Shoes(models.Model):
    shoesno = models.CharField(db_column='shoesNo', primary_key=True, max_length=8)  # Field name made lowercase.
    shoes = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.shoes

    class Meta:
        managed = False
        db_table = 'shoes'


class Style(models.Model):
    styleno = models.CharField(db_column='styleNo', primary_key=True, max_length=8)  # Field name made lowercase.
    style = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.style

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


class Webandusersentenceanalysis(models.Model):
    websentenceno = models.IntegerField(db_column='webSentenceNo')  # Field name made lowercase.
    web = models.CharField(max_length=100, blank=True, null=True)
    webtitle = models.CharField(db_column='webTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sentence = models.CharField(max_length=100, blank=True, null=True)
    ownaccount = models.CharField(db_column='ownAccount', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'webAndUserSentenceAnalysis'
