from tx2.Users.models import Menu,GroupMenu,Group
from tx2.Users.DBFunctions.DatabaseFunctions import DBGroupMenuInsert , DBGroupMenuDelete
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_DELETE,SYSTEM_STATE_DELETED
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
    
  def getListFromString(self,_str):
    _str = _str.split(self.MenuSep)
    try:
      _List = [int(x) for x in _str]
      return (1,_List)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      
  def getUniqueIntegersList(self,_list):
    UList = []
    try:
      for x in range(0,len(_list)):
        if _list[x] not in _list[x+1:]:
          UList.append(_list[x])
      return (1,UList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
    
        
  def Insert(self,MenuList,GroupID,PermissionList,extrainfo,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT):
    MenuStr = self.getStringFromList((MenuList))
    if MenuStr[0] != 1:
      return (-1,MenuStr[1])
    PermissionStr = self.getStringFromList((PermissionList))
    if PermissionStr[0] != 1:
      return (-1,PermissionStr[1])
    ExtraInfo = self.getStringFromList((extrainfo))
    if ExtraInfo[0] != 1:
      return (-1,ExtraInfo[1])
    try:
      details = {
        'MenuStr':MenuStr[1],
        'GroupID':GroupID,
        'PermissionStr':PermissionStr[1],
        'extrainfo':ExtraInfo[1],
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
    MenuIDStr = self.getStringFromList(self.getUniqueIntegersList(MenuIDList)[1])
    if MenuIDStr[0] != 1:
      return (-1,MenuIDStr[1])
    try:
      details = {
        'MenuIDStr':MenuIDStr[1],
        'RequestedOperation':RequestedOperation,
        'by':by,
        'ip':ip,
        }
      result = DBGroupMenuDelete(details)
      if (result['result'] == 1):
        from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
        # get a list of groups, and delete cache for each
        GroupFnxObj = GroupFnx()
        GroupList = GroupFnxObj.ListAllGroups()
        if GroupList[0] == 1:
          for x in GroupList[1]:
            deleteCacheKey(self.getKey(x.id))
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
      
  def AddGroupMenu(self,MenuList,GroupID,_PermissionList,_extrainfo,by,ip,Insop=SYSTEM_PERMISSION_INSERT,Delop=SYSTEM_PERMISSION_DELETE):
    PreviousList = self.getGroupMenuObjectByGroupID(GroupID)
    if PreviousList[0] != 1:
      return (-1,PreviousList[1])
    else:
      PreviousList = PreviousList[1]
    try:
      #CommonEle = []
      NewEle = []
      #DeleteEle = []
      PermissionList = []
      extrainfo = []
      
      for x in range(0,len(MenuList)):
        if MenuList[x] not in PreviousList:
          NewEle.append(MenuList[x])
          PermissionList.append(_PermissionList[x])
          extrainfo.append(_extrainfo[x])
      
#      # 1. delete 
#      if len(DeleteEle) > 0 :
#        resultDel = self.Delete(DeleteEle,by,ip,Delop)
#        self.UserLogger.debug('%s %s' % ('DELETE',str(resultDel)))
      # 2. insert
      if len(NewEle) > 0 :
        resultIns = self.Insert(NewEle,GroupID,PermissionList,extrainfo,by,ip,Insop)
        return resultIns
      else:
        return (-1,'No element to add')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      
  def DeleteGroupMenu(self,MenuList,GroupID,by,ip,Insop=SYSTEM_PERMISSION_INSERT,Delop=SYSTEM_PERMISSION_DELETE):
    PreviousList = self.getGroupMenuObjectByGroupID(GroupID)
    if PreviousList[0] != 1:
      return (-1,PreviousList[1])
    else:
      PreviousList = PreviousList[1]
    try:
      #CommonEle = []
      DeleteEle = []
      for x in PreviousList:
        if x.Menu.id in MenuList:
          DeleteEle.append(x.id)
          
      if len(DeleteEle) > 0 :
        resultDel = self.Delete(DeleteEle,by,ip,Delop)
        return resultDel
      else:
        return (-1,'No element to delete')
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
        #print '===== CACHE RETURN :: %d ====== ' % (groupid)
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
      
  def getGroupMenuObjectByGroupID(self,groupid):
    try:
      GroupMenuObjList = []
      GroupMenuList = self.getListFromCache(groupid)
      if GroupMenuList[0] != 1:
        GroupMenuList = GroupMenu.objects.filter(Group__id = groupid)
        for m in GroupMenuList:
          if m.Menu.State.StateName != SYSTEM_STATE_DELETED:
            GroupMenuObjList.append(m)
        setCache(self.getKey(groupid),GroupMenuObjList)
      else:
        GroupMenuObjList = GroupMenuList[1]
      return (1,GroupMenuObjList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      
  def getParentGroupMenuObjectByGroupID(self,groupid):
    try:
      ParentGroupMenuList = []
      GroupMenuObjList = self.getGroupMenuObjectByGroupID(groupid)
      if GroupMenuObjList[0] != 1:
        return (-1,GroupMenuObjList[1])
      else:
        GroupMenuObjList = GroupMenuObjList[1]
        for x in GroupMenuObjList:
          if x.Menu.MenuPid == -1:
            ParentGroupMenuList.append(x)
      return (1,ParentGroupMenuList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      
def TestGroupMenuFuntions():
  GroupMenuFnxObj  = GroupMenuFnx()
  from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
  from tx2.Users.BusinessFunctions.MenuFunctions import MenuFnx
  # get a list of groups
  GroupFnxObj = GroupFnx()
  MenuFnxObj =  MenuFnx()
  GroupList = GroupFnxObj.ListAllGroups()
  if GroupList[0] != 1:
    return GroupList[1]
  else:
    GroupList = GroupList[1]
    print ' === PRINTING ALL GROUPS ==='
    for g in GroupList:
      print g.GroupName
    MenuList = MenuFnxObj.getParentMenu()
    if MenuList[0] != 1:
      return MenuList[1]
    else:
      MenuList = MenuList[1]
      print ' === PRINTING ALL PARENT MENU ==='
      for p in MenuList:
        print p.MenuName
      import random
      print ' === FOR EACH GROUP, ADD 2 PARENT MENUS ==='
      for g in GroupList:
        pstr = []
        p1 = random.randint(0,len(MenuList)-1)
        print 'PARENT -1 = %d , %s' % (MenuList[p1].id, MenuList[p1].MenuName)
        # add parent 1
        pstr.append(MenuList[p1].id)
        ChildMenu = MenuFnxObj.getChildMenuByParentID(MenuList[p1].id)
        if ChildMenu[0] is 1:
          for c in ChildMenu[1]:
            pstr.append(c.id)
        p2 = random.randint(0,len(MenuList)-1)
        print 'PARENT -2 = %d , %s' % (MenuList[p2].id, MenuList[p2].MenuName)
        pstr.append(MenuList[p2].id)
        ChildMenu = MenuFnxObj.getChildMenuByParentID(MenuList[p2].id)
        if ChildMenu[0] is 1:
          for c in ChildMenu[1]:
            pstr.append(c.id)
        print '=== menu list ===' ,pstr
        result = GroupMenuFnxObj.Insert(pstr,g.id,pstr,pstr,1,'test')
        if result[0] != 1:
          return result[1]
        else:
          print pstr, g.GroupName , result
  # now for each group, get the list of menu and delete them
    for g in GroupList:
      GroupMenuObjList = GroupMenuFnxObj.getGroupMenuObjectByGroupID(g.id)
      if GroupMenuObjList[0] != 1:
        return GroupMenuObjList[1]
      else:
        menustr = []
        print '=== %s, Menu in this group ===' % (g.GroupName)
        for p in GroupMenuObjList[1]:
          print p.Menu.MenuName
          menustr.append(p.id)
        print menustr , g.GroupName
        result = GroupMenuFnxObj.Delete(menustr,1,'ip')
        print menustr , g.GroupName , result
