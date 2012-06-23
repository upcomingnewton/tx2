from django.db import models
from django.contrib.contenttypes.models import ContentType
from tx2.UserReg.models import RegisterUser
from tx2.Users.models import User
from tx2.Security.models import SecurityStates,SecurityPermissions

# Create your models here.

class AppEventType(models.Model):
	EventTypeName = models.CharField(max_length=100)
	EventTypeDesc = models.CharField(max_length=500)
	
class AppEvent(models.Model):
	EventType = models.ForeignKey(AppEventType)
	EventName = models.CharField(max_length=100)
	EventDesc = models.TextField()
	EventStart = models.DateTimeField()
	EventDuration = models.IntegerField()
	EventRounds = models.IntegerField()
	EventRef = models.IntegerField()
	EventFolders = models.CharField(max_length=500)

class AppEventRound(models.Model):
	RoundName = models.CharField(max_length=100)
	RoundDesc = models.TextField()
	RoundStart = models.DateTimeField()
	RoundDuration = models.IntegerField()
	Event = models.ForeignKey(AppEvent)
	RoundRegUsers = models.ForeignKey(RegisterUser)
	
class AppEventLogs(models.Model):
    # user making changes
    LogsUser = models.ForeignKey(User)
    ContentType = models.ForeignKey(ContentType)
    # row id being changed
    LogsObject = models.IntegerField()
    LogsPermission = models.ForeignKey(SecurityPermissions)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.CharField(max_length=200)
	
