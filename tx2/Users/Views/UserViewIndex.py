from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.Views.UserViews import CheckAndlogout
from tx2.CONFIG import LoggerUser, SESSION_MESSAGE
from django.contrib.messages import constants as messages
import logging
import inspect


LoggerUser = logging.getLogger(LoggerUser)
ExceptionMessage = 'ERROR : System has suffered some error while processing your request. Please try after some-time. If the problem persists, contact system administrators.'

def LoginIndex(HttpRequest):
  try:
    # check if user is already logged in or not
    # if user is already logged in, then redirect it to home page 
    # and generate an error that user needs to log out to log in again
    if "details" in HttpRequest.session.keys():
      return HttpResponseRedirect('/user/dashboard/')
      messages.warning(HttpRequest, 'You are already logged in.')
    return render_to_response('UserSystem/login.html',{},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: Could not load login page. ' + str(msg))
      return HttpResponseRedirect('/message/')
    
def CreateUserIndex(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    HttpRequest.session[SESSION_MESSAGE] = msglist 
    return render_to_response('TXtemplates/UserSystem/User/Register.html',{},context_instance=RequestContext(HttpRequest))
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
    return render_to_response("TXtemplates/UserSystem/User/ChangePass.html",{},context_instance=RequestContext(HttpRequest))
  except:
    LoggerUser.exception('ChangePassIndex')
    msglist.append(ExceptionMessage)
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/message/')
	
def ResetPasswordIndex(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] != -1):
    CheckAndlogout(HttpRequest)
  try:
    HttpRequest.session[SESSION_MESSAGE] = []
    return render_to_response("TXtemplates/UserSystem/User/ResetPassword.html",{},context_instance=RequestContext(HttpRequest))
  except:
    LoggerUser.exception('ResetPasswordIndex')
    msglist.append(ExceptionMessage)
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/message/')
    
def ResendAuthenticationEmailIndex(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
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
    return render_to_response('TXtemplates/index.html',{},context_instance=RequestContext(HttpRequest))
