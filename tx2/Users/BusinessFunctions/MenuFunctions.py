from django.db import models
from tx2.Users.models import Menu
from tx2.Users.DBFunctions.DatabaseFunctions import DBMenuInsert , DBMenuUpdate
from tx2.Users.DBFunctions.Messages import decode
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_UPDATE
from tx2.Misc.CacheManagement import setCache,getCache
import logging

class MenuFnx():
  
  def __init__(self):
    self.UserLogger = logging.getLogger(LoggerUser)
    self.ExceptionMessage = "Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon"
    self.CACHEKEY = 'CACHE_KEY_ALL_MENU'
  
  def MakeExceptionMessage(self,msg):
    return 'Exception Generated : ' + str(msg) + ' Administrators have been alerted to rectify the error. We will send you a notification in this regard soon.'
        
  def Insert(self,MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT):
    try:
      details = {
        'MenuName':MenuName,
        'MenuDesc':MenuDesc,
        'MenuUrl':MenuUrl,
        'MenuPid':MenuPid,
        'MenuIcon':MenuIcon,
        'RequestedOperation':RequestedOperation,
        'by':by,
        'ip':ip,
        }
      result = DBMenuInsert(details)
      if (result['result'] == 1):
        return (1,'SUCESS. Menu has been sucessfully added to database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('Insert')
      return (-2,self.MakeExceptionMessage(str(ex)))
                
  def Update(self,MenuId,MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,by,ip,LogDesc,RequestedOperation=SYSTEM_PERMISSION_UPDATE):
    MenuObj = self.getMenuObjByMenuId(MenuId)
    if  MenuObj[0] is -1:
      return (-1,self.ExceptionMessage)
    PreviousState = str(MenuObj)
    try:
      details = {
		   		'MenuId':MenuId,
		   		'MenuName':MenuName,
		   		'MenuDesc':MenuDesc,
		   		'MenuUrl':MenuUrl,
		   		'MenuPid':MenuPid,
		   		'MenuIcon':MenuIcon,
		   		'RequestedOperation':RequestedOperation,
		   		'LogDesc':LogDesc,
		   		'LogPreviousState':PreviousState,
          'by':by,
		   		'ip':ip,
        }
      result = DBMenuUpdate(details)
      if (result['result'] == 1):
        return (1,'SUCESS. Menu has been sucessfully updated in database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('Update')
      return (-2,self.MakeExceptionMessage(str(ex)))
        
  def getMenuListFromCache(self):
    try:
      MenuList = getCache(self.CACHEKEY)
      if MenuList is not -1 and MenuList is not None:
        return (1,MenuList)
      else:
        return (-1,'ERROR in Retrieveing Menu from cache')
    except Exception, ex:
      self.UserLogger.exception('getMenuListFromCache')
      return (-2,self.MakeExceptionMessage(str(ex)))

  def getAllMenuObj(self):
    try:
      MenuList = self.getMenuListFromCache()
      if MenuList[0] is not 1:
        MenuList = Menu.objects.all()
        setCache(self.CACHEKEY,MenuList)
      return (1,MenuList)
    except Exception, ex:
      self.UserLogger.exception('getAllMenuObj')
      return (-2,self.MakeExceptionMessage(str(ex)))
        

  def getMenuObjByMenuId(self,menuid):
    try:
      MenuList = self.getAllMenuObj()
      if MenuList[0] is 1:
        for x in MenuList[1]:
          if x.id == menuid:
            return (1,x)
        return (-1,'ERROR : Menu does not exist')
      else:
        return (-1,'ERROR : Error retrieving requested data from database')
    except Exception, ex:
      self.UserLogger.exception('getMenuObjByMenuId')
      return (-2,self.MakeExceptionMessage(str(ex)))


  def getParentMenu(self):
    try:
      MenuList = self.getAllMenuObj()
      ParentMenuList = []
      if MenuList[0] is 1:
        for x in MenuList[1]:
          if x.MenuPid == -1:
            ParentMenuList.append(x)
        return (1,ParentMenuList)
      else:
        return (-1,'ERROR : Error retrieving requested data from database')
    except Exception, ex:
      self.UserLogger.exception('getParentMenu')
      return (-2,self.MakeExceptionMessage(str(ex)))


  def getChildMenuByParentID(self,pid):
    try:
      MenuList = self.getAllMenuObj()
      ChildMenuList = []
      if MenuList[0] is 1:
        for x in MenuList[1]:
          if x.MenuPid == pid:
            ChildMenuList.append(x)
        return (1,ChildMenuList)
      else:
        return (-1,'ERROR : Error retrieving requested data from database')
    except Exception, ex:
      self.UserLogger.exception('getChildMenuByParentID')   
      return (-2,self.MakeExceptionMessage(str(ex)))

