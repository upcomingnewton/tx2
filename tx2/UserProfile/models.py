from django.db import models
from tx2.Users.models import User
from tx2.Security.models import SecurityStates,SecurityPermissions
from django.contrib.contenttypes.models import ContentType
from tx2.UserAdress.models import Adress

class DegreeType(models.Model): #pg, ug, etc
	Name=models.CharField(max_length=100)
	
class Degree(models.Model): #bsc, be etc etc
	Name=models.CharField(max_length=100)

class Board(models.Model): #pu, cbse etc etc
	Name=models.CharField(max_length=100)
	
class SessionType(models.Model):
	Name=models.CharField(max_length=100) #yearly , sem-wise, quarterly etc etc


class Marks(models.Model):
	SessionStart = models.DateField()
	SessionEnd = models.DateField()
	SessionNumber = models.IntegerField()
	SessionType = models.ForeignKey(SessionType) # we require  session type as forreign key, not which session it is ..
	TotalMarks = models.IntegerField()
	SecuredMarks = models.IntegerField() # model name and field name, better to use alt name for any conflicts
	TotalReappers = models.IntegerField()
	ReappersRemaining = models.IntegerField()
	DegreeType = models.ForeignKey(DegreeType)
	Board = models.ForeignKey(Board)
	Degree = models.ForeignKey(Degree)
	UserId = models.ForeignKey(User)
	State = models.ForeignKey(SecurityStates)

class ExtraAcademicInfoType(models.Model): # project, or work-exp
	Name=models.CharField(max_length=100)
	
class FunctionalAreaType(models.Model): # eg computers, mba etc etc
	FunctionalAreaTypeName = models.CharField(max_length=500)

class FunctionalAreaList(models.Model): # list of all functional areas, like c, c++, dot net in computers
	FunctionalAreaType = models.ForeignKey(FunctionalAreaType)
	FunctionalArea = models.CharField(max_length=100)

class ExtraAcademicInfoDetails(models.Model):
	User = models.ForeignKey(User)
	Title=models.CharField(max_length=500)
	Start=models.DateField()
	End=models.DateField()
	Organisation=models.CharField(max_length=500)
	Designation=models.CharField(max_length=500)
	Details=models.TextField()
	PlaceOfWork=models.ForeignKey(Adress) # this should be changed to adress id
	FunctionalArea = models.TextField() # this will contain the FunctionalAreaList's id  separated by some sep, (comma-sep values)
	ExtraAcadmicInfoType =models.ForeignKey(ExtraAcademicInfoType)
	State=models.ForeignKey(SecurityStates)
	References = models.TextField() # can be anything like manager's numberor something else
	Summary = models.TextField()
	
class Branch(models.Model):
	BranchName = models.CharField(max_length=100)
	
class Category(models.Model):
	CategoryName = models.CharField(max_length=100)
	
class StudentDetails(models.Model):
	User = models.ForeignKey(User)
	RollNo = models.CharField(max_length=20)
	BranchMajor = models.ForeignKey(Branch)
	BranchMinor = models.IntegerField()
	DegreePursuing = models.ForeignKey(Degree)
	Category = models.ForeignKey(Category)
	ComputerProficiency = models.CharField(max_length=500)
	State=models.ForeignKey(SecurityStates)
 	
class StudentSkills(models.Model):
	User = models.ForeignKey(User)
	FunctionalArea = models.TextField() # this will contain the FunctionalAreaList's id  separated by some sep, (comma-sep values)
	
class MedicalInfo(models.Model):
	User = models.ForeignKey(User)
	Height = models.CharField(max_length=100)
	Weight = models.CharField(max_length=100)
	LeftEye = models.CharField(max_length=100)
	RightEye = models.CharField(max_length=100)
	DisabilityInfo = models.TextField()
	
class LegalInfo(models.Model):
	AnyLegalIssue = models.CharField(max_length=1000)
	PassPortNo = models.CharField(max_length=25)
	
	
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

