from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.Views.UserViews import CheckAndlogout
from tx2.Users.BusinessFunctions.UserFunctions import UserFnx
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity,getSystemGroup_NewUsers, getSystemUser_DaemonCreateUser
from tx2.Misc.Encryption import Encrypt
from tx2.CONFIG import AlumniLogger
from django.contrib import messages
import logging
import inspect

AlmLogger = logging.getLogger(AlumniLogger)

def RegisterIndex(HttpRequest):
  try:
    return render_to_response('alumni/RegisterAlumni.html',{},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AlmLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def Register(HttpRequest):
  try:
    EmailID = ''
    Password1 = ''
    Password2 = ''
    FirstName = ''
    MiddleName = ''
    LastName = ''
    Gender = ''
    DateofBirthDay = ''
    DateofBirthYear = ''
    DateofBirthMonth = ''
    DateofBirth = ''
    Batch = ''
    Branch = ''
    RollNO = ''
    flag = False
    if 'EmailID' in HttpRequest.POST:
      EmailID = HttpRequest.POST['EmailID']
    else:
      messages.error(HttpRequest,'Proper Email Required.')
      flag = True
    if len(EmailID) < 4:
      messages.error(HttpRequest,'Proper Email Required.')
      flag = True

    if 'Password1' in HttpRequest.POST:
      Password1 = HttpRequest.POST['Password1']
    else:
      messages.error(HttpRequest,'Proper Password Required.')
      flag = True
    if len(Password1) < 4:
      messages.error(HttpRequest,'Proper should be between 4 to 10 characters.')
      flag = True
      
    if 'Password2' in HttpRequest.POST:
      Password2 = HttpRequest.POST['Password2']
    else:
      messages.error(HttpRequest,'Confirmation of Password Required.')
      flag = True
    if len(Password) < 4:
      messages.error(HttpRequest,'Passwords do not match.')
      flag = True

    if Password1 != Password2:
      flag = True
      messages.error(HttpRequest,'Passwords do not match.')

    if 'FirstName' in HttpRequest.POST:
      FirstName = HttpRequest.POST['FirstName']
    else:
      messages.error(HttpRequest,'Proper First Name Required.')
      flag = True
    if len(FirstName) < 4:
      messages.error(HttpRequest,'Proper First Name Required.')
      flag = True
      
    if 'MiddleName' in HttpRequest.POST:
      MiddleName = HttpRequest.POST['MiddleName']
    else:
      MiddleName = ''

    if 'LastName' in HttpRequest.POST:
      LastName = HttpRequest.POST['LastName']
    else:
      messages.error(HttpRequest,'Proper LastName Required.')
      flag = True
    if len(LastName) < 4:
      messages.error(HttpRequest,'Proper LastName Required.')
      flag = True
      
    if 'RollNO' in HttpRequest.POST:
      RollNO = HttpRequest.POST['RollNO']
    else:
      messages.error(HttpRequest,'Proper RollNO Required.')
      flag = True
    if len(RollNO) < 4:
      messages.error(HttpRequest,'Proper RollNO Required.')
      flag = True

    if 'Gender' in HttpRequest.POST:
      Gender = HttpRequest.POST['Gender']
    else:
      messages.error(HttpRequest,'Please select your gender.')
      flag = True
    if Gender == -1:
      messages.error(HttpRequest,'Please select your gender.')
      flag = True
      
    if 'Batch' in HttpRequest.POST:
      Batch = HttpRequest.POST['Batch']
    else:
      messages.error(HttpRequest,'Please select your Batch.')
      flag = True
    if Batch == -1:
      messages.error(HttpRequest,'Please select your Batch.')
      flag = True
      
    if 'Branch' in HttpRequest.POST:
      Branch = HttpRequest.POST['Branch']
    else:
      messages.error(HttpRequest,'Please select your Branch.')
      flag = True
    if Branch == -1:
      messages.error(HttpRequest,'Please select your Branch.')
      flag = True
      
    if 'DateofBirthDay' in HttpRequest.POST:
      DateofBirthDay = HttpRequest.POST['DateofBirthDay']
    else:
      messages.error(HttpRequest,'Please select your BirthDay.')
      flag = True
    if DateofBirthDay == -1:
      messages.error(HttpRequest,'Please select your BirthDay.')
      flag = True
      
    if 'DateofBirthMonth' in HttpRequest.POST:
      DateofBirthMonth = HttpRequest.POST['DateofBirthMonth']
    else:
      messages.error(HttpRequest,'Please select your BirthMonth.')
      flag = True
    if DateofBirthMonth == -1:
      messages.error(HttpRequest,'Please select your BirthMonth.')
      flag = True

    if 'DateofBirthYear' in HttpRequest.POST:
      DateofBirthYear = HttpRequest.POST['DateofBirthYear']
    else:
      messages.error(HttpRequest,'Please select your BirthYear.')
      flag = True
    if DateofBirthYear == -1:
      messages.error(HttpRequest,'Please select your BirthYear.')
      flag = True

  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AlmLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
