from tx2.Misc.Encryption import Encrypt
from tx2.Users.DBFunctions.DatabaseFunctions import DBLoginUser ,DBLogoutUser,DBInsertUser,DBUpdateUser
from tx2.Users.DBFunctions.DBMessages import decode
from tx2.Users.HelperFunctions.LoginDetails import AddLoginIdToLoggedInUsersDict, ClearLoginIdFromLoggedInUsersDict 
from tx2.Users.HelperFunctions.DefaultValues import *
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
from tx2.conf.LocalProjectConfig import *
from tx2.Users.models import *
from tx2.Misc.CacheManagement import setCache,getCache
#from cPickle import dumps, loads 
from tx2.CONFIG import LoggerUser
import logging
from tx2.Misc.Email import sendMail



class UserFnx():
  def  __init__(self):
    self.encrypt = Encrypt()
    self.UserLogger = logging.getLogger(LoggerUser)
    self.ExceptionMessage = "Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon"
    
    
  def RegisterUserForForums(self,email,password):
    try:
      import httplib, urllib, urllib2
      url =   "http://forum.thoughtxplore.com/signup_TX"
      params = {'user':email,'pass':password,'email':email}
      data = urllib.urlencode(params)
      req = urllib2.Request(url,data)
      req.add_header("Content-type", "application/x-www-form-urlencoded")
      res = urllib2.urlopen(req).read()
      self.UserLogger.debug("FORUMS REG - %s , %s"%(email,str(res)))
      return 1
    except:
      self.UserLogger.exception("FORUMS REG")
      return -2
    
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
      if ( result['result'] == 1):
        msg = "Your profile has been sucessfully created.Please check your email for activation link."
        self.send_mail_test(email,result['rescode'],fname,ip)
        res = self.RegisterUserForForums(email,password)
        if( res == 1 ):
          msg += "You have also been registered for forums. User your placement site credentials for login."
        return (1,msg)
      else:
        return (-1,decode(result[1])) 
    except:
      exception_log = ('[%s] %s,%s')%('InsertUserFromSite',ip,email)
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)
      
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
    except:
      exception_log = ('[%s] %s')%('UpdateUser',ip)
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)
      
  def AuthenticateUserFromSite(self,emailid,ip,op=SYSTEM_PERMISSION_UPDATE):
    try:
      to_emailid = self.encrypt.decrypt(emailid)
      s = to_emailid.split('___')
      userid = int(s[0])
      user_obj = User.objects.get(id=userid)
      if( user_obj is None ):
        msg = 'ERROR. User does not exist'
        self.UserLogger.exception(msg)
        return (-2,msg + ' ' + self.ExceptionMessage)
      groupid = getSystemGroup_EmailAU()
      #SYSTEM_DAEMON_USERAU_USER_GROUP
      if( groupid == -1):
        self.UserLogger.exception('Error at HelperFunctions, getSystemGroup_EmailAU. It returned -1')
        return (-2,self.ExceptionMessage)
      user_obj.Group.id = groupid
      result = self.UpdateUser(user_obj,'UserAuthenticationByEmail','UserAuthenticationByEmail',user_obj.id,ip,op)
      if result[0] == 1 :
        return (1,"Your profile has been sucessfully activated.You can login now") 
      elif result[0] == -2:
        return (-2,'error in authenticating user')
      elif result[0] == -1:
        return (-1,decode(result[1]))
    except:
      exception_log = ('[%s] %s,%s')%('AuthenticateUserFromSite',ip,emailid)
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)

  def LoginUser(self,email,password,_type,ip):
    try:
      self.UserLogger.debug('%s:%s'%(email,password))
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
    except:
      exception_log = ('[%s] %s,%s %s %s')%('LoginUser',ip,email,_type,self.encrypt.encrypt(password))
      self.UserLogger.exception(exception_log)
      return (-2, self.ExceptionMessage)

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
        return (-1,decode(result[1]))
    except:
      exception_log = ('[%s] %s')%('LogoutUser',loginid)
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)
    
  def ChangeUserGroup(self,userid,GroupName,by,ip,op=SYSTEM_PERMISSION_UPDATE):
    try:
      user_obj = self.getUserObjectByUserId(userid)
      GroupFnxObj = GroupFnx()
      groupobj = GroupFnxObj.getGroupByName(GroupName)
      if groupobj is not 1:
        self.UserLogger.exception('[%s] Error, group is not valid',('ChangeUserGroup'))
        return (-1,self.ExceptionMessage)
      groupobj = groupobj[1]
      PreviousGroup = user_obj.Group.id
      user_obj.Group = groupobj
      result = self.UpdateUser(self,user_obj,'ChangeUserGroup',str(PreviousGroup),by,ip,op)
      if result[0] == 1 :
        return (1,"Group Change Sucessful") 
      elif result[0] == -2:
        return (-2,'Error in Changing Group')
      elif result[0] == -1:
        return (-1,decode(result[1]))
    except:
      exception_log = ('[%s] %s %s')%('ChangeUserGroup',userid,GroupName)
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)

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
        return (-1,'ERROR: User Does not exists')
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
        return (-2,'Error in Changing Password')
      elif result[0] == -1:
        return (-1,decode(result[1]))
    except:
        self.UserLogger.exception("ChangePassword")
        return (-2,self.ExceptionMessage)
            
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
        return (-1,decode(result[1]))
    except:
        self.UserLogger.exception("ChangePassword")
        return (-2,self.ExceptionMessage)

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
    except:
      pass
      
  def send_email_forget_pass(self,email,password):
    try:
      import time
      refs = int(time.time())
      token= "password reset for " + email + " new password is " + str(password) 
      sendMail([ "thoughtxplore@gmail.com",email],"no-reply@thoughtxplore.com","authenticate",token)
    except:
      pass

  def getAllUsers(self):
    try:
      UsersList =  User.objects.all()
      return (1,UsersList)
    except:
      exception_log = ('[%s]')%('getAllUsers')
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)

  def getUserObjectByEmailid(self,emailid):
    try:
      UserObj = User.objects.get(UserEmail=emailid)
      if  UserObj is None:
        return (-1,'ERROR : User Does not exist')
      else:
        return (1,UserObj)
    except:
      exception_log = ('[%s] emailid =  %s')%('getUserObjectByEmailid',emailid)
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)

  def getUserObjectByUserId(self,UserId):
    try:
      UserObj = User.objects.get(id=UserId)
      if  UserObj is None:
        return (-1,'ERROR : User Does not exist')
      else:
        return (1,UserObj)
    except:
      exception_log = ('[%s] UserId =  %d')%('getUserObjectByUserId',UserId)
      self.UserLogger.exception(exception_log)
      return (-2,self.ExceptionMessage)

    
