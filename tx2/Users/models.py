from django.db import models
from tx2.Security.models import SecurityStates,Entity,SecurityPermissions
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class User(models.Model):
    UserEmail = models.CharField(max_length=500)
    UserPassword = models.CharField(max_length=500)
    UserBirthDate = models.DateField()
    UserFirstName = models.CharField(max_length=100)
    UserMiddleName = models.CharField(max_length=100)
    UserLastName = models.CharField(max_length=100)
    UserEntity = models.ForeignKey(Entity)
    State = models.ForeignKey(SecurityStates)
    UserGender = models.CharField(max_length=1)
    
    def __unicode__(self):
        return self.UserEmail
    
class GroupType(models.Model):
    GroupTypeName = models.CharField(max_length=50)
    GroupTypeDescription = models.CharField(max_length=500)
    
class Group(models.Model):
    GroupName = models.CharField(max_length=50)
    GroupDescription = models.CharField(max_length=500)
    GroupType = models.ForeignKey(GroupType)
    State = models.ForeignKey(SecurityStates)
    GroupEntity = models.ForeignKey(Entity)
    
class UserGroup(models.Model):
    User = models.ForeignKey(User)
    Group = models.ForeignKey(Group)
    State = models.ForeignKey(SecurityStates)
    
class Menu(models.Model):
    MenuName = models.CharField(max_length=100)
    MenuDesc = models.CharField(max_length=500)
    MenuUrl = models.CharField(max_length=500)
    MenuPid = models.IntegerField()
    State = models.ForeignKey(SecurityStates)
    MenuIcon = models.CharField(max_length=500)
    
    
class GroupMenu(models.Model):
    Menu = models.ForeignKey(Menu)
    Group = models.ForeignKey(Group)
    Active = models.IntegerField()
    
class UserLogs(models.Model):
    # user making changes
    LogsUser = models.ForeignKey(User)
    # row id being changed
    ContentType = models.ForeignKey(ContentType)
    LogsObject = models.IntegerField()
    LogsPermission = models.ForeignKey(SecurityPermissions)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.CharField(max_length=200)
    LogsPreviousState = models.CharField(max_length=5000)
    
class LoginType(models.Model):
    LoginTypeName = models.CharField(max_length=100)
    LoginTypeDesc = models.CharField(max_length=500)
    
class UserLoginLog(models.Model):
    user = models.ForeignKey(User)
    LoginTime = models.DateTimeField()
    Login_From = models.IntegerField()
    LogoutTime = models.DateTimeField()
    LoginIP = models.CharField(max_length=20)
    Logout_From = models.IntegerField()
