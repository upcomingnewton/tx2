from tx2.Users.models import Menu,GroupMenu,Group
from tx2.Users.DBFunctions.DatabaseFunctions import DBGroupMenuInsert , DBGroupMenuDelete
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_DELETE
from tx2.Misc.CacheManagement import setCache,getCache
from tx2.Users.DBFunctions.Messages import decode
import logging

class GroupMenuFnx():
    
  def __init__(self):
    self.UserLogger = logging.getLogger(LoggerUser)
    self.ExceptionMessage = "Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon"
    
    self.CACHEKEY = 'CACHE_KEY_ALL_MENU'
  
  def MakeExceptionMessage(self,msg):
    return 'Exception Generated : ' + str(msg) + ' Administrators have been alerted to rectify the error. We will send you a notification in this regard soon.'
          
  def getStringFromList(self,_List):
    _str = ''
    try:
      for x in _List:
        _str += str(x) + ','
      _str = _str[:-1]
      return _str
    except:
      return ''
        
  def Insert(self,MenuList,GroupID,PermissionList,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT):
    try:
      details = {
        'MenuStr':self.getStringFromList(MenuList),
        'GroupID':GroupID,
        'PermissionStr':self.getStringFromList(PermissionList),
        'RequestedOperation':RequestedOperation,
        'by':by,
        'ip':ip,
        }
      result = DBGroupMenuInsert(details)
      if (result['result'] == 1):
        return (1,'SUCESS. Group Menus has been sucessfully added to database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('Insert')
      return (-2,self.MakeExceptionMessage(str(ex)))

  def Delete(self,MenuIDList,by,ip,RequestedOperation=SYSTEM_PERMISSION_DELETE):
    try:
      details = {
        'MenuIDStr':self.getStringFromList(MenuIDList),
        'RequestedOperation':RequestedOperation,
        'by':by,
        'ip':ip,
        }
      result = DBGroupMenuDelete(details)
      if (result['result'] == 1):
        return (1,'SUCESS. Group Menus has been sucessfully deleted from database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('Delete')
      return (-2,self.MakeExceptionMessage(str(ex)))
