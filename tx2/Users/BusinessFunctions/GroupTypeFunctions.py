from tx2.Users.DBFunctions.DatabaseFunctions import DBLoginUser ,DBLogoutUser, DBGroupTypeInsert
from tx2.Users.DBFunctions.Messages import decode
from tx2.Users.models import GroupType
from tx2.Misc.CacheManagement import setCache,getCache,deleteCacheKey
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT, SYSTEM_USERDEFINED_GROUPTYPE
import logging
import inspect

class GroupTypeFnx():
    
  def __init__(self): 
    self.UserLogger = logging.getLogger(LoggerUser)
    self.CACHEKEY = 'CACHE_KEY_ALL_GROUPTYPE'
        #CRUD FUNCTIONS

  def CreateGroupType(self,gname,gdesc,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
      details = {
        'ip':ip,
        'by':by,
        'name':gname,
        'desc':gdesc,
        'req_op':req_op,
        }
      result = DBGroupTypeInsert(details)
      if (result['result'] == 1):
        deleteCacheKey(self.CACHEKEY)
        return (1,'SUCESS. GroupType has been sucessfully added to database.') 
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
        
  def getGroupTypeFromCache(self):
    GroupTypeList = getCache(self.CACHEKEY)
    if GroupTypeList is not -1 and GroupTypeList is not None:
      return (1,GroupTypeList)
    else:
      return (-1,'ERROR in Retrieveing grouptypes from cache')
            
  def ListAllGroupTypes(self):
    try:
      grouptypelist = self.getGroupTypeFromCache()
      if grouptypelist[0] != 1:
        grouptypelist =  GroupType.objects.all()  
        setCache(self.CACHEKEY,grouptypelist)
      else:
        grouptypelist = grouptypelist[1]
      return (1,grouptypelist)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))

        
  def getGroupTypeByName(self,gtypename):
    try:
      grouptypelist = self.ListAllGroupTypes()
      if grouptypelist[0] is 1:
        for x in grouptypelist[1]:
          if x.GroupTypeName == gtypename:
            return (1,x)
        return (-1,'ERROR : GroupType does not exist')
      else:
        return (-1,'ERROR : Error retrieving requested data from database')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
        
def TestGroupTypeFunctions():
  GroupTypeFnxObj = GroupTypeFnx()
  print 'adding 2 groups types'
  for x in range(0,2):
    gname = 'grouptype' + str(x)
    result  = GroupTypeFnxObj.CreateGroupType(gname,gname,1,'testing')
    print gname , result
  print 'now i will get all groupo types and print them '
  GroupTypeList = GroupTypeFnxObj.ListAllGroupTypes()
  if GroupTypeList[0] != 1:
    print GroupTypeList[1]
  else:
    for gt in GroupTypeList[1]:
      print "%s %s" % (gt.GroupTypeName , gt.GroupTypeDescription)
      obj = GroupTypeFnxObj.getGroupTypeByName(gt.GroupTypeName)
      if obj[0] != 1:
        print obj[1]
