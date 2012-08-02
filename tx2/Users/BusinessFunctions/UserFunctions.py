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
      res=urllib2.urlopen(req).read()
      self.UserLogger.debug("FORUMS REG - %s , %s"%(email,str(res)))
      return 1
    except:
      self.UserLogger.exception("FORUMS REG - %s , %s"%(email,str(res)))
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
        res = self.RegisterUserForForums(self,email,password)
        if( res == 1 ):
          msg += "You have also been registered for forums. User your placement site credentials for login."
        return (1,msg)
      else:
        return (-1,decode(result)) 
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
      
  def AuthenticateUserFromSite(self,emailid,ip):
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
      result = self.UpdateUser(self,user_obj,'UserAuthenticationByEmail','UserAuthenticationByEmail',by,ip,op)
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
        return(-1, decode(result) + self.ExceptionMessage )
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
        return (-1,decode(result))
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
        return (-1,self.ExceptionMessage)
    
    
    def ResetPass(self,password,user_obj,_LogsDesc,_PreviousState,by,ip,op=SYSTEM_PERMISSION_UPDATE):
    	try:
            details = {
                       'email':user_obj.UserEmail,
                       'pass':password,
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
            self.UserLogger.debug('result = %s' % (result))
            return (1,result)
        except:
            exception_log = ('[%s] %s')%('ResetPass',ip)
            self.UserLogger.exception(exception_log)
            return (-1,'error in ResetPass')
    
    
    # do not send encrypted passes
    def ChangePassword(self,oldpass,newpass,by,ip,userid=-1,op=SYSTEM_PERMISSION_UPDATE):
    	try:
    		if len(oldpass) < 4 or len(newpass) < 4:
    			self.UserLogger.debug('Error, length less than 4 oldpass = %s, newpass = %s, ip = %s , userid = %d' % (oldpass,newpass,ip,userid))
    			return (-1,'ERROR: Length of password should be atleast 4')
    		oldpass = self.encrypt.encrypt(oldpass)
    		newpass = self.encrypt.encrypt(newpass)
    		user_obj = User()
    		if userid == -1:
    			self.UserLogger.debug('Error, no userid or emailid provided oldpass = %s, newpass = %s, ip = %s , userid = %d' % (oldpass,newpass,ip,userid))
    			return (-1,'ERROR: either pass userid or emailid')
    		user_obj = User.objects.get(id=userid)
    		if user_obj is None:
    			self.UserLogger.debug('Error,no user object retrieved oldpass = %s, newpass = %s, ip = %s , emailid = %s, userid = %d' % (oldpass,newpass,ip,str(emailid),userid))
    			return (-1,'ERROR: No such user exists')
            	if user_obj.UserPassword != oldpass:
            		self.UserLogger.debug('Error,Old Pasword does not match oldpass = %s, newpass = %s, ip = %s , userid = %d' % (oldpass,newpass,ip,userid))
    			return (-1,'ERROR: Old Pasword does not match')
    		PreviousState = "{oldpass:"+ oldpass + "}"
    		LogsDesc = 'Changed Password'
		return self.ResetPass(newpass,user_obj,LogsDesc,PreviousState,by,ip,op=SYSTEM_PERMISSION_UPDATE)
    	except:
            exception_log = ('[%s] %s,%d')%('ChangePassword',ip,userid)
            self.UserLogger.exception(exception_log)
            return (-1,'error in Changing password')
            
            
    def ForgetPassword(self,emailid,by,ip,op=SYSTEM_PERMISSION_UPDATE):
    	try:
    		user_obj = User()
    		user_obj = User.objects.get(UserEmail=emailid)
    		if by == -1:
    			by = user_obj.id
    		if user_obj is None:
    			self.UserLogger.debug('Error,no user object retrieved')
    			return (-1,'ERROR: No such user exists')
    		PreviousState = "{oldpass:"+ user_obj.UserPassword + "}"
    		LogsDesc = 'Forget Password'
    		import random
    		password = str(random.randint(100000,999999))
    		# send an email 
    		self.send_email_forget_pass(emailid,password)
    		#generate a new password
    		self.UserLogger.exception("password reset for " + emailid + " new password is " + str(password))
		return self.ResetPass(self.encrypt.encrypt(password),user_obj,LogsDesc,PreviousState,by,ip,op=SYSTEM_PERMISSION_UPDATE)
    	except:
            exception_log = ('[%s] %s,%s')%('ForgetPassword',ip,emailid)
            self.UserLogger.exception(exception_log)
            return (-1,'error in Changing password')


        

            


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
		
		
    def getAllUsers(self):
    	try:
                UsersList =  User.objects.all()
                self.UserLogger.debug('[%s] %s'%('getAllUsers',str(len(UsersList))))                
                return (1,UsersList)
    	except:
                exception_log = ('[%s]')%('getAllUsers')
                self.UserLogger.exception(exception_log)
                return (-1,[])

    def send_email_forget_pass(self,email,password):
    	try:
		import time
		refs = int(time.time())
		token= "password reset for " + email + " new password is " + str(password) 
		sendMail([ "thoughtxplore@gmail.com",email],"no-reply@thoughtxplore.com","authenticate",token)
	except:
		pass
    
    def getUserObjectByEmailid(self,emailid):
    	try:
    		return User.objects.get(UserEmail=emailid)
    	except:
    		exception_log = ('[%s] emailid =  %s')%('getUserObjectByEmailid',emailid)
            	self.UserLogger.exception(exception_log)
    		return None
    		
    def getUserObjectByUserId(self,UserId):
    	try:
    		return User.objects.get(id=UserId)
    	except:
    		exception_log = ('[%s] UserId =  %d')%('getUserObjectByUserId',UserId)
            	self.UserLogger.exception(exception_log)
    		return None
    
