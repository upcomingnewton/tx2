# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.BusinessFunctions.MenuFunctions import MenuFnx
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity,getSystemGroup_NewUsers, getSystemUser_DaemonCreateUser
from tx2.CONFIG import LoggerUser,SESSION_MESSAGE
from django.contrib import messages
import logging
import datetime
import inspect


LoggerUser = logging.getLogger(LoggerUser)
ExceptionMessage = 'ERROR : System has suffered some error while processing your request. Please try after some-time. If the problem persists, contact system administrators.'

def ListAllMenu(HttpRequest):
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,"Error.Please login to continue.")
    return HttpResponseRedirect('/user/login/')
  try:
    MenuObj = MenuFnx()
    MenuList = MenuObj.getAllMenuObj()
    if MenuList[0] == 1:
      return render_to_response('UserSystem/Menu/ListMenu.html',{"MenuList":MenuList[1]},context_instance=RequestContext(HttpRequest))
    else:
      messages.error(HttpRequest,"Error. %s" % (MenuList[0])) 
      return HttpResponseRedirect('/message/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,"Error. %s" % (str(ex))) 
      return HttpResponseRedirect('/message/')
    
def AddMenuIndex(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    msglist.append('Please Login to continue')
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/user/login/')
  try:
    MenuObj = MenuFnx()
    ParentMenuList = MenuObj.getParentMenu()
    if ParentMenuList[0] == 1:
      return render_to_response('UserSystem/Menu/AddMenu.html',{"ParentMenuList":ParentMenuList[1]},context_instance=RequestContext(HttpRequest))
    else:
      HttpRequest.session[SESSION_MESSAGE] = [ParentMenuList[1]]
      return HttpResponseRedirect('/message/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: Could not login user. ' + str(msg))
      return HttpResponseRedirect('/message/')
    
def EditMenuIndex(HttpRequest,MenuId):
  msglist = AppendMessageList(HttpRequest)
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    msglist.append('Please Login to continue')
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/user/login/')
  try:
    MenuObj = MenuFnx()
    MenuObject = MenuObj.getMenuObjByMenuId(MenuId)
    if MenuObject[0] == 1:
      return render_to_response('UserSystem/Menu/EditMenu.html',{"MenuObj":MenuObject[1]},context_instance=RequestContext(HttpRequest))
    else:
      HttpRequest.session[SESSION_MESSAGE] = [MenuObject[1]]
      return HttpResponseRedirect('/message/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: Could not login user. ' + str(msg))
      return HttpResponseRedirect('/message/')
    
# CB FNX

def AddMenu(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    msglist.append('Please Login to continue')
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/user/login/')
  try:
    flag = 0
    MenuName = ''
    MenuDesc = ''
    MenuUrl = ''
    MenuPid = ''
    MenuIcon = ''
    if "MenuName" in HttpRequest.POST and len(HttpRequest.POST['MenuName']) > 0:
      MenuName = HttpRequest.POST['MenuName']
    else:
      msglist.append('ERROR : MenuName not found or No value is entered for Menu Name')
      flag = 1
    if "MenuDesc" in HttpRequest.POST and len(HttpRequest.POST['MenuDesc']) > 0:
      MenuDesc = HttpRequest.POST['MenuDesc']
    else:
      msglist.append('ERROR : MenuDesc not found or No value is entered for MenuDesc')
      flag = 1
    if "MenuUrl" in HttpRequest.POST and len(HttpRequest.POST['MenuUrl']) > 0:
      MenuUrl = HttpRequest.POST['MenuUrl']
    else:
      msglist.append('ERROR : MenuUrl not found or No value is entered for MenuUrl')
      flag = 1
    if "MenuIcon" in HttpRequest.POST and len(HttpRequest.POST['MenuIcon']) > 0:
      MenuName = HttpRequest.POST['MenuIcon']
    else:
      msglist.append('ERROR : MenuIcon not found or No value is entered for MenuIcon')
      flag = 1
    if "MenuPid" in HttpRequest.POST:
      MenuPid = int(HttpRequest.POST['MenuPid'])
    else:
      msglist.append('ERROR : Menu Parent not found or No value is selected for Parent')
      flag = 1
    if flag == 1:
      HttpRequest.session[SESSION_MESSAGE] = msglist
      return HttpResponseRedirect('/message/')
    else:
      MenuFnxObj = MenuFnx()
      result = MenuFnxObj.Insert(MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,int(details['userid']),HttpRequest.META['REMOTE_ADDR'])
      HttpRequest.session[SESSION_MESSAGE] = [str(result)]
      return HttpResponseRedirect('/user/menu/list')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: Could not login user. ' + str(msg))
      return HttpResponseRedirect('/message/')
    
def EditMenu(HttpRequest,MenuId):
  msglist = AppendMessageList(HttpRequest)
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    msglist.append('Please Login to continue')
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/user/login/')
  try:
    pass
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: Could not login user. ' + str(msg))
      return HttpResponseRedirect('/message/')
    
def Delete(HttpRequest,MenuId):
  msglist = AppendMessageList(HttpRequest)
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    msglist.append('Please Login to continue')
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/user/login/')
  try:
    pass
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: Could not login user. ' + str(msg))
      return HttpResponseRedirect('/message/')
