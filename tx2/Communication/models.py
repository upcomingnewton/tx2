from django.db import models
from tx2.Security.models import SecurityStates,SecurityPermissions
from tx2.Users.models import User
from django.contrib.contenttypes.models import ContentType
from tx2.UserReg.models import RegisterUser

class CommunicationType(models.Model):
	CommName = models.CharField(max_length=100)
	CommDesc = models.TextField()
	
class Messages(models.Model):
	Title = models.CharField(max_length=100)
	Content = models.TextField()
	UsersReg = models.ForeignKey(RegisterUser)
	Comment = models.IntegerField()
	User = models.ForeignKey(User)
	Timestamp = models.DateTimeField()
	CommunicationType = models.ForeignKey(CommunicationType)
	State = models.ForeignKey(SecurityStates)
	RefContentType = models.IntegerField()
	Record = models.IntegerField()
	
class Comment(models.Model):
	ContentType = models.ForeignKey(ContentType)
	Record = models.IntegerField()
	User = models.ForeignKey(User)
	Timestamp = models.DateTimeField()
	State = models.ForeignKey(SecurityStates)
	Comment = models.TextField()
	
class CommunicationLogs(models.Model):
    # user making changes
    LogsUser = models.ForeignKey(User)
    
    ContentType = models.ForeignKey(ContentType)
    # row id being changed
    LogsObject = models.IntegerField()
    LogsPermission = models.ForeignKey(SecurityPermissions)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.TextField()
