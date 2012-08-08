from tx2.Misc.Encryption import Encrypt
from tx2.Users.DBFunctions.DatabaseFunctions import DBLoginUser ,DBLogoutUser,DBInsertUser,DBUpdateUser
from tx2.Users.DBFunctions.Messages import decode
from tx2.Users.HelperFunctions.LoginDetails import AddLoginIdToLoggedInUsersDict, ClearLoginIdFromLoggedInUsersDict 
from tx2.Users.HelperFunctions.DefaultValues import *
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
from tx2.conf.LocalProjectConfig import *
from tx2.Users.models import *
from tx2.Misc.CacheManagement import setCache,getCache
from tx2.CONFIG import LoggerUser
import logging
from tx2.Misc.Email import sendMail
import urllib



class UserFnx():
  def  __init__(self):
    self.encrypt = Encrypt()
    self.UserLogger = logging.getLogger(LoggerUser)
    self.ExceptionMessage = "Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon"
  def MakeExceptionMessage(self,msg):
    return 'Exception Generated : ' + str(msg) + ' Administrators have been alerted to rectify the error. We will send you a notification in this regard soon.'
    
    
  def fetch_url(self,url,params):
      params=urllib.urlencode(params)
      f = urllib.urlopen(url+"?"+params)
      return (f.read(), f.code)
    
  def RegisterUserForForums(self,email,password, secret):
    
    import httplib, urllib, urllib2
    url =   "http://forum.thoughtxplore.com/signup_TX"
    secret== 'A2lx135sVzm$803A88'
    params = {'user':email,'pass':password,'email':email, 'secret':secret}
    [content, response_code] = self.fetch_url(url, params)
    self.UserLogger.debug("FORUMS REG - %s , %s"%(email,str(response_code)))
    if(response_code==200):
      return (1, "User has been successfully registered for forums")
    else:
      self.UserLogger.exception('RegisterUserForForums')
      return (-2,self.MakeExceptionMessage(str(response_code)))
    
  def InsertUser(self,email,password,fname,mname,lname,gender,bday,entity,group,by,ip,op=SYSTEM_PERMISSION_INSERT):
    try:
      user = {'email':email, 
              'pass':self.encrypt.encrypt(password),
              'fname':fname,
              'lname':lname,
              'mname':mname,
              'gender':gender,
              'bday':str(bday), #date
              'entity':entity,
              'group':group,
              'op':op,
              'by':by,
              'ip':ip
              }
      result = DBInsertUser(user)
      if ( result['result'] == 1 or result['result'] == 2):
        msg = "Your profile has been sucessfully created.Please check your email for activation link."
        self.send_mail_test(email,result['rescode'],fname,ip)
        res = self.RegisterUserForForums(email,password)
        if( res[0] == 1 ):
          msg += "You have also been registered for forums. User your placement site credentials for login."
        return (1,msg)
      else:
        return (-1,decode(result)) 
    except Exception, ex:
      self.UserLogger.exception('InsertUser')
      return (-2,self.MakeExceptionMessage(str(ex)))
      
  def UpdateUser(self,user_obj,_LogsDesc,_PreviousState,by,ip,op=SYSTEM_PERMISSION_UPDATE):
    try:
      details = {
        'email':user_obj.UserEmail,
        'pass':user_obj.UserPassword,
        'bday':str(user_obj.UserBirthDate),
        'fname':user_obj.UserFirstName,
        'mname':user_obj.UserMiddleName,
        'lname':user_obj.UserLastName,
        'entity':user_obj.UserEntity.id,
        'gender':user_obj.UserGender,
        'LogsDesc':_LogsDesc,
        'PreviousState':_PreviousState,
        'group':user_obj.Group.id,
        'op':op,
        'by':by,
        'ip':ip,
        }
      result = DBUpdateUser(details)
      if (result['result'] == 1 and result['rescode'] == 99):
        return (1,result)
      else:
        return (-1,result)
    except Exception, ex:
      self.UserLogger.exception('UpdateUser')
      return (-2,self.MakeExceptionMessage(str(ex)))
      
  def AuthenticateUserFromSite(self,emailid,ip,op=SYSTEM_PERMISSION_UPDATE):
    try:
      to_emailid = self.encrypt.decrypt(emailid)
      s = to_emailid.split('___')
      userid = int(s[0])
      user_obj = self.getUserObjectByUserId(userid)
      if( user_obj[0] is not 1 ):
        return (-2,'ERROR : ' + user_obj[1])
      user_obj = user_obj[1]
      groupid = getSystemGroup_EmailAU()
      #SYSTEM_DAEMON_USERAU_USER_GROUP
      if( groupid == -1):
        self.UserLogger.exception('Error at HelperFunctions, getSystemGroup_EmailAU. It returned -1')
        return (-2,self.ExceptionMessage)
      if user_obj.Group.id == groupid:
        return (1,'Your profile has been sucessfully activated.You can login now.')
      user_obj.Group.id = groupid
      result = self.UpdateUser(user_obj,'UserAuthenticationByEmail','UserAuthenticationByEmail',user_obj.id,ip,op)
      if result[0] == 1 :
        return (1,"Your profile has been sucessfully activated.You can login now") 
      elif result[0] == -2:
        return (-2,result[1])
      elif result[0] == -1:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('AuthenticateUserFromSite')
      return (-2,self.MakeExceptionMessage(str(ex)))

  def LoginUser(self,email,password,_type,ip):
    try:
      details = { 'email':email,
                  'pass':self.encrypt.encrypt(password),
                  'login_type':_type,
                  'ip':ip,
                }
      result = DBLoginUser(details)
      if( int(result['result']) >= 1):
        AddLoginIdToLoggedInUsersDict(self.encrypt.encrypt(str(result['loginid'])))
        return(1,result)
      else:
        return(-1,self.ExceptionMessage )
    except Exception, ex:
      self.UserLogger.exception('LoginUser')
      return (-2,self.MakeExceptionMessage(str(ex)))

  def LogoutUser(self,loginid,out_from):
    try:
      details = {'loginid':self.encrypt.decrypt(loginid),
                 'logout_from':out_from,
                }
      result = DBLogoutUser(details)
      if (result['result'] == 1 ):
        ClearLoginIdFromLoggedInUsersDict(self.encrypt.encrypt(str(details['loginid'])))
        return (1,result)
      else:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('LogoutUser')
      return (-2,self.MakeExceptionMessage(str(ex)))
    
  def ChangeUserGroup(self,userid,GroupName,by,ip,op=SYSTEM_PERMISSION_UPDATE):
    try:
      user_obj = self.getUserObjectByUserId(userid)
      if( user_obj[0] is not 1 ):
        return (-2,'ERROR : ' + user_obj[1])
      user_obj = user_obj[1]
      GroupFnxObj = GroupFnx()
      groupobj = GroupFnxObj.getGroupObjectByName(GroupName)
      if( groupobj[0] is not 1 ):
        return (-2,'ERROR : ' + groupobj[1])
      groupobj = groupobj[1]
      if user_obj.Group.id == groupobj.id:
        return (1,'Group has been updated sucessfully.')
      PreviousGroup = user_obj.Group.id
      user_obj.Group = groupobj
      result = self.UpdateUser(user_obj,'ChangeUserGroup',str(PreviousGroup),by,ip,op)
      if result[0] == 1 :
        return (1,"Group Change Sucessful") 
      elif result[0] == -2:
        return (-2,result[1])
      elif result[0] == -1:
        return (-1,decode(result[1]))
    except Exception, ex:
      self.UserLogger.exception('UpdateUser')
      return (-2,self.MakeExceptionMessage(str(ex)))

    # do not send encrypted passes
  def ChangePassword(self,oldpass,newpass,by,ip,userid,emailid,op=SYSTEM_PERMISSION_UPDATE):
    try:
      if len(oldpass) < 4 or len(newpass) < 4:
        return (-1,'ERROR: Length of password should be atleast 4 characters.')
      oldpass = self.encrypt.encrypt(oldpass)
      newpass = self.encrypt.encrypt(newpass)
      if userid == -1 and emailid == -1:
        return (-1,'ERROR: No information passed to identify user')
      user_obj = User()
      if userid is not -1:
        user_obj = self.getUserObjectByUserId(userid)
      else:
        user_obj = self.getUserObjectByEmailid(emailid)
      if user_obj[0] is not 1:
        return (-2,'ERROR : ' + user_obj[1])
      user_obj = user_obj[1]
      if user_obj.UserPassword != oldpass:
        return (-1,'ERROR: Old Pasword does not match')
      if user_obj.UserPassword == newpass:
        # NO NEED TO CHANGE, IT IS ALREADY SAME
        return (1,"SUCESS.Your password has been changed sucessfully.")
      PreviousState = "{oldpass:"+ oldpass + "}"
      LogsDesc = 'Changed Password'
      user_obj.UserPassword = newpass
      result = self.UpdateUser(user_obj,LogsDesc,PreviousState,by,ip,op)
      if result[0] == 1 :
        return (1,"SUCESS.Your password has been changed sucessfully.") 
      elif result[0] == -2:
        return (-2,result[1])
      elif result[0] == -1:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('ChangePassword')
      return (-2,self.MakeExceptionMessage(str(ex)))
            
  def ForgetPassword(self,emailid,by,ip,op=SYSTEM_PERMISSION_UPDATE):
    try:
      user_obj = User()
      user_obj = self.getUserObjectByEmailid(emailid)
      if user_obj[0] is not 1:
        return (-1,'ERROR: User Does not exists')
      user_obj = user_obj[1]
      if by == -1:
        by = user_obj.id
      PreviousState = "{oldpass:"+ user_obj.UserPassword + "}"
      LogsDesc = 'Forget Password'
      import random
      password = str(random.randint(100000,999999))
      user_obj.UserPassword = self.encrypt.encrypt(password)
      #UpdateUser(self,user_obj,_LogsDesc,_PreviousState,by,ip,op=SYSTEM_PERMISSION_UPDATE):
      result = self.UpdateUser(user_obj,LogsDesc,PreviousState,by,ip,op)
      if result[0] == 1 :
        self.send_email_forget_pass(emailid,password)
        return (1,"SUCESS.Your password has been changed sucessfully.") 
      elif result[0] == -2:
        return (-2,'Error in Changing Password')
      elif result[0] == -1:
        return (-1,decode(result))
    except Exception, ex:
      self.UserLogger.exception('ForgetPassword')
      return (-2,self.MakeExceptionMessage(str(ex)))

  def send_mail_test(self,email,userid,fname,ip):
    try:
      token= self.encrypt.encrypt(str(userid) + '___' + email)
      import time
      refs = int(time.time())
      msg = "hey " + fname + "\n"
      msg += "Please click on following link to activate your account \n\n"
      msg += "http://uiet.thoughtxplore.com/user/authenticate/email/"+token+"/" + str(refs) + "/"
      msg += "\n\nRegards \n Training and Placement Cell, UIET"
      sendMail([ "thoughtxplore@gmail.com",email],"no-reply@thoughtxplore.com","Training and Placement Cell, UIET",msg)
    except Exception, ex:
      self.UserLogger.exception('send_mail_test')
      return (-2,self.MakeExceptionMessage(str(ex)))
      
  def send_email_forget_pass(self,email,password):
    try:
      import time
      refs = int(time.time())
      token= "password reset for " + email + " new password is " + str(password) 
      sendMail([ "thoughtxplore@gmail.com",email],"no-reply@thoughtxplore.com","Password Reset",token)
    except Exception, ex:
      self.UserLogger.exception('send_email_forget_pass')
      return (-2,self.MakeExceptionMessage(str(ex)))

  def getAllUsers(self):
    try:
      UsersList =  User.objects.all()
      return (1,UsersList)
    except Exception, ex:
      self.UserLogger.exception('getAllUsers')
      return (-2,self.MakeExceptionMessage(str(ex)))

  def getUserObjectByEmailid(self,emailid):
    try:
      UserObj = User.objects.get(UserEmail=emailid)
      if  UserObj is None:
        return (-1,'ERROR : User Does not exist')
      else:
        return (1,UserObj)
    except ObjectDoesNotExist:
      return (-1,'ERROR : User Does not exist')
    except Exception, ex:
      self.UserLogger.exception('getUserObjectByEmailid')
      return (-2,self.MakeExceptionMessage(str(ex)))


  def getUserObjectByUserId(self,UserId):
    try:
      UserObj = User.objects.get(id=UserId)
      if  UserObj is None:
        return (-1,'ERROR : User Does not exist')
      else:
        return (1,UserObj)
    except ObjectDoesNotExist:
      return (-1,'ERROR : User Does not exist')
    except Exception, ex:
      self.UserLogger.exception('getUserObjectByUserId')
      return (-2,self.MakeExceptionMessage(str(ex)))

    
