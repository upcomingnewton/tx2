from django.db import models
from tx2.Users.models import User
from tx2.Security.models import SecurityStates,SecurityPermissions
from django.contrib.contenttypes.models import ContentType

class DegreeType(models.Model):
	Name=models.CharField(max_length=100)
	level=models.IntegerField()

class Board(models.Model):
	Name=models.CharField(max_length=100)
	
class Degree(models.Model):
	Name=models.CharField(max_length=100)

class Session(models.Model):
	Name=models.CharField(max_length=100)


class Marks(models.Model):
	Start=models.DateField()
	End=models.DateField()
	SessionNo=models.ForeignKey(Session)
	SessionType=models.IntegerField()
	TotalMarks=models.IntegerField()
	Marks=models.IntegerField()
	TotalReappers=models.IntegerField()
	ReappersRemaining=models.IntegerField()
	DegreeType=models.ForeignKey(DegreeType)
	Board=models.ForeignKey(Board)
	Degree=models.ForeignKey(Degree)
	UserId=models.ForeignKey(User)
	State=models.ForeignKey(SecurityStates)

class ExtraAcademicInfo(models.Model):
	Name=models.CharField(max_length=100)

class ExtraAcademicInfoDetails(models.Model):
	Title=models.CharField(max_length=500)
	Start=models.DateField()
	End=models.DateField()
	Organisation=models.CharField(max_length=500)
	Role=models.CharField(max_length=500)
	Details=models.CharField(max_length=1000)
	Venue=models.CharField(max_length=1000)
	Duration_in_weeks=models.IntegerField()
	UserId=models.ForeignKey(User)
	ExtraAcadmicInfoId=models.ForeignKey(ExtraAcademicInfo)
	
class UserProfileLogs(models.Model):
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
# Create your models here.
