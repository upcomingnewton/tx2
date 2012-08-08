from django.db import models
from tx2.Users.models import Group
from tx2.Users.DBFunctions.DatabaseFunctions import DBGroupInsert
from tx2.Users.DBFunctions.Messages import decode
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_ENTITY,CACHE_KEY_SYSTEM_ENTITY
from tx2.Misc.CacheManagement import setCache,getCache
from tx2.Security.models import Entity
import logging

class GroupFnx(models.Model):
  def __init__(self):
    self.UserLogger = logging.getLogger(LoggerUser)
    self.ExceptionMessage = "Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon"
    self.CACHE_KEY_ALL_GROUPS = 'CACHE_KEY_ALL_GROUPS'
    
  def MakeExceptionMessage(self,msg):
    return 'Exception Generated : ' + str(msg) + ' Administrators have been alerted to rectify the error. We will send you a notification in this regard soon.'

        #CRUD FUNCTIONS
        
  def CreateGroup(self,gname,gdesc,gtype,entity,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    eid = entity
    if entity == -1:
      e_obj = getSystemEntity()
    try:
      details = {
                           'ip':ip,
                           'by':by,
                           'RequestedOperation':req_op,
                           'GroupEntity':eid,
                           'GroupType':gtype,
                           'GroupName':gname,
                           'GroupDescription':gdesc,
                           }
      result = DBGroupInsert(details)
      if (result['result'] == 1):
        return (1,'SUCESS. Group has been sucessfully added to database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('CreateGroup')
      return (-2,self.MakeExceptionMessage(str(ex)))


  # SELECTION AND QUERY FUNCTIONS
            
  def getGroupFromCache(self,name=-1,groupid = -1):
    GroupList = getCache(self.CACHE_KEY_ALL_GROUPS)
    try:
      if GroupList is not -1 and GroupList is not None:
        return (1,GroupList)
      else:
        return (-1,'ERROR in Retrieveing groups from cache')
    except Exception, ex:
      self.UserLogger.exception('getGroupFromCache')
      return (-2,self.MakeExceptionMessage(str(ex)))
            
  def ListAllGroups(self):
    try:
      grouplist  = self.getGroupFromCache()
      if grouplist is not 1:
        grouplist =  Group.objects.all()
        setCache(self.CACHE_KEY_ALL_GROUPS,grouplist)
      return (1,grouplist)
    except Exception, ex:
      self.UserLogger.exception('ListAllGroups')
      return (-2,self.MakeExceptionMessage(str(ex)))
        
  def getGroupObjectByName(self,name):
    try:
      grouplist  = self.ListAllGroups()
      if grouplist[0] is 1:
        for x in grouplist[1]:
          if x.GroupName == name:
            return (1,x)
        return (-1,'Group Does not exist.')
      else:
        return (-1,'Error retrieveing group list from database.')
    except Exception, ex:
      self.UserLogger.exception('getGroupObjectByName')
      return (-2,self.MakeExceptionMessage(str(ex)))

  def getGroupObjectById(self,groupid):
    try:
      grouplist  = self.ListAllGroups()
      if grouplist[0] is 1:
        for x in grouplist[1]:
          if x.id == groupid:
            return (1,x)
        return (-1,'Group Does not exist.')
      else:
        return (-1,'Error retrieveing group list from database.')
    except Exception, ex:
      self.UserLogger.exception('getGroupObjectById')
      return (-2,self.MakeExceptionMessage(str(ex)))
           
                    
