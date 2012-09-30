# Create your views here.
import urls
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.ShowAllUrlsInDjango import MakeAllUrls
from tx2.Users.BusinessFunctions.MenuFunctions import MenuFnx
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity,getSystemGroup_NewUsers, getSystemUser_DaemonCreateUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_DELETE, SYSTEM_PERMISSION_INSERT, SYSTEM_PERMISSION_UPDATE
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
      messages.error(HttpRequest,"Error. %s" % (MenuList[1])) 
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
      
def ListDeletedMenu(HttpRequest):
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,"Error.Please login to continue.")
    return HttpResponseRedirect('/user/login/')
  try:
    MenuObj = MenuFnx()
    MenuList = MenuObj.getDeletedMenuObj()
    if MenuList[0] == 1:
      return render_to_response('UserSystem/Menu/ListDeletedMenu.html',{"MenuList":MenuList[1]},context_instance=RequestContext(HttpRequest))
    else:
      messages.error(HttpRequest,"Error. %s" % (MenuList[1])) 
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
    
def AddMenuIndex(HttpRequest):
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    MenuObj = MenuFnx()
    ParentMenuList = MenuObj.getParentMenu()
    MenuUrlList = []
    MakeAllUrls('/',urls.urlpatterns,MenuUrlList, depth=0)
    if ParentMenuList[0] == 1:
      return render_to_response('UserSystem/Menu/AddMenu.html',{"ParentMenuList":ParentMenuList[1],'MenuUrlList':MenuUrlList},context_instance=RequestContext(HttpRequest))
    else:
      messages.error(HttpRequest,ParentMenuList[1])
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
    
def EditMenuIndex(HttpRequest,MenuId):
  print '==== EditMenuIndex ==== ' +  str(MenuId)
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    MenuObj = MenuFnx()
    MenuObject = MenuObj.getMenuObjByMenuId(int(MenuId))
    if MenuObject[0] == 1:
      MenuObj = MenuFnx()
      ParentMenuList = MenuObj.getParentMenu()
      MenuUrlList = []
      MakeAllUrls('/',urls.urlpatterns,MenuUrlList, depth=0)
      return render_to_response('UserSystem/Menu/EditMenu.html',{"MenuObj":MenuObject[1],"ParentMenuList":ParentMenuList[1],'MenuUrlList':MenuUrlList},context_instance=RequestContext(HttpRequest))
    else:
      messages.error(HttpRequest,MenuObject[1])
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

      
def DeleteMenuIndex(HttpRequest,MenuId):
  print '==== EditMenuIndex ==== ' +  str(MenuId)
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    return HttpResponseRedirect('/user/menu/delete/' + str(MenuId) + '/post/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def ActivateMenuIndex(HttpRequest,MenuId):
  print '==== EditMenuIndex ==== ' +  str(MenuId)
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    return HttpResponseRedirect('/user/menu/activate/' + str(MenuId) + '/post/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

    
# CB FNX

def AddMenu(HttpRequest):
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    flag = 0
    MenuName = ''
    MenuDesc = ''
    MenuUrl = ''
    MenuUrl1 = ''
    MenuUrl2 = ''
    MenuPid = ''
    MenuIcon = ''
    if "MenuName" in HttpRequest.POST and len(HttpRequest.POST['MenuName']) > 0:
      MenuName = HttpRequest.POST['MenuName']
    else:
      messages.error(HttpRequest,'ERROR : MenuName not found or No value is entered for Menu Name')
      flag = 1
    if "MenuDesc" in HttpRequest.POST and len(HttpRequest.POST['MenuDesc']) > 0:
      MenuDesc = HttpRequest.POST['MenuDesc']
    else:
      messages.error(HttpRequest,'ERROR : MenuDesc not found or No value is entered for MenuDesc')
      flag = 1
    if "MenuUrlInput" in HttpRequest.POST:
      MenuUrl = HttpRequest.POST['MenuUrlInput']
    else:
      messages.error(HttpRequest,'ERROR : MenuUrl not found or Improper value is entered for MenuUrl')
      flag = 1
    if "MenuIcon" in HttpRequest.POST and len(HttpRequest.POST['MenuIcon']) > 0:
      MenuIcon = HttpRequest.POST['MenuIcon']
    else:
      messages.error(HttpRequest,'ERROR : MenuIcon not found or No value is entered for MenuIcon')
      flag = 1
    if "MenuPid" in HttpRequest.POST:
      MenuPid = int(HttpRequest.POST['MenuPid'])
    else:
      messages.error(HttpRequest,'ERROR : Menu Parent not found or No value is selected for Parent')
      flag = 1
    if flag == 1:
      return HttpResponseRedirect('/message/')
    else:
      MenuFnxObj = MenuFnx()
      if MenuPid == -1:
        MenuUrl = MenuName
      result = MenuFnxObj.Insert(MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,int(details['userid']),HttpRequest.META['REMOTE_ADDR'])
      messages.error(HttpRequest,str(result))
      return HttpResponseRedirect('/user/menu/add/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
    
def EditMenu(HttpRequest,MenuId):
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
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
      messages.error(HttpRequest,'ERROR : MenuName not found or No value is entered for Menu Name')
      flag = 1
    if "MenuDesc" in HttpRequest.POST and len(HttpRequest.POST['MenuDesc']) > 0:
      MenuDesc = HttpRequest.POST['MenuDesc']
    else:
      messages.error(HttpRequest,'ERROR : MenuDesc not found or No value is entered for MenuDesc')
      flag = 1
    if "MenuUrlInput" in HttpRequest.POST:
      MenuUrl = HttpRequest.POST['MenuUrlInput']
    else:
      messages.error(HttpRequest,'ERROR : MenuUrl not found or Improper value is entered for MenuUrl')
      flag = 1
    if "MenuIcon" in HttpRequest.POST and len(HttpRequest.POST['MenuIcon']) > 0:
      MenuIcon = HttpRequest.POST['MenuIcon']
    else:
      messages.error(HttpRequest,'ERROR : MenuIcon not found or No value is entered for MenuIcon')
      flag = 1
    if "MenuPid" in HttpRequest.POST:
      MenuPid = int(HttpRequest.POST['MenuPid'])
    else:
      messages.error(HttpRequest,'ERROR : Menu Parent not found or No value is selected for Parent')
      flag = 1
    if "LogDesc" in HttpRequest.POST:
      LogDesc = (HttpRequest.POST['LogDesc'])
    else:
      messages.error(HttpRequest,'ERROR : LogDesc not found or No value is entered for LogDesc')
      flag = 1
    if flag == 1:
      return HttpResponseRedirect('/message/')
    else:
      MenuFnxObj = MenuFnx()
      result = MenuFnxObj.Update(int(MenuId),MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,int(details['userid']),HttpRequest.META['REMOTE_ADDR'],LogDesc)
      messages.error(HttpRequest,str(result))
      return HttpResponseRedirect('/user/menu/list')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
    
def Delete(HttpRequest,MenuId):
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    MenuObj = MenuFnx()
    MenuObject = MenuObj.getMenuObjByMenuId(int(MenuId))
    if MenuObject[0] == 1:
      MenuObject = MenuObject[1]
      result = MenuObj.Update(int(MenuId),MenuObject.MenuName,MenuObject.MenuDesc,MenuObject.MenuUrl,MenuObject.MenuPid,MenuObject.MenuIcon,int(details['userid']),HttpRequest.META['REMOTE_ADDR'],'Delete',RequestedOperation=SYSTEM_PERMISSION_DELETE)
      messages.error(HttpRequest,str(result))
      return HttpResponseRedirect('/user/menu/list')
    else:
      messages.error(HttpRequest,MenuObject[1])
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
      
def Activate(HttpRequest,MenuId):
  LoggerUser.debug("== ACTIVATE FUNCTION, MENUID = %d",int(MenuId))
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    MenuObj = MenuFnx()
    MenuObject = MenuObj.getDeletedMenuObjByMenuId(int(MenuId))
    if MenuObject[0] == 1:
      MenuObject = MenuObject[1]
      print " ** I HAVE GOT THE MENU OBJECT " + MenuObject.MenuName
      result = MenuObj.Update(int(MenuId),MenuObject.MenuName,MenuObject.MenuDesc,MenuObject.MenuUrl,MenuObject.MenuPid,MenuObject.MenuIcon,int(details['userid']),HttpRequest.META['REMOTE_ADDR'],'ReActivation',RequestedOperation=SYSTEM_PERMISSION_UPDATE)
      messages.error(HttpRequest,str(result))
      return HttpResponseRedirect('/user/menu/list')
    else:
      messages.error(HttpRequest,MenuObject[1])
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
