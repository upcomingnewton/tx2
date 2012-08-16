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
import logging
import datetime


LoggerUser = logging.getLogger(LoggerUser)
ExceptionMessage = 'ERROR : System has suffered some error while processing your request. Please try after some-time. If the problem persists, contact system administrators.'



    
    
def log_in(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
  usrfn = UserFnx()
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    email = ''
    password = ''
    if 'LoginUser_email' in HttpRequest.POST.keys():
      email = HttpRequest.POST['LoginUser_email']
    else:
      msglist.append('email required')
    if 'LoginUser_pass' in HttpRequest.POST.keys():
      password = HttpRequest.POST['LoginUser_pass']
    if( len(password) < 4):
      msglist.append('proper password required')
    if len(msglist) > 0:
      HttpRequest.session[SESSION_MESSAGE] = msglist
      return HttpResponseRedirect('/user/login/')
    else:
      res = usrfn.LoginUser(email, password,Login_From_Type, ip)
      if ( res[0] == 1):
        result = res[1]
        if( result['result'] == 1):
          usrfn.RegisterUserForForums(email, password)
            
          encdec = Encrypt()
          token = {"userid":result['userid'],"groupid":result['groupid'],"loginid":encdec.encrypt( str(result['loginid'])),
"fname":result['username']}
          HttpRequest.session["details"] = token
          HttpRequest.session.set_expiry(0)
          return HttpResponseRedirect('/userprofile/UserProfile/StudentDetails/')
        else:
          msglist.append(res[1])
          HttpRequest.session[SESSION_MESSAGE] = msglist
          return HttpResponseRedirect('/message/')
      else:
        msglist.append(res[1])
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
  except Exception, ex:
        LoggerUser.exception('log_in')
        HttpRequest.session[SESSION_MESSAGE] = ['ERROR' + str(ex)]
        return HttpResponseRedirect('/message/')
                
        
def log_out(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  msglist = AppendMessageList(HttpRequest)
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
          return HttpResponseRedirect('/user/login/')
        else:
          msglist.append(res[1])
          HttpRequest.session[SESSION_MESSAGE] = msglist
          return HttpResponseRedirect('/message/')
      else:
        msglist.append(res[1])
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
    else:
      msglist.append("Please login in first , for loggging out")
      HttpRequest.session[SESSION_MESSAGE] = msglist
      return HttpResponseRedirect('/user/login/')
  except Exception, ex:
      LoggerUser.exception('log_in')
      HttpRequest.session[SESSION_MESSAGE] = ['ERROR' + str(ex)]
      return HttpResponseRedirect('/message/')

    
#@never_cache
def CreateUserFromSite(HttpRequest):  
  msglist = []
  flag = 0
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  by = getSystemUser_DaemonCreateUser()
  if( details['userid'] != -1):
    by = int(details['userid'])
  try:
    email = HttpRequest.POST['RegisterUser_email']
    if len(email) < 4:
      msglist.append('email required')
      flag = 1
    pass1 = HttpRequest.POST['RegisterUser_pass']
    if len(pass1) < 4 or len(pass1) > 10:
      msglist.append('password should be between 4 to 10 characters')
      flag = 1
    pass2 = HttpRequest.POST['RegisterUser_pass2']
    if pass1 != pass2:
      msglist.append('passwords do not match ')
      flag = 1
    fname = HttpRequest.POST['RegisterUser_fname']
    if len(fname) < 2:
      msglist.append('first name required')
      flag = 1
    mname = HttpRequest.POST['RegisterUser_mname']
    if len(mname) < 2 or mname == "":
      mname = "--"
    lname = HttpRequest.POST['RegisterUser_lname']
    if len(lname) < 4:
      msglist.append('last name required')
      flag = 1
    bday = HttpRequest.POST['RegisterUser_dob']
    if len(bday) < 10:
      msglist.append('birth date required')
      flag = 1
    bday = bday.split('/')
    try:
      bday = datetime.date(int(bday[2]),int(bday[0]),int(bday[1]))
    except ValueError as err:
      msglist.append('Invalid Birthdate, '+ err.message)
    gender = HttpRequest.POST['RegisterUser_gender']
    if gender== "-1" :
      msglist.append('Please select your gender')
    if ( flag == 1 ):
      HttpRequest.session[SESSION_MESSAGE] = msglist
      return HttpResponseRedirect('/message/')
    else:
      insfnx = UserFnx()
      res = insfnx.InsertUser(email, pass2, fname, mname, lname, gender, bday,getSystemEntity(),getSystemGroup_NewUsers(),by,ip)
      msglist.append(res[1])
      HttpRequest.session[SESSION_MESSAGE] = msglist
      return HttpResponseRedirect('/message/')
  except Exception, ex:
      LoggerUser.exception('log_in')
      HttpRequest.session[SESSION_MESSAGE] = ['ERROR' + str(ex)]
      return HttpResponseRedirect('/message/')

def AuthenticateUserFromEmail(HttpRequest,token,refs):
  au_user = UserFnx()
  ip = HttpRequest.META['REMOTE_ADDR']
  msglist = []
  try:
    res = au_user.AuthenticateUserFromSite(token, ip)
    msglist.append(res[1])
    HttpRequest.session[SESSION_MESSAGE] = msglist
    if( res[0] == 1):
      return HttpResponseRedirect('/user/login/')
    else:
      return HttpResponseRedirect('/message/')
  except Exception, ex:
      LoggerUser.exception('log_in')
      HttpRequest.session[SESSION_MESSAGE] = ['ERROR' + str(ex)]
      return HttpResponseRedirect('/message/')

def CheckAndlogout(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
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
        else:
          msglist.append(res[1])
          HttpRequest.session[SESSION_MESSAGE] = msglist
      else:
        msglist.append(res[1])
        HttpRequest.session[SESSION_MESSAGE] = msglist
    else:
      pass
    return msglist
  except:
    LoggerUser.exception('CheckAndlogout')
    HttpRequest.session[SESSION_MESSAGE] = ['ERROR' + str(ex)]
    return []


def view_dashboard(HttpRequest):
  msglist = AppendMessageList(HttpRequest)
  details = GetLoginDetails(HttpRequest)
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    if "details" in HttpRequest.session:
      if( details['userid'] == -1):
        msglist.append('Please Login.')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/user/login/')
      return render_to_response('UserSystem/User/home.html',{"details":str(HttpRequest.session["details"]), 'msglist':msglist},context_instance=RequestContext(HttpRequest))
    else:
      return HttpResponseRedirect('/user/login/')
  except Exception, ex:
      LoggerUser.exception('log_in')
      HttpRequest.session[SESSION_MESSAGE] = ['ERROR' + str(ex)]
      return HttpResponseRedirect('/message/')
        
        


def ChangePass(HttpRequest):
  msglist = []
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    msglist.append('Please Login to continue')
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/user/login/')
  try:
    HttpRequest.session[SESSION_MESSAGE] = msglist
    flag = -1
    oldpass = ''
    newpass = ''
    if 'OldPassword' in HttpRequest.POST:
      oldpass = HttpRequest.POST['OldPassword']
    else:
      flag = 1
      msglist.append('old password required')
    if 'NewPassword1' in HttpRequest.POST:
      newpass = HttpRequest.POST['NewPassword1']
    else:
      flag = 1
      msglist.append('new password required')
    if flag == 1:
      HttpRequest.session[SESSION_MESSAGE] = msglist
      return HttpResponseRedirect('/user/password/change/')
    else:
      UserObj = UserFnx()
      res = UserObj.ChangePassword(oldpass,newpass,int(details['userid']),ip,int(details['userid']),-1)
      msglist.append(res[1])
      HttpRequest.session[SESSION_MESSAGE] = msglist
      return HttpResponseRedirect('/message/')
  except Exception, ex:
      LoggerUser.exception('log_in')
      HttpRequest.session[SESSION_MESSAGE] = ['ERROR' + str(ex)]
      return HttpResponseRedirect('/message/')
	
def ResetPass(HttpRequest):
  msglist = []
  ip = HttpRequest.META['REMOTE_ADDR']
  try:
    HttpRequest.session[SESSION_MESSAGE] = []
    if 'ResetPasswordEmail' in HttpRequest.POST:
      emailid = HttpRequest.POST['ResetPasswordEmail']
      UserObj = UserFnx()
      obj = UserObj.getUserObjectByEmailid(emailid)
      if obj[0] is not 1:
        msglist.append(obj[1])
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
      else:
        details = GetLoginDetails(HttpRequest)
        if( details['userid'] != -1):
          by = int(details['userid'])
        else:
          by = int(obj[1].id)
        res = UserObj.ForgetPassword(emailid,by,ip)
        msglist.append(res[1])
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
    else:
      msglist.append('email required')
      HttpRequest.session[SESSION_MESSAGE] = msglist
      return render_to_response("UserSystem/User/ResetPassword.html",{},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      LoggerUser.exception('log_in')
      HttpRequest.session[SESSION_MESSAGE] = ['ERROR' + str(ex)]
      return HttpResponseRedirect('/message/')
        


from django.contrib.auth.models import User



