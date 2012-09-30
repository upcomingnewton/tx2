from django.db import models
from tx2.Users.models import Group
from tx2.Users.DBFunctions.DatabaseFunctions import DBGroupInsert, DBgetUserIDListByGroupID
from tx2.Users.DBFunctions.Messages import decode
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_ENTITY,CACHE_KEY_SYSTEM_ENTITY, SESSION_SELECTED_GROUPS
from tx2.Misc.CacheManagement import setCache,getCache,deleteCacheKey
from tx2.Security.models import Entity
import logging
import inspect

class GroupFnx(models.Model):
  def __init__(self):
    self.UserLogger = logging.getLogger(LoggerUser)
    self.CACHE_KEY_ALL_GROUPS = 'CACHE_KEY_ALL_GROUPS'

      #CRUD FUNCTIONS
        
  def CreateGroup(self,gname,gdesc,gtype,entity,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    eid = entity
    if entity == -1:
      eid = getSystemEntity()
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
        deleteCacheKey(self.CACHE_KEY_ALL_GROUPS)
        return (1,'SUCESS. Group has been sucessfully added to database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))


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
      if grouplist[0] != 1:
        grouplist =  Group.objects.all()
        setCache(self.CACHE_KEY_ALL_GROUPS,grouplist)
      else:
        grouplist = grouplist[1]
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
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      RegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      
  def getUserIDListByGroupID(self,groupid):
    try:
      UserList = DBgetUserIDListByGroupID(groupid)
      if UserList[0] == 1:
        return (1,UserList[1])
      else:
        return (-1,UserList[1])
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      RegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
           
                    
