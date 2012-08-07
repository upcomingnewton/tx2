from django.db import models
from tx2.Users.models import Group
from tx2.Users.DBFunctions.DatabaseFunctions import DBGroupInsert
from tx2.Users.DBFunctions.Messages import decode
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
      e_obj = Entity.objects.get(EntityName=SYSTEM_ENTITY)
      if  e_obj is None:
        self.UserLogger.exception('[%s] Entity Object is null' % ('CreateGroup'))
        return (-1,self.ExceptionMessage)
      else:
        setCache(CACHE_KEY_SYSTEM_ENTITY,e_obj.id)
        eid = e_obj.id
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
      return (1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('CreateGroup')
      return (-2,self.MakeExceptionMessage(str(ex)))


  # SELECTION AND QUERY FUNCTIONS
            
  def getGroupFromCache(self,name=-1,groupid = -1):
    GroupList = getCache(self.CACHE_KEY_ALL_GROUPS)
    if GroupList is not -1:
      if name == -1 and groupid == -1:
        return GroupList
      elif name is not -1 and groupid == -1:
        # find group with name
        for x in GroupList:
          if x.GroupName == name:
            return x
        return -1
      elif id is not -1 and name == -1:
        # find group with id
        for x in GroupList:
          if x.id == id:
            return x
        return -1
      elif name is not -1 and groupid is not -1:
        # find group with name and id
        for x in GroupList:
          if x.id == id and x.GroupName == name:
            return x
        return -1
    else:
      return -1
            
  def ListAllGroups(self):
    try:
      grouplist  = self.getGroupFromCache()
      if grouplist is -1:
        grouplist =  Group.objects.all()
        setCache(self.CACHE_KEY_ALL_GROUPS,grouplist)
      return (1,grouplist)
    except:
      exception_log = ('[%s]')%('ListAllGroups')
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)
        
  def getGroupObjectByName(self,name):
    try:
      groupobj  = self.getGroupFromCache(name,-1)
      if groupobj is -1:
        groupobj = Group.objects.get(GroupName=name)
      if groupobj is None:
        return (-1,None)
      else:
        return (1,groupobj)
    except:
      exception_log = ('[%s] name passed = %s')%('getGroupByName',name)
      self.UserLogger.exception(exception_log)
      return (-2,[])

  def getGroupObjectById(self,groupid):
    try:
      groupobj  = self.getGroupFromCache(-1,groupid)
      if groupobj is -1:
        groupobj = Group.objects.get(id=groupid)
      if groupobj is None:
        return (-1,None)
      else:
        return (1,groupobj)
    except:
      exception_log = ('[%s] id passed = %d')%('getGroupById',groupid)
      self.UserLogger.exception(exception_log)
      return (-2,[])
           
                    
