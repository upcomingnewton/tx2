from tx2.Users.models import Menu,GroupMenu,Group
from tx2.Users.DBFunctions.DatabaseFunctions import DBGroupMenuInsert , DBGroupMenuDelete
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_DELETE
from tx2.Misc.CacheManagement import setCache,getCache
import logging

class GroupMenuFnx():
    
  def __init__(self):
    self.UserLogger = logging.getLogger(LoggerUser)
    self.ExceptionMessage = "Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon"
    self.CACHEKEY = 'CACHE_KEY_ALL_MENU'
            
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
      res = DBGroupMenuInsert(details)
      return res
    except:
      error_msg = 'EXCEPTION at Business Functions in Insert'
      self.UserLogger.exception(error_msg)
      return (-5,error_msg)

  def Delete(self,MenuIDList,by,ip,RequestedOperation=SYSTEM_PERMISSION_DELETE):
    try:
      details = {
        'MenuIDStr':self.getStringFromList(MenuIDList),
        'RequestedOperation':RequestedOperation,
        'by':by,
        'ip':ip,
        }
      res = DBGroupMenuDelete(details)
      return res
    except:
      error_msg = 'EXCEPTION at Business Functions in Delete'
      self.UserLogger.exception(error_msg)
      return (-5,error_msg)
