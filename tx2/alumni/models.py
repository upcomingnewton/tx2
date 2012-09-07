from django.db import models
from tx2.Security.models import SecurityStates
from tx2.Users.models import User
from tx2.UserProfile.models import Branch
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class AlumniBaseProfile(models.Model):
  User = models.ForeignKey(User)
  Batch = models.IntegerField()
  Branch = models.ForeignKey(Branch)
  RollNo = models.CharField(max_length=10,default="NULL")
  State = models.ForeignKey(SecurityStates)
  
class JobsLogs(models.Model):
	# user making changes
	LogsUser = models.ForeignKey(User)
	# row id being changed
	ContentType = models.ForeignKey(ContentType)
	LogsObject = models.IntegerField(default=0)
	LogsPermission = models.ForeignKey(SecurityPermissions)
	LogsIP = models.CharField(max_length=20, default="NULL")
	LogsTimeStamp = models.DateTimeField()
	LogsDescription = models.CharField(max_length=200, default="NULL")
	LogsPreviousState = models.TextField(default="NULL")
