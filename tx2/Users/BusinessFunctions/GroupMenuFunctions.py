from tx2.Users.models import Menu,GroupMenu,Group
from tx2.Users.DBFunctions.DatabaseFunctions import DBGroupMenuInsert , DBGroupMenuDelete
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_DELETE
from tx2.Misc.CacheManagement import setCache,getCache,deleteCacheKey
from tx2.Users.DBFunctions.Messages import decode
import logging
import inspect

class GroupMenuFnx():
    
  def __init__(self):
    self.UserLogger = logging.getLogger(LoggerUser)
    self.CACHEKEY = 'CACHE_KEY_ALL_MENU'
    self.MenuSep = ','

  def getKey(self,groupid):
    return 'GroupMenuKeys_' + str(groupid)

  def getStringFromList(self,_List):
    _str = ''
    try:
      for x in _List:
        _str += str(x) + self.MenuSep
      _str = _str[:-1]
      return (1,_str)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
        
  def Insert(self,MenuList,GroupID,PermissionList,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT):
    MenuStr = self.getStringFromList(MenuList)
    if MenuStr[0] != 1:
      return (-1,MenuStr[1])
    PermissionStr = self.getStringFromList(PermissionList)
    if PermissionStr[0] != 1:
      return (-1,PermissionStr[1])
    try:
      details = {
        'MenuStr':MenuStr[1],
        'GroupID':GroupID,
        'PermissionStr':PermissionStr[1],
        'RequestedOperation':RequestedOperation,
        'by':by,
        'ip':ip,
        }
      result = DBGroupMenuInsert(details)
      if (result['result'] == 1):
        deleteCacheKey(self.getKey(GroupID))
        return (1,'SUCESS. Group Menus has been sucessfully added to database.') 
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

  def Delete(self,MenuIDList,by,ip,RequestedOperation=SYSTEM_PERMISSION_DELETE):
    MenuIDStr = self.getStringFromList(MenuIDList)
    if MenuIDStr[0] != 1:
      return (-1,MenuIDStr[1])
    try:
      details = {
        'MenuIDStr':self.getStringFromList(MenuIDList),
        'RequestedOperation':RequestedOperation,
        'by':by,
        'ip':ip,
        }
      result = DBGroupMenuDelete(details)
      if (result['result'] == 1):
        #TODO deleteCacheKey(self.getKey(GroupID))
        # get each group from group functions
        # delete each groups cache
        return (1,'SUCESS. Group Menus has been sucessfully deleted from database.') 
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
      
  ############## SELECT FUNCTIONS #################
  
  def getListFromCache(self, groupid):
    try:
      GroupMenuList = getCache(self.getKey(groupid))
      if GroupMenuList is not -1 and GroupMenuList is not None:
        return (1,GroupMenuList)
      else:
        return (-1,'ERROR in Retrieveing GroupMenuList from cache')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
