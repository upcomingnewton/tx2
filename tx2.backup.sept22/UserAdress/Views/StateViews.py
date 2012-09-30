from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import LoggerAdress
from tx2.UserAdress.BusinessFunctions.StateFunctions import StateFnx
from django.contrib import messages
import logging
import inspect

AdressLogger = logging.getLogger(LoggerAdress)

def StateIndex(HttpRequest):
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    StateFnxObj = StateFnx()
    StateList = StateFnxObj.getAllStates()
    if StateList[0] != 1:
      messages.error(HttpRequest,"ERROR " + str(StateList[1]))
      return HttpResponseRedirect('/message/')
    else:
      return render_to_response("Adress/EditState.html",{'StateList':StateList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')


def StateAdd(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    StateName = ''
    if 'StateName' in HttpRequest.POST:
      StateName = HttpRequest.POST['StateName']
      StateFnxObj = StateFnx()
      res = StateFnxObj.Add(StateName,int(logindetails["userid"]),ip)
      if( res[0] == 1):
        messages.error(HttpRequest,"State : %s has been sucessfully added to database" % (StateName))
      else:
        messages.error(HttpRequest,"ERROR: " + str(res[1]))
    else:
      messages.error(HttpRequest,"Error. No state name found in request.")
    return HttpResponseRedirect('/adress/state/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
