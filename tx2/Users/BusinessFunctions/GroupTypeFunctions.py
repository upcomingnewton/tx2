from tx2.Users.DBFunctions.DatabaseFunctions import DBLoginUser ,DBLogoutUser, DBGroupTypeInsert
from tx2.Users.DBFunctions.DBMessages import decode
from tx2.Users.models import GroupType
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT, SYSTEM_USERDEFINED_GROUPTYPE
import logging

class GroupTypeFnx():
    
  def __init__(self): 
    self.UserLogger = logging.getLogger(LoggerUser)
    self.ExceptionMessage = "Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon"
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
      self.UserLogger.debug('[%s] %s,%s'%('CreateGroupType',str(details),str(result)))
      return (1,result)
    except:
      exception_log = ('[%s] %s,%s,%s,%s,%s,%s')%('CreateGroup',gname,gdesc,gtype,entity,by,ip)
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)


        # SELECTION AND QUERY FUNCTIONS
        
  def getGroupTypeFromCache(self):
    GroupTypeList = getCache(self.CACHEKEY)
    if GroupList is not -1 and GroupList is not None:
      return GroupTypeList
    else:
      return -1
            
  def ListAllGroupTypes(self):
    try:
      grouptypelist = self.getGroupTypeFromCache()
      if grouptypelist is -1:
        grouptypelist =  GroupType.objects.all()  
        setCache(self.CACHEKEY,grouptypelist)
      return (1,grouptypelist)
    except:
      exception_log = ('ListAllGroupTypes')
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)

        
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
    except:
      exception_log = ('getGroupTypeByName')
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage) 
        
    
      
