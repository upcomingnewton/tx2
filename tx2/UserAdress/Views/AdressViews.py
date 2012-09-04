from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import LoggerAdress
from tx2.UserAdress.BusinessFunctions.AdressFunctions import AdressFnx
from tx2.UserAdress.BusinessFunctions.CityFunctions import CityFnx
from tx2.UserAdress.BusinessFunctions.StateFunctions import StateFnx
from tx2.UserAdress.BusinessFunctions.CountryFunctions import CountryFnx
from django.contrib import messages
import logging
import inspect

AdressLogger = logging.getLogger(LoggerAdress)

def AdressIndex(HttpRequest):
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
      CityFnxObj = CityFnx()
      StateFnxObj = StateFnx()
      CountryFnxObj = CountryFnx()
      CityList = CityFnxObj.getAllCities()
      StateList = StateFnxObj.getAllStates()
      CountryList = CountryFnxObj.getAllCountries()
      if CityList[0] != 1:
        messages.error(HttpRequest,"ERROR " + str(CityList[1]))
        return HttpResponseRedirect('/message/')
      if StateList[0] != 1:
        messages.error(HttpRequest,"ERROR " + str(StateList[1]))
        return HttpResponseRedirect('/message/')
      if CountryList[0] != 1:
        messages.error(HttpRequest,"ERROR " + str(CountryList[1]))
        return HttpResponseRedirect('/message/')
      if 'AdressObjIDSession' in HttpRequest.session.keys():
        AdressObjID = HttpRequest.session['AdressObjIDSession']
        objid1 = AdressObjID['Permanent']
        objid2 = AdressObjID['Present']
        AdressFnxObj = AdressFnx()
        obj1 = AdressFnxObj.getAdressObjById(objid1)
        obj2 = AdressFnxObj.getAdressObjById(objid2)
        if obj1[0] != 1:
          messages.error(HttpRequest,"ERROR " + str(obj1[1]))
          return HttpResponseRedirect('/message/')
        if obj2[0] != 1:
          messages.error(HttpRequest,"ERROR " + str(obj2[1]))
          return HttpResponseRedirect('/message/')
       # del HttpRequest.session['AdressObjIDSession'] TODO
        return render_to_response("Adress/EditAdress.html",{'Permanent':obj1[1],'Present':obj2[1],'CityList':CityList[1],'StateList':StateList[1],'CountryList':CountryList[1]},context_instance=RequestContext(HttpRequest))
      else:
        return render_to_response("Adress/EditAdress.html",{'Permanent':'Null','Present':'Null','CityList':CityList[1],'StateList':StateList[1],'CountryList':CountryList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def AddAdress(HttpRequest):
  logindetails = GetLoginDetails(HttpRequest)
  ip = HttpRequest.META['REMOTE_ADDR']
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
        AdressFnxObj = AdressFnx()
        #  Permanent adress
        PermanentAdressNo = ''
        PermanentStreetAdress1 = ''
        PermanentStreetAdress2 = ''
        PermanentCity = ''
        PermanentState = ''
        PermanentCountry = ''
        PermanentPinCode = ''
        if 'PermanentAdressNo' in HttpRequest.POST:
          PermanentAdressNo = HttpRequest.POST['PermanentAdressNo']
        else:
          PermanentAdressNo = 'NA'
        if 'PermanentStreetAdress1' in HttpRequest.POST:
          PermanentStreetAdress1 = HttpRequest.POST['PermanentStreetAdress1']
        else:
          PermanentStreetAdress1 = 'NA'
        if 'PermanentStreetAdress2' in HttpRequest.POST:
          PermanentStreetAdress2 = HttpRequest.POST['PermanentStreetAdress2']
        else:
          PermanentStreetAdress2 = 'NA'
        if 'PermanentCity' in HttpRequest.POST:
          PermanentCity = int(HttpRequest.POST['PermanentCity'])
        else:
          messages.error("Please select some value for Permanent city adress")
          return HttpResponseRedirect('/message/')
        if 'PermanentState' in HttpRequest.POST:
          PermanentState = int(HttpRequest.POST['PermanentState'])
        else:
          messages.error("Please select some value for  Permanent state adress")
          return HttpResponseRedirect('/message/')
        if 'PermanentCountry' in HttpRequest.POST:
          PermanentCountry = int(HttpRequest.POST['PermanentCountry'])
        else:
          messages.error("Please select some value for Permanent country adress")
          return HttpResponseRedirect('/message/')
        if 'PermanentPinCode' in HttpRequest.POST:
          PermanentPinCode = HttpRequest.POST['PermanentPinCode']
        else:
          PermanentPinCode = 'NA'
        # present adress
        PresentAdressNo = ''
        PresentStreetAdress1 = ''
        PresentStreetAdress2 = ''
        PresentCity = ''
        PresentState = ''
        PresentCountry = ''
        PresentPinCode = ''
        if 'PresentAdressNo' in HttpRequest.POST:
          PresentAdressNo = HttpRequest.POST['PresentAdressNo']
        else:
          PresentAdressNo = 'NA'
        if 'PresentStreetAdress1' in HttpRequest.POST:
          PresentStreetAdress1 = HttpRequest.POST['PresentStreetAdress1']
        else:
          PresentStreetAdress1 = 'NA'
        if 'PresentStreetAdress2' in HttpRequest.POST:
          PresentStreetAdress2 = HttpRequest.POST['PresentStreetAdress2']
        else:
          PresentStreetAdress2 = 'NA'
        if 'PresentCity' in HttpRequest.POST:
          PresentCity = int(HttpRequest.POST['PresentCity'])
        else:
          messages.error("Please select some value for Present city'")
          return HttpResponseRedirect('/message/')
        if 'PresentState' in HttpRequest.POST:
          PresentState = int(HttpRequest.POST['PresentState'])
        else:
          messages.error("Please select some value for Present state")
          return HttpResponseRedirect('/message/')
        if 'PresentCountry' in HttpRequest.POST:
          PresentCountry = int(HttpRequest.POST['PresentCountry'])
        else:
          messages.error("Please select some value for Present country")
          return HttpResponseRedirect('/message/')
        if 'PresentPinCode' in HttpRequest.POST:
          PresentPinCode = HttpRequest.POST['PresentPinCode']
        else:
          PresentPinCode = 'NA'
        PermanentAdressResult = AdressFnxObj.Add(PermanentAdressNo,PermanentStreetAdress1,PermanentStreetAdress2,PermanentCity,PermanentState,PermanentCountry,PermanentPinCode,int(logindetails["userid"]),ip)
        PresentAdressResult = AdressFnxObj.Add(PresentAdressNo,PresentStreetAdress1,PresentStreetAdress2,PresentCity,PresentState,PresentCountry,PresentPinCode,int(logindetails["userid"]),ip)
        adressId = {}
        if  PermanentAdressResult[0] == 1:
          adressId['Permanent'] =  PermanentAdressResult[1]
          messages.error(HttpRequest,'Your  Permanent adress has been sucessfully updated.')
        else:
          adressId['Permanent'] = -1
          messages.error(HttpRequest,str( PermanentAdressResult[1]))
        if PresentAdressResult[0] == 1:
          adressId['Present'] = PresentAdressResult[1]
          messages.error(HttpRequest,'Your present adress has been sucessfully updated.')
        else:
          adressId['Present'] = -1
          messages.error(HttpRequest,str(PresentAdressResult[1]))
        HttpRequest.session['AdressObjIDSession'] = adressId
        return HttpResponseRedirect('/adress/contactinfo/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def EditAdress(HttpRequest):
  logindetails = GetLoginDetails(HttpRequest)
  ip = HttpRequest.META['REMOTE_ADDR']
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
      if 'AdressObjIDSession' in HttpRequest.session.keys():
        AdressObjID = HttpRequest.session['AdressObjIDSession']
        objid1 = AdressObjID['Permanent']
        objid2 = AdressObjID['Present']
        AdressFnxObj = AdressFnx()
        #  Permanent adress
        PermanentAdressNo = ''
        PermanentStreetAdress1 = ''
        PermanentStreetAdress2 = ''
        PermanentCity = ''
        PermanentState = ''
        PermanentCountry = ''
        PermanentPinCode = ''
        if 'PermanentAdressNo' in HttpRequest.POST:
          PermanentAdressNo = HttpRequest.POST['PermanentAdressNo']
        else:
          PermanentAdressNo = 'NA'
        if 'PermanentStreetAdress1' in HttpRequest.POST:
          PermanentStreetAdress1 = HttpRequest.POST['PermanentStreetAdress1']
        else:
          PermanentStreetAdress1 = 'NA'
        if 'PermanentStreetAdress2' in HttpRequest.POST:
          PermanentStreetAdress2 = HttpRequest.POST['PermanentStreetAdress2']
        else:
          PermanentStreetAdress2 = 'NA'
        if 'PermanentCity' in HttpRequest.POST:
          PermanentCity = int(HttpRequest.POST['PermanentCity'])
        else:
          messages.error("Please select some value for Permanent city adress")
          return HttpResponseRedirect('/message/')
        if 'PermanentState' in HttpRequest.POST:
          PermanentState = int(HttpRequest.POST['PermanentState'])
        else:
          messages.error("Please select some value for  Permanent state adress")
          return HttpResponseRedirect('/message/')
        if 'PermanentCountry' in HttpRequest.POST:
          PermanentCountry = int(HttpRequest.POST['PermanentCountry'])
        else:
          messages.error("Please select some value for Permanent country adress")
          return HttpResponseRedirect('/message/')
        if 'PermanentPinCode' in HttpRequest.POST:
          PermanentPinCode = HttpRequest.POST['PermanentPinCode']
        else:
          PermanentPinCode = 'NA'
        # present adress
        PresentAdressNo = ''
        PresentStreetAdress1 = ''
        PresentStreetAdress2 = ''
        PresentCity = ''
        PresentState = ''
        PresentCountry = ''
        PresentPinCode = ''
        if 'PresentAdressNo' in HttpRequest.POST:
          PresentAdressNo = HttpRequest.POST['PresentAdressNo']
        else:
          PresentAdressNo = 'NA'
        if 'PresentStreetAdress1' in HttpRequest.POST:
          PresentStreetAdress1 = HttpRequest.POST['PresentStreetAdress1']
        else:
          PresentStreetAdress1 = 'NA'
        if 'PresentStreetAdress2' in HttpRequest.POST:
          PresentStreetAdress2 = HttpRequest.POST['PresentStreetAdress2']
        else:
          PresentStreetAdress2 = 'NA'
        if 'PresentCity' in HttpRequest.POST:
          PresentCity = int(HttpRequest.POST['PresentCity'])
        else:
          messages.error("Please select some value for Present city'")
          return HttpResponseRedirect('/message/')
        if 'PresentState' in HttpRequest.POST:
          PresentState = int(HttpRequest.POST['PresentState'])
        else:
          messages.error("Please select some value for Present state")
          return HttpResponseRedirect('/message/')
        if 'PresentCountry' in HttpRequest.POST:
          PresentCountry = int(HttpRequest.POST['PresentCountry'])
        else:
          messages.error("Please select some value for Present country")
          return HttpResponseRedirect('/message/')
        if 'PresentPinCode' in HttpRequest.POST:
          PresentPinCode = HttpRequest.POST['PresentPinCode']
        else:
          PresentPinCode = 'NA'
        PermanentAdressResult = AdressFnxObj.Update(int(objid1),PermanentAdressNo,PermanentStreetAdress1,PermanentStreetAdress2,PermanentCity,PermanentState,PermanentCountry,PermanentPinCode,int(logindetails["userid"]),ip)
        PresentAdressResult = AdressFnxObj.Update(int(objid2),PresentAdressNo,PresentStreetAdress1,PresentStreetAdress2,PresentCity,PresentState,PresentCountry,PresentPinCode,int(logindetails["userid"]),ip)
        adressId = {}
        if  PermanentAdressResult[0] == 1:
          adressId[' Permanent'] =  PermanentAdressResult[1]
          messages.error(HttpRequest,'Your  Permanent adress has been sucessfully updated.')
        else:
          adressId[' Permanent'] = -1
          messages.error(HttpRequest,str( PermanentAdressResult[1]))
        if PresentAdressResult[0] == 1:
          adressId['Present'] = PresentAdressResult[1]
          messages.error(HttpRequest,'Your present adress has been sucessfully updated.')
        else:
          adressId['Present'] = -1
          messages.error(HttpRequest,str(PresentAdressResult[1]))
        HttpRequest.session['AdressObjIDSession'] = adressId
        return HttpResponseRedirect('/adress/contactinfo/')
      else:
        messages.error(HttpRequest,"Error occured while updating your adress records.Your session has expired.Please try again.")
        return HttpResponseRedirect('/message/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
