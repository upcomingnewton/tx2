from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
from tx2.Users.BusinessFunctions.GroupTypeFunctions import GroupTypeFnx
import logging
import inspect
from django.contrib import messages
Logger_User = logging.getLogger(LoggerUser)


##################################################################
def GroupIndex(HttpRequest, options):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    GroupFnxObj  = GroupFnx()
    GroupList = GroupFnxObj.ListAllGroups()
    if(GroupList[0] == 1):
      GroupList  = GroupList[1]
      if( len (GroupList) == 0):
        messages.error(HttpRequest,'There are no Group in the system')
      return render_to_response("UserSystem/Group/SelectGroups.html",{'GroupList':GroupList,'options':options},context_instance=RequestContext(HttpRequest))
    else:
      messages.error(HttpRequest,'ERROR : %s' % GroupList[0])
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
