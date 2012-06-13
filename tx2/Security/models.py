from django.db import models
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class SecurityPermissions(models.Model):
    PermissionName = models.CharField(max_length=50)
    PermissionDescription = models.CharField(max_length=500)
    
class SecurityStates(models.Model):
    StateName  = models.CharField(max_length=50)
    StateDescription = models.CharField(max_length=500)

class SecurityGroupContent(models.Model):
    Group = models.IntegerField()
    ContentType = models.ForeignKey(ContentType)
    Permission = models.ForeignKey(SecurityPermissions)
    State = models.ForeignKey(SecurityStates)
    Active = models.IntegerField()
    
 
    
class SecurityLogs(models.Model):
    User = models.IntegerField()
    ContentType = models.ForeignKey(ContentType)
    TimeStamp = models.DateTimeField()
    ip = models.CharField(max_length=20)
    Record = models.IntegerField()
    Desc = models.CharField(max_length=1000)


class Entity(models.Model):
    """
        Entity represents all institutes / companies etc associated with the system.
        Like colleges col-1, col-2  etc  
        it also uses to classify users of a particular institute 
        like col1-student, col1-coordinator, col1-tpo etc etc
        EntityName = name of the entity
        EntityDescription = description 
        EntityState = Current state of the entity
    """
    EntityName = models.CharField(max_length=50)
    EntityDescription = models.CharField(max_length=500)
