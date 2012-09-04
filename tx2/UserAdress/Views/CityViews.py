from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import LoggerAdress
from tx2.UserAdress.BusinessFunctions.CityFunctions import CityFnx
from django.contrib import messages
import logging
import inspect

AdressLogger = logging.getLogger(LoggerAdress)

def CityIndex(HttpRequest):
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    CityFnxObj = CityFnx()
    CityList = CityFnxObj.getAllCities()
    if CityList[0] != 1:
      messages.error(HttpRequest,"ERROR " + str(CityList[1]))
      return HttpResponseRedirect('/message/')
    else:
      return render_to_response("Adress/EditCity.html",{'CityList':CityList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')


def CityAdd(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    CityName = ''
    if 'CityName' in HttpRequest.POST:
      CityName = HttpRequest.POST['CityName']
      CityFnxObj = CityFnx()
      res = CityFnxObj.Add(CityName,int(logindetails["userid"]),ip)
      if( res[0] == 1):
        messages.error(HttpRequest,"City : %s has been sucessfully added to database" % (CityName))
      else:
        messages.error(HttpRequest,"ERROR: " + str(res[1]))
    else:
      messages.error(HttpRequest,"Error. No city name found in request.")
    return HttpResponseRedirect('/adress/city/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
