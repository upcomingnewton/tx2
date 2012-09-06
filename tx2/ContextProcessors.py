from tx2.CONFIG import TEMPLATE_PARAM_USER_NOT_LOGGED_IN, GROUP_MENU_PREFIX, SESSION_MESSAGE, LoggerUser
from tx2.conf.LocalProjectConfig import  SESSION_SELECTED_GROUPS, ANONYMOUS_GROUP, ALL_LOGGED_IN_USERS_GROUP
from tx2.Misc.CacheManagement import setCache,getCache,deleteCacheKey
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.BusinessFunctions.GroupMenuFunctions import GroupMenuFnx
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
#from ThoughtXplore.txMenu.BusinessFunctions.LoginMenuFunctions import MakeGroupMenu
import logging
import inspect

Logger_User = logging.getLogger(LoggerUser)

        
def UserContextProcessor(request):
    try:
      logindetails = GetLoginDetails(request)
      GroupMenuFnxObj = GroupMenuFnx()
      if( logindetails["userid"] != -1):
        # USER IS LOGGED IN, GET THE MENU LISTS AND PASS HERE
        # get the groupid
        AllUsersGid = getCache(ALL_LOGGED_IN_USERS_GROUP)
        if AllUsersGid == None or AllUsersGid == -1:
          GroupFnxObj = GroupFnx()
          gobj = GroupFnxObj.getGroupObjectByName(ALL_LOGGED_IN_USERS_GROUP)
          if (gobj[0] == 1):
            AllUsersGid = gobj[1].id
          else:
            return {'loggedin':False}
          setCache(ALL_LOGGED_IN_USERS_GROUP,AllUsersGid)
        #get the menulist
        AllUsersChildMenuList = GroupMenuFnxObj.getGroupMenuObjectByGroupID(AllUsersGid)[1]
        AllUsersParentMenuList = GroupMenuFnxObj.getParentGroupMenuObjectByGroupID(AllUsersGid)[1]
        GroupChildMenuList = GroupMenuFnxObj.getGroupMenuObjectByGroupID(int(logindetails['groupid']))[1]
        GroupParentMenuList = GroupMenuFnxObj.getParentGroupMenuObjectByGroupID(int(logindetails['groupid']))[1]
        return_dict =  {  
                  "userid":logindetails['userid'],
                  "groupid":logindetails['groupid'],
                  "loginid":logindetails['loginid'],
                  "fname":logindetails["fname"],
                  "loggedin":True,
                  "AllUsersChildMenuList":AllUsersChildMenuList,
                  "AllUsersParentMenuList":AllUsersParentMenuList,
                  "GroupChildMenuList":GroupChildMenuList,
                  "GroupParentMenuList":GroupParentMenuList,
              }
        return return_dict
      else:
        # USER IS NOT LOGGED IN, GET ANONYMOUS LISTS AND PASS HERE
        AnonymousUsersGid = getCache(ANONYMOUS_GROUP)
        if AnonymousUsersGid == None or AnonymousUsersGid == -1:
          GroupFnxObj = GroupFnx()
          gobj = GroupFnxObj.getGroupObjectByName(ANONYMOUS_GROUP)
          if (gobj[0] == 1):
            AnonymousUsersGid = gobj[1].id
          else:
            return {'loggedin':False}
          setCache(ANONYMOUS_GROUP,AnonymousUsersGid)
        #get the menulist
        AnonymousChildMenuList = GroupMenuFnxObj.getGroupMenuObjectByGroupID(AnonymousUsersGid)[1]
        AnonymousParentMenuList = GroupMenuFnxObj.getParentGroupMenuObjectByGroupID(AnonymousUsersGid)[1]
        return_dict =  {
                  "loggedin":False,
                  "AnonymousChildMenuList":AnonymousChildMenuList,
                  "AnonymousParentMenuList":AnonymousParentMenuList,
               }
        return return_dict
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'loggedin':False}

#def MessageContextProcessor(request):
#    try:
#        if SESSION_MESSAGE in request.session.keys():
#            msglist = request.session[SESSION_MESSAGE]
#            del request.session[SESSION_MESSAGE]
#            return {'msglist':msglist,}
#        else:
#            return {'msglist':[],}
#    except:
#        LOGGERUSER.exception('EXCEPTION IN MessageContextProcessor')
