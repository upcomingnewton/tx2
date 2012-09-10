from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import LoggerAdress
from tx2.UserAdress.BusinessFunctions.AdressFunctions import AdressFnx
from tx2.UserAdress.BusinessFunctions.UserContactInfoFunctions import UserContactInfoFnx
from tx2.UserAdress.models import UserContactInfo
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import logging
import inspect

AdressLogger = logging.getLogger(LoggerAdress)

def AddDummyContactInfo(HttpRequest,userid):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    if 'AdressObjIDSession' in HttpRequest.session.keys():
      AdressObjID = HttpRequest.session['AdressObjIDSession']
      objid1 = AdressObjID['Permanent']
      objid2 = AdressObjID['Present']
      del HttpRequest.session['AdressObjIDSession']
      if objid1 != -1 and objid2 != -1:
        UserContactInfoFnxobj = UserContactInfoFnx()
        res = UserContactInfoFnxobj.Initialise(userid,int(objid1),int(objid2),int(logindetails["userid"]),ip)
        if( res[0] == 1):
          return HttpResponseRedirect('/adress/contactinfo/')
        else:
          messages.error(HttpRequest,'Error : ' + str(res[1]))
          return HttpResponseRedirect('/message/')
      else:
        messages.error(HttpRequest,'Error While updating adress records')
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

def ContactInfoIndex(HttpRequest,UserID):
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    Userid = UserID
    if Userid == -1:
      Userid = int(logindetails['userid'])
    UserContactInfoFnxobj = UserContactInfoFnx()
    p = UserContactInfoFnxobj.getUserContactInfoByUserId(Userid)
    print str(p)
    if p[0] == -1:
      # does not exist
      if 'AdressObjIDSession' in HttpRequest.session.keys():
        # add a dummy adress
        return AddDummyContactInfo(HttpRequest,Userid)
      else:
        return HttpResponseRedirect('/adress/adress/')
    elif p[0] == 1:
      p = p[1]
      PermanentAdressId = p.ParmanentAdress
      PresentAdressId = p.PresentAdress
      print '==' + str(PermanentAdressId) + ' == '  + str(PresentAdressId)
      AdressFnxObj = AdressFnx()
      PermanentAdress = AdressFnxObj.getAdressObjById(PermanentAdressId)
      PresentAdress = AdressFnxObj.getAdressObjById(PresentAdressId)
      HttpRequest.session['AdressObjIDSession'] = {'Permanent': PermanentAdressId,'Present':PresentAdressId}
      if  PermanentAdress[0] == 1:
         PermanentAdress =  PermanentAdress[1]
      else:
         PermanentAdress = -1
      if PresentAdress[0] == 1:
        PresentAdress = PresentAdress[1]
      else:
        PresentAdress = -1
      return render_to_response("Adress/EditContactInfo.html",{'UserContactInfo':p,'PermanentAdress':PermanentAdress,'PresentAdress':PresentAdress,'User_ID':Userid},context_instance=RequestContext(HttpRequest))
    else:
      messages.error(HttpRequest,"ERROR : " + str(p[1]))
      return HttpResponseRedirect('/message/')
      # exists
#  1. check if there some entry or not 
#  2. if yes, get values and display
#  3. if no, redirect the add adress page
#  4. user will add values
#  5. AdressObjIDSession will be set to adresses
#  6. add a dummy contactinfo
#  7. repeat step 1
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def ContactInfoEdit(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
      messages.error(HttpRequest,'Please Login to continue')
      return HttpResponseRedirect('/user/login/')
  try:
    if 'AdressObjIDSession' in HttpRequest.session.keys():
      AdressObjID = HttpRequest.session['AdressObjIDSession']
      PermanentAdressObjID = AdressObjID['Permanent']
      PresentAdressObjID = AdressObjID['Present']
      del HttpRequest.session['AdressObjIDSession']
      UserID = int(logindetails["userid"])
      MobileNo = 'Null'
      AltEmail = 'Null'
      FatherName = 'Null'
      FatherContactNo = 'Null'
      MotherName = 'Null'
      MotherContactNo = 'Null'
      if 'MobileNo' in HttpRequest.POST:
        MobileNo = HttpRequest.POST['MobileNo']
      if 'AltEmail' in HttpRequest.POST:
        AltEmail = HttpRequest.POST['AltEmail']
      if 'FatherName' in HttpRequest.POST:
        FatherName = HttpRequest.POST['FatherName']
      if 'FatherContactNo' in HttpRequest.POST:
        FatherContactNo = HttpRequest.POST['FatherContactNo']
      if 'MotherName' in HttpRequest.POST:
        MotherName = HttpRequest.POST['MotherName']
      if 'MotherContactNo' in HttpRequest.POST:
        MotherContactNo = HttpRequest.POST['MotherContactNo']
      UserContactInfoObj = UserContactInfoFnx()
      res = UserContactInfoObj.Update(UserID,MobileNo,AltEmail,FatherName,FatherContactNo,MotherName,MotherContactNo,PermanentAdressObjID,PresentAdressObjID,int(logindetails["userid"]),ip)
      if res[0] == 1:
        messages.error(HttpRequest,"Sucess, your details have been sucessfully updated.")
      else:
        messages.error(HttpRequest,"ERROR. " + str(res[1]))
      return HttpResponseRedirect('/adress/contactinfo/')
    else:
      messages.error(HttpRequest,'ERROR. No session is set for this request. Please repoert this error.')
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
