from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
from tx2.Users.BusinessFunctions.GroupMenuFunctions import GroupMenuFnx
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
from tx2.Users.BusinessFunctions.MenuFunctions import MenuFnx
from tx2.conf.LocalProjectConfig import  SESSION_SELECTED_GROUPS
import logging
import inspect
from django.contrib import messages
LoggerUser = logging.getLogger(LoggerUser)


##################################################################
def GroupMenuViewIndex(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    for k in HttpRequest.session.keys():
      print k
    if SESSION_SELECTED_GROUPS not in HttpRequest.session.keys():
      print '====== list is not there'
      messages.error(HttpRequest,'Please select some groups for furthur operations')
      return HttpResponseRedirect('/user/group/select/')
    else:
      SelectedGroups = HttpRequest.session[SESSION_SELECTED_GROUPS]
      return render_to_response("UserSystem/GroupMenu/GroupMenuIndex.html",{'SelectedGroups':SelectedGroups},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')


##################################################################
def GroupMenuDetailsIndex(HttpRequest,GroupID):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    GroupMenuFnxobj = GroupMenuFnx()
    GroupMenuObjList = GroupMenuFnxobj.getGroupMenuObjectByGroupID(int(GroupID))
    print GroupMenuObjList
    if GroupMenuObjList[0] != 1:
      messages.error(HttpRequest,"ERROR " + str(GroupMenuObjList[1]))
      return HttpResponseRedirect('/message/')
    ParentGroupMenuList  = GroupMenuFnxobj.getParentGroupMenuObjectByGroupID(int(GroupID))
    print ParentGroupMenuList
    if ParentGroupMenuList[0] != 1:
      messages.error(HttpRequest,"ERROR " + str(ParentGroupMenuList[1]))
      return HttpResponseRedirect('/message/')
    return render_to_response("UserSystem/GroupMenu/GroupMenuDetails.html",{'ParentGroupMenuList':ParentGroupMenuList[1],'GroupMenuObjList':GroupMenuObjList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

##################################################################
def GroupMenuAddIndex(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    if SESSION_SELECTED_GROUPS not in HttpRequest.session.keys():
      messages.error(HttpRequest,'Please select some groups for furthur operations')
      return HttpResponseRedirect('/user/group/select/')
    else:
      MenuFnxobj = MenuFnx()
      MenuList = MenuFnxobj.getAllMenuObj()
      if MenuList[0] != 1:
        messages.error(HttpRequest,"ERROR " + str(MenuList[1]))
        return HttpResponseRedirect('/message/')
      ParentMenuList  = MenuFnxobj.getParentMenu()
      if ParentMenuList[0] != 1:
        messages.error(HttpRequest,"ERROR " + str(ParentMenuList[1]))
        return HttpResponseRedirect('/message/')
      return render_to_response("UserSystem/GroupMenu/GroupMenuDetailsAdd.html",{'ParentMenuList':ParentMenuList[1],'MenuList':MenuList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
##################################################################
def GroupMenuDeleteIndex(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    if SESSION_SELECTED_GROUPS not in HttpRequest.session.keys():
      messages.error(HttpRequest,'Please select some groups for furthur operations')
      return HttpResponseRedirect('/user/group/select/')
    else:
      MenuFnxobj = MenuFnx()
      MenuList = MenuFnxobj.getAllMenuObj()
      if MenuList[0] != 1:
        messages.error(HttpRequest,"ERROR " + str(MenuList[1]))
        return HttpResponseRedirect('/message/')
      ParentMenuList  = MenuFnxobj.getParentMenu()
      if ParentMenuList[0] != 1:
        messages.error(HttpRequest,"ERROR " + str(ParentMenuList[1]))
        return HttpResponseRedirect('/message/')
      return render_to_response("UserSystem/GroupMenu/GroupMenuDetailsDelete.html",{'ParentMenuList':ParentMenuList[1],'MenuList':MenuList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

##################################################################
def GroupMenuAdd(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    if SESSION_SELECTED_GROUPS not in HttpRequest.session.keys():
      messages.error(HttpRequest,'Please select some groups for furthur operations')
      return HttpResponseRedirect('/user/group/select/')
    else:
      MenuList = HttpRequest.POST.getlist('MenuList')
      MenuList = [int(x) for x in MenuList]
      PermList = []
      for x in MenuList:
        PermList.append(int(HttpRequest.POST['Perm_' + str(x)]))
      GroupMenuFnxObj = GroupMenuFnx()
      Grouplist = HttpRequest.session['SESSION_SELECTED_GROUPS']
      for group in Grouplist:
        result = GroupMenuFnxObj.AddGroupMenu(MenuList,int(group),PermList,MenuList,int(logindetails["userid"]),ip)
        messages.error(HttpRequest,"%s : %s" % (str(group),str(result)))
      del HttpRequest.session['SESSION_SELECTED_GROUPS']
      return HttpResponseRedirect('/user/group/select/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
##################################################################
def GroupMenuDelete(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    if SESSION_SELECTED_GROUPS not in HttpRequest.session.keys():
      messages.error(HttpRequest,'Please select some groups for furthur operations')
      return HttpResponseRedirect('/user/group/select/')
    else:
      MenuList = HttpRequest.POST.getlist('MenuList')
      MenuList = [int(x) for x in MenuList]
      GroupMenuFnxObj = GroupMenuFnx()
      Grouplist = HttpRequest.session['SESSION_SELECTED_GROUPS']
      for group in Grouplist:
        result = GroupMenuFnxObj.DeleteGroupMenu(MenuList,int(group),int(logindetails["userid"]),ip)
        messages.error(HttpRequest,"%s : %s" % (str(group),str(result)))
      del HttpRequest.session['SESSION_SELECTED_GROUPS']
      return HttpResponseRedirect('/user/group/select/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
