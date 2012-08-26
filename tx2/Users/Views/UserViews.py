# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.BusinessFunctions.UserFunctions import UserFnx
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity,getSystemGroup_NewUsers, getSystemUser_DaemonCreateUser
from tx2.Misc.Encryption import Encrypt
from tx2.CONFIG import LoggerUser,SESSION_MESSAGE,Login_From_Type,LogOut_From_Type
from django.contrib import messages
import logging
import datetime
import inspect


LoggerUser = logging.getLogger(LoggerUser)




    
def Login(HttpRequest):
  usrfn = UserFnx()
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    email = ''
    password = ''
    flag = 0
    if 'LoginUser_email' in HttpRequest.POST.keys():
      email = HttpRequest.POST['LoginUser_email']
    else:
      messages.error(HttpRequest,'ERROR : Email required for logging in.')
      flag = 1
    #TODO check if this is a valid email id or not
    if 'LoginUser_pass' in HttpRequest.POST.keys():
      password = HttpRequest.POST['LoginUser_pass']
    else:
      messages.error(HttpRequest,'ERROR : Password required for logging in.')
      flag = 1
    if( len(password) < 4):
      messages.error(HttpRequest,'ERROR : Minimum password length should be 4.')
      flag = 1
    if flag is 1:
      return HttpResponseRedirect('/user/login/')
    else:
      res = usrfn.LoginUser(email, password,Login_From_Type, ip)
      if ( res[0] == 1):
        result = res[1]
        if( result['result'] == 1):
          encdec = Encrypt()
          token = {"userid":result['userid'],"groupid":result['groupid'],"loginid":encdec.encrypt( str(result['loginid'])),
"fname":result['username']}
          HttpRequest.session["details"] = token
          return HttpResponseRedirect('/user/dashboard/')
        else:
          messages.error(HttpRequest,res[1])
          return HttpResponseRedirect('/message/')
      else:
        messages.error(HttpRequest,res[1])
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
                
        
def log_out(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    if "details" in HttpRequest.session.keys():
      token = HttpRequest.session['details']
      logout_user = UserFnx()
      res =  logout_user.LogoutUser(token['loginid'],2)
      if ( res[0] == 1):
        result = res[1]
        if( result['result'] == 1):
          for sesskey in HttpRequest.session.keys():
            del HttpRequest.session[sesskey]
          messages.error(HttpRequest,'You have been logged out sucessfully')
          return HttpResponseRedirect('/user/login/')
        else:
          messages.error(HttpRequest,res[1])
          return HttpResponseRedirect('/message/')
      else:
        messages.error(HttpRequest,res[1])
        return HttpResponseRedirect('/message/')
    else:
      messages.error(HttpRequest,'Invalid request.')
      return HttpResponseRedirect('/user/login/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

    
#@never_cache
def CreateUserFromSite(HttpRequest):  
  flag = 0
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  by = getSystemUser_DaemonCreateUser()
  if( details['userid'] != -1):
    by = int(details['userid'])
  try:
    email = HttpRequest.POST['RegisterUser_email']
    if len(email) < 4:
      messages.error(HttpRequest,'email required')
      flag = 1
    pass1 = HttpRequest.POST['RegisterUser_pass']
    if len(pass1) < 4 or len(pass1) > 10:
      messages.error(HttpRequest,'password should be between 4 to 10 characters')
      flag = 1
    pass2 = HttpRequest.POST['RegisterUser_pass2']
    if pass1 != pass2:
      messages.error(HttpRequest,'passwords do not match ')
      flag = 1
    fname = HttpRequest.POST['RegisterUser_fname']
    if len(fname) < 2:
      messages.error(HttpRequest,'first name required')
      flag = 1
    mname = HttpRequest.POST['RegisterUser_mname']
    if len(mname) < 2 or mname == "":
      mname = "--"
    lname = HttpRequest.POST['RegisterUser_lname']
    if len(lname) < 4:
      messages.error(HttpRequest,'last name required')
      flag = 1
    RegisterUser_dob_date = HttpRequest.POST['RegisterUser_dob_date']
    RegisterUser_dob_month = HttpRequest.POST['RegisterUser_dob_month']
    RegisterUser_dob_year = HttpRequest.POST['RegisterUser_dob_year']
    try:
      bday = datetime.date(int(RegisterUser_dob_year),int(RegisterUser_dob_month),int(RegisterUser_dob_date))
    except ValueError as err:
      messages.error(HttpRequest,'Invalid Birthdate')
    gender = HttpRequest.POST['RegisterUser_gender']
    if gender== "-1" :
      messages.error(HttpRequest,'Please select your gender')
    if ( flag == 1 ):
      return HttpResponseRedirect('/message/')
    else:
      insfnx = UserFnx()
      res = insfnx.InsertUser(email, pass2, fname, mname, lname, gender, bday,getSystemEntity(),getSystemGroup_NewUsers(),by,ip)
      messages.error(HttpRequest,res[1])
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

def AuthenticateUserFromEmail(HttpRequest,token,refs):
  au_user = UserFnx()
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    res = au_user.AuthenticateUserFromSite(token, ip)
    messages.error(HttpRequest,res[1])
    if( res[0] == 1):
      return HttpResponseRedirect('/user/login/')
    else:
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

def CheckAndlogout(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    if "details" in HttpRequest.session.keys():
      token = HttpRequest.session['details']
      logout_user = UserFnx()
      res =  logout_user.LogoutUser(token['loginid'],-9)
      if ( res[0] == 1):
        result = res[0]
        if( result['result'] == 1):
          for sesskey in HttpRequest.session.keys():
            del HttpRequest.session[sesskey]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return []


def view_dashboard(HttpRequest):
  details = GetLoginDetails(HttpRequest)
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    if "details" in HttpRequest.session:
      if( details['userid'] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        HttpResponseRedirect('/user/login/')
      return render_to_response('UserSystem/User/home.html',{"details":str(HttpRequest.session["details"])},context_instance=RequestContext(HttpRequest))
    else:
      return HttpResponseRedirect('/user/login/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')


def ChangePass(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    flag = -1
    oldpass = ''
    newpass = ''
    if 'OldPassword' in HttpRequest.POST:
      oldpass = HttpRequest.POST['OldPassword']
    else:
      flag = 1
      messages.error(HttpRequest,'Please enter your old password.')
    if 'NewPassword1' in HttpRequest.POST:
      newpass = HttpRequest.POST['NewPassword1']
    else:
      flag = 1
      messages.error(HttpRequest,'Please enter new password')
    if flag == 1:
      return HttpResponseRedirect('/user/password/change/')
    else:
      UserObj = UserFnx()
      res = UserObj.ChangePassword(oldpass,newpass,int(details['userid']),ip,int(details['userid']),-1)
      messages.error(HttpRequest,res[1])
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
	
def ResetPass(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    if 'ResetPasswordEmail' in HttpRequest.POST:
      emailid = HttpRequest.POST['ResetPasswordEmail']
      UserObj = UserFnx()
      obj = UserObj.getUserObjectByEmailid(emailid)
      if obj[0] is not 1:
        messages.error(HttpRequest,obj[1])
        return HttpResponseRedirect('/message/')
      else:
        details = GetLoginDetails(HttpRequest)
        if( details['userid'] != -1):
          by = int(details['userid'])
        else:
          by = int(obj[1].id)
        res = UserObj.ForgetPassword(emailid,by,ip)
        messages.error(HttpRequest,res[1])
        return HttpResponseRedirect('/message/')
    else:
      messages.error(HttpRequest,'Please enter valid email id.')
      return HttpResponseRedirect('/user/password/reset/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
