from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import LoggerAdress
from tx2.UserAdress.BusinessFunctions.CountryFunctions import CountryFnx
from django.contrib import messages
import logging
import inspect

AdressLogger = logging.getLogger(LoggerAdress)

def CountryIndex(HttpRequest):
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    CountryFnxObj = CountryFnx()
    CountryList = CountryFnxObj.getAllCountries()
    if CountryList[0] != 1: 
      messages.error(HttpRequest,"ERROR " + str(CountryList[1]))
      return HttpResponseRedirect('/message/')
    else:
      return render_to_response("Adress/EditCountry.html",{'CountryList':CountryList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')


def CountryAdd(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    CountryName = ''
    if 'CountryName' in HttpRequest.POST:
      CountryName = HttpRequest.POST['CountryName']
      CountryFnxObj = CountryFnx()
      res = CountryFnxObj.Add(CountryName,int(logindetails["userid"]),ip)
      if( res[0] == 1):
        messages.error(HttpRequest,"Country : %s has been sucessfully added to database" % (CountryName))
      else:
        messages.error(HttpRequest,"ERROR: " + str(res[1]))
    else:
      messages.error(HttpRequest,"Error. No Country name found in request.")
    return HttpResponseRedirect('/adress/country/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
