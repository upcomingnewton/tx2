from django.db import models
from tx2.Users.models import User
from tx2.Security.models import SecurityStates,SecurityPermissions
from django.contrib.contenttypes.models import ContentType

class City(models.Model):
	CityName = models.CharField(max_length=500)
	
class State(models.Model):
	StateName = models.CharField(max_length=500)
	
class Country(models.Model):
	CountryName = models.CharField(max_length=500)

class Adress(models.Model):
	AdressNo = models.CharField(max_length=50)
	StreetAdress1 = models.CharField(max_length=500)
	StreetAdress2 = models.CharField(max_length=500)
	City = models.ForeignKey(City)
	State = models.ForeignKey(State)
	Country = models.ForeignKey(Country)
	PinCode = models.CharField(max_length=15)

class UserContactInfo(models.Model):
	User = models.ForeignKey(User)
	MobileNo = models.CharField(max_length=20)
	AltEmail = models.CharField(max_length=500)
	FatherName = models.CharField(max_length=310) #fname, mname, lname = 100 chars each, rest use as sep
	FatherContactNo = models.CharField(max_length=20)
	MotherName = models.CharField(max_length=310)#fname, mname, lname = 100 chars each, rest use as sep
	MotherContactNo = models.CharField(max_length=20)
	ParmanentAdress = models.IntegerField()
	PresentAdress = models.IntegerField()

class UserAdressLogs(models.Model):
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
