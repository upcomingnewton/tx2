from tx2.Users.DBFunctions.DatabaseFunctions import DBLoginUser ,DBLogoutUser, DBGroupTypeInsert
from tx2.Users.DBFunctions.Messages import decode
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
        
  def MakeExceptionMessage(self,msg):
    return 'Exception Generated : ' + str(msg) + ' Administrators have been alerted to rectify the error. We will send you a notification in this regard soon.'
        
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
        return (1,'SUCESS. GroupType has been sucessfully added to database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('CreateGroupType')
      return (-2,self.MakeExceptionMessage(str(ex)))


        # SELECTION AND QUERY FUNCTIONS
        
  def getGroupTypeFromCache(self):
    GroupTypeList = getCache(self.CACHEKEY)
    if GroupList is not -1 and GroupList is not None:
      return (1,GroupTypeList)
    else:
      return (-1,'ERROR in Retrieveing grouptypes from cache')
            
  def ListAllGroupTypes(self):
    try:
      grouptypelist = self.getGroupTypeFromCache()
      if grouptypelist is -1:
        grouptypelist =  GroupType.objects.all()  
        setCache(self.CACHEKEY,grouptypelist)
      return (1,grouptypelist)
    except Exception, ex:
      self.UserLogger.exception('ListAllGroupTypes')
      return (-2,self.MakeExceptionMessage(str(ex)))

        
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
      self.UserLogger.exception('getGroupTypeByName')
      return (-2,self.MakeExceptionMessage(str(ex)))
        
    
      
