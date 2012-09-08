from django.db import models
from tx2.Security.models import SecurityStates,SecurityPermissions
from tx2.Users.models import User
from tx2.UserProfile.models import Branch
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class CompanyInfo(models.Model):
  CompanyName = models.CharField(max_length=1000, default="NULL")
  CompanyAdress = models.TextField(default="NULL")
  CompanyWebsite = models.CharField(max_length=1000, default="NULL")
  CompanyAbout = models.TextField(default="NULL")
  CompanyOtherDetails1 = models.TextField(default="NULL")
  CompanyOtherDetails2 = models.TextField(default="NULL")
  User = models.ForeignKey(User)
  
class Job(models.Model):
  Company = models.ForeignKey(CompanyInfo)
  Profile = models.CharField(max_length=1000, default="NULL")
  Designation = models.CharField(max_length=1000, default="NULL")
  Package = models.CharField(max_length=1000, default="NULL")
  DateOfVisit = models.DateField()
  JobDetails1 = models.TextField(default="NULL")
  JobDetails2 = models.TextField(default="NULL")
  RecruitmentRounds = models.CharField(max_length=1000, default="NULL")
  ContactPersonName = models.CharField(max_length=1000, default="NULL")
  ContactPersonMobile = models.CharField(max_length=20, default="NULL")
  ContactPersonEmail = models.CharField(max_length=1000, default="NULL")
  ContactPersonDetails = models.TextField(default="NULL")
  RegistrationsUpto = models.DateTimeField()
  State = models.ForeignKey(SecurityStates)

class JobType(models.Model):
  Name = models.CharField(max_length=1000, default="NULL")
  
class BranchJob(models.Model):
  Branch = models.ForeignKey(Branch)
  Job = models.ForeignKey(Job)
  JobType = models.ForeignKey(JobType)
  State = models.ForeignKey(SecurityStates)
  Comments1 = models.TextField(default="NULL")
  Comments2 = models.TextField(default="NULL")
  
class StudentsCredit(models.Model):
  User = models.ForeignKey(User)
  JobType = models.ForeignKey(JobType)
  Credit = models.IntegerField(default=0)
  
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
