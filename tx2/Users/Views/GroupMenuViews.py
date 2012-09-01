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
Logger_User = logging.getLogger(LoggerUser)


##################################################################
def GroupMenuViewIndex(HttpRequest):
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
      SelectedGroups = HttpRequest.session[SESSION_SELECTED_GROUPS]
      return render_to_response("UserSystem/Group/EditGroup.html",{'SelectedGroups':SelectedGroups},context_instance=RequestContext(HttpRequest))
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
    if GroupMenuObjList[0] != 1:
      messages.error(HttpRequest,"ERROR " + str(GroupMenuObjList[1]))
      return HttpResponseRedirect('/message/')
    ParentGroupMenuList  = GroupMenuFnxobj.getParentGroupMenuObjectByGroupID(int(GroupID))
    if ParentGroupMenuList[0] != 1:
      messages.error(HttpRequest,"ERROR " + str(ParentGroupMenuList[1]))
      return HttpResponseRedirect('/message/')
    return render_to_response("UserSystem/Group/EditGroup.html",{'ParentGroupMenuList':ParentGroupMenuList[1],'GroupMenuObjList':GroupMenuObjList[1]},context_instance=RequestContext(HttpRequest))
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
def GroupMenuEditIndex(HttpRequest, options):
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
      SelectedGroups = HttpRequest.session[SESSION_SELECTED_GROUPS]
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

def CreateNewGroupIndex(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    GroupTypeFnxObj  = GroupTypeFnx()
    GroupTypeList = GroupTypeFnxObj.ListAllGroupTypes()
    if(GroupTypeList[0] == 1):
      GroupTypeList  = GroupTypeList[1]
      if( len (GroupTypeList) == 0):
        messages.error(HttpRequest,'There are no Group types in the system')
      return render_to_response("UserSystem/Group/EditGroup.html",{'GroupTypeList':GroupTypeList},context_instance=RequestContext(HttpRequest))
    else:
      messages.error(HttpRequest,'ERROR : %s' % GroupTypeList[0])
      return HttpResponseRedirect('/message/')
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
def CreateNewGroup(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    Group_Name = ""
    Group_Desc = ""
    Group_GroupType = ""
    flag = 0
    if "Group_Name" in HttpRequest.POST:
      Group_Name = HttpRequest.POST['Group_Name']
    else:
      messages.error(HttpRequest,'error performing operation. Problem in Name')
      flag = 1
    if "Group_Desc" in HttpRequest.POST:
      Group_Desc = HttpRequest.POST['Group_Desc']
    else:
      messages.error(HttpRequest,'error performing operation.Problem in desc')
      flag = 1
    if 'Group_GroupType' in  HttpRequest.POST:
      Group_GroupType = int(HttpRequest.POST['Group_GroupType'])
      if Group_GroupType == -1:
        messages.error(HttpRequest,'Please select a proper group type')
        flag = 1
    else:
      messages.error(HttpRequest,'error performing operation.Problem in GroupType')
      flag = 1
    if flag == 1:
      return HttpResponseRedirect('/message/')
    else:
      GroupFnxObj  = GroupFnx()
      result = GroupFnxObj.CreateGroup(Group_Name,Group_Desc,Group_GroupType,-1,logindetails["userid"],ip)
      messages.error(HttpRequest,result[1])
      return HttpResponseRedirect('/user/group/')
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
def GroupSelectToMemory(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
      grouplist = HttpRequest.POST.getlist('SelectedGroups')
      grouplist = [int(x) for x in grouplist]
      HttpRequest.Session[SESSION_SELECTED_GROUPS] = grouplist
      messages.error(HttpRequest,"Selected Groups have been sucessfully added to memory")
      return HttpResponseRedirect('/user/group/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
