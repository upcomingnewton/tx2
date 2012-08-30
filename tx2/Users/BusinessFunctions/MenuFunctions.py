from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from tx2.Users.models import Menu
from tx2.Users.DBFunctions.DatabaseFunctions import DBMenuInsert , DBMenuUpdate
from tx2.Users.DBFunctions.Messages import decode
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_UPDATE
from tx2.Misc.CacheManagement import setCache,getCache,deleteCacheKey,getDeletedState
import logging
import inspect

class MenuFnx():
  
  def __init__(self):
    self.UserLogger = logging.getLogger(LoggerUser)
    self.CACHEKEY = 'CACHE_KEY_ALL_MENU'

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
        deleteCacheKey(self.CACHEKEY)
        return (1,'SUCESS. Menu has been sucessfully added to database.') 
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
                
  def Update(self,MenuId,MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,by,ip,LogDesc,RequestedOperation=SYSTEM_PERMISSION_UPDATE):
    MenuObj = ''
    try:
      MenuObj = Menu.objects.get(id=MenuId)
    except ObjectDoesNotExist:
      return (-1,'Menu does not exist.')
    PreviousState = str(MenuObj)
    #TODO store based on comparisons
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
        deleteCacheKey(self.CACHEKEY)
        return (1,'SUCESS. Menu has been sucessfully updated in database.') 
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
        
  def getMenuListFromCache(self):
    try:
      MenuList = getCache(self.CACHEKEY)
      if MenuList is not -1 and MenuList is not None:
        return (1,MenuList)
      else:
        return (-1,'Error in Retrieveing Menu from cache.')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))

  def getAllMenuObj(self):
    try:
      MenuList = self.getMenuListFromCache()
      if MenuList[0] is not 1:
        getDeletedState()
        MenuList = Menu.objects.exclude(State = getDeletedState())
        setCache(self.CACHEKEY,MenuList)
      else:
        MenuList = MenuList[1]
      return (1,MenuList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex)) 
      
  def getDeletedMenuObj(self):
    try:
        MenuList = Menu.objects.filter(State = getDeletedState())
        return (1,MenuList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex)) 
        

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
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex)) 


  def getDeletedMenuObjByMenuId(self,menuid):
    try:
      MenuList = self.getDeletedMenuObj()
      if MenuList[0] is 1:
        for x in MenuList[1]:
          if x.id == menuid:
            return (1,x)
        return (-1,'ERROR : Menu does not exist')
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
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))


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
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex)) 


def TestMenuFunctions():
  MenuFnxObj = MenuFnx()
  print 'inserting 5 parent menu'
  for x in range(0,5):
    pname = 'ParentMenu' + str(x)
    result = MenuFnxObj.Insert(pname,pname,pname,-1,pname,1,'test from main')
    print pname , result
  print 'getting parent menu list'
  ParentMenuList = MenuFnxObj.getParentMenu()
  if ParentMenuList[0] != 1:
    print ParentMenuList[1]
  else:
    for par in ParentMenuList[1]:
      parobj = MenuFnxObj.getMenuObjByMenuId(par.id)
      if parobj[0] != 1:
        print parobj[1]
      else:
        print 'printing children for %s' % (parobj[1].MenuName)
        ChildList = MenuFnxObj.getChildMenuByParentID(parobj[1].id)
        if ChildList[0] == 1:
          for p in ChildList[1]:
            print p.MenuName
        print '=== adding 1 more child ==='
        pname = parobj[1].MenuName + "- Child_"
        result = MenuFnxObj.Insert(pname,pname,pname,parobj[1].id,pname,1,'test from main')
        print pname , result
        print '=== Updating this parent ==='
        result = MenuFnxObj.Update(parobj[1].id,parobj[1].MenuName + "_updated",parobj[1].MenuName + "_updated",parobj[1].MenuName + "_updated",-1,parobj[1].MenuName + "_updated",1,'updated ip','updating test')
        print result
  print 'Finally printing all menu'
  MenuList = MenuFnxObj.getAllMenuObj()
  if MenuList[0] != 1:
    print MenuList[1]
  else:
    for menu in MenuList:
      print "%s\t%s\t%d" % (menu.MenuName, menu.MenuUrl, menu.MenuPid)
