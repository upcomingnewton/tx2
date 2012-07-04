from django.db import models

# Create your models here.
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
    ExtraAcadmicInfoId=models.ForeignKey(ExtraAcademicInfo)