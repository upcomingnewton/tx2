from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.Views.UserViews import CheckAndlogout
from tx2.CONFIG import LoggerUser, SESSION_MESSAGE
from django.contrib import messages
import logging
import inspect


LoggerUser = logging.getLogger(LoggerUser)


def LoginIndex(HttpRequest):
  try:
    # check if user is already logged in or not
    # if user is already logged in, then redirect it to home page 
    # and generate an error that user needs to log out to log in again
    if "details" in HttpRequest.session.keys():
      return HttpResponseRedirect('/user/dashboard/')
      messages.error(HttpRequest, 'You are already logged in.')
    return render_to_response('UserSystem/User/Login.html',{},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
    
def CreateUserIndex(HttpRequest):
  try:
    return render_to_response('UserSystem/User/Register.html',{},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
    
def ChangePassIndex(HttpRequest):
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    return render_to_response("UserSystem/User/ChangePass.html",{},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
	
def ResetPasswordIndex(HttpRequest):
  try:
    return render_to_response("UserSystem/User/ResetPassword.html",{},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
    
def ResendAuthenticationEmailIndex(HttpRequest):
  try:
    return render_to_response("UserSystem/User/ResendAuthenticationEmail.html",{},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

################################ SHOW MESSAGE FUNCTION ##############################

def ShowMessages(HttpRequest):
    return render_to_response('Message.html',{},context_instance=RequestContext(HttpRequest))
