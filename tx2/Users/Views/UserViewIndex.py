from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.Views.UserViews import CheckAndlogout
from tx2.CONFIG import LoggerUser, SESSION_MESSAGE
import logging


LoggerUser = logging.getLogger(LoggerUser)
ExceptionMessage = 'ERROR : System has suffered some error while processing your request. Please try after some-time. If the problem persists, contact system administrators.'

def LoginIndex(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    mlist = CheckAndlogout(HttpRequest)
    msglist += mlist
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return render_to_response("UserSystem/User/Login.html",{},context_instance=RequestContext(HttpRequest))
  except:
    LoggerUser.exception('LoginIndex')
    msglist.append(ExceptionMessage)
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/message/')
    
def CreateUserIndex(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return render_to_response('UserSystem/User/Register.html',{},context_instance=RequestContext(HttpRequest))
  except:
    LoggerUser.exception('CreateUserIndex')
    HttpRequest.session[SESSION_MESSAGE] = [ExceptionMessage]
    return HttpResponseRedirect('/message/')
    
def ChangePassIndex(HttpRequest):
  msglist = []
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    msglist.append('Please Login to continue')
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/user/login/')
  try:
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return render_to_response("UserSystem/User/ChangePass.html",{},context_instance=RequestContext(HttpRequest))
  except:
    LoggerUser.exception('ChangePassIndex')
    msglist.append(ExceptionMessage)
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/message/')
	
def ResetPasswordIndex(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] != -1):
    CheckAndlogout(HttpRequest)
  try:
    HttpRequest.session[SESSION_MESSAGE] = []
    return render_to_response("UserSystem/User/ResetPassword.html",{},context_instance=RequestContext(HttpRequest))
  except:
    LoggerUser.exception('ResetPasswordIndex')
    msglist.append(ExceptionMessage)
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/message/')
    
def ResendAuthenticationEmailIndex(HttpRequest)
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] != -1):
    CheckAndlogout(HttpRequest)
  try:
    HttpRequest.session[SESSION_MESSAGE] = []
    return render_to_response("UserSystem/User/ResendAuthenticationEmail.html",{},context_instance=RequestContext(HttpRequest))
  except:
    LoggerUser.exception('ResendAuthenticationEmailIndex')
    msglist.append(ExceptionMessage)
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/message/')

################################ SHOW MESSAGE FUNCTION ##############################

def ShowMessages(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return render_to_response("UserSystem/User/message.html",{},context_instance=RequestContext(HttpRequest))
