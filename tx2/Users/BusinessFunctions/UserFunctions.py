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
    
    def __init__(self):
        self.encrypt = Encrypt()
        self.UserLogger = logging.getLogger(LoggerUser)
        
    def AuthenticateUserFromSite(self,emailid,ip):
        try:
            to_emailid = self.encrypt.decrypt(emailid)
            s = to_emailid.split('___')
            userid = int(s[0])
            self.UserLogger.debug('userid = %d' % (userid))
            # get the user
            user_obj = User.objects.get(id=userid)
            self.UserLogger.debug('userid = %d, userid from token %d' % (user_obj.id, userid))
            if( user_obj is None ):
            	self.UserLogger.exception('user does not exists')
            	return -1
	    groupid = getSystemGroup_EmailAU();
	    if( groupid == -1):
	    	self.UserLogger.exception('group id is -1')
	    	return -1
            details = {
                       'email':user_obj.UserEmail,
                       'pass':user_obj.UserPassword,
                       'bday':str(user_obj.UserBirthDate),
                       'fname':user_obj.UserFirstName,
                       'mname':user_obj.UserMiddleName,
                       'lname':user_obj.UserLastName,
                       'entity':user_obj.UserEntity.id,
                       'gender':user_obj.UserGender,
                       'LogsDesc':'UserAuthenticationByEmail',
                       'PreviousState':'UserAuthenticationByEmail',
                       'group':groupid,
                       'op':SYSTEM_PERMISSION_EMAIL_AU,
                       'by':userid,
                       'ip':ip,
                       }
            self.UserLogger.debug('userid = %d, details = %s' % (userid, str(details)))
            result = DBUpdateUser(details)
            self.UserLogger.debug('result = %s' % (result))
            if result['result'] == 1 :
                return (1,"Your profile has been sucessfully updated. </ br>You can login now") 
            else:
                return (-1,"Some Error has occured") 
        except:
            exception_log = ('[%s] %s,%s')%('AuthenticateUserFromSite',ip,emailid)
            self.UserLogger.exception(exception_log)
            return (-1,'error in authenticating user')
        
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
                    'ip':ip}
            result = DBInsertUser(user)
            if ( result['result'] == 1):
            	 self.send_mail_test(email,result['rescode'],fname,ip)
            if result['result'] == 1 :
                return (1,"Your profile has been sucessfully created.Please check your email for activation link.") 
            else:
                return (-1,"Some Error has occured") 
        except:
            exception_log = ('[%s] %s,%s')%('InsertUserFromSite',ip,email)
            self.UserLogger.exception(exception_log)
            return (-1,'error in inserting user')
            
    def UpdateUser(self,email,password,bday,fname,mname,lname,entity,gender,group,by,ip,op=SYSTEM_PERMISSION_UPDATE):
        try:
#            to_emailid = self.encrypt.decrypt(emailid)
#            user_obj = User.objects.get(id=userid)
#            self.UserLogger.debug('userid = %d, userid from token %d' % (user_obj.id, userid))
#	    self.UserLogger.exception('group id is -1')
#	    return -1
#            details = {
#                       'email':email,
#                       'pass':password,
#                       'bday':str(bday),
#                       'fname':fname,
#                       'mname':mname,
#                       'lname':lname,
#                       'entity':user_obj.UserEntity.id,
#                       'gender':gender,
#                       'LogsDesc':'UserAuthenticationByEmail',
#                       'PreviousState':'UserAuthenticationByEmail',
#                       'group':groupid,
#                       'op':SYSTEM_PERMISSION_EMAIL_AU,
#                       'by':userid,
#                       'ip':ip,
#                       }
#            self.UserLogger.debug('userid = %d, details = %s' % (userid, str(details)))
#            result = DBUpdateUser(details)
#            self.UserLogger.debug('result = %s' % (result))
            return (1,'')
        except:
            exception_log = ('[%s] %s,%s')%('AuthenticateUserFromSite',ip,emailid)
            self.UserLogger.exception(exception_log)
            return (-1,'error in authenticating user')
        ##################################################################
    
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

    def LoginUser(self,email,password,_type,ip):
        try:
            details = {'email':email,
                       'pass':self.encrypt.encrypt(password),
                       'login_type':_type,
                        'ip':ip,
                       }
            #print self.encrypt.encrypt(password)
            result = DBLoginUser(details)
            if( int(result['result']) >= 1):
                #MakeGroupMenu(result['groupid'])
                AddLoginIdToLoggedInUsersDict(self.encrypt.encrypt(str(result['loginid'])))
                return(1,result)
            else:
                return(-1,'Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon')
        except:
            exception_log = ('[%s] %s,%s %s %s')%('LoginUser',ip,email,_type,self.encrypt.encrypt(password))
            self.UserLogger.exception(exception_log)
            return (-1,'Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon')
        
    def LogoutUser(self,loginid,out_from):
        try:
            details = {'loginid':self.encrypt.decrypt(loginid),
                       'logout_from':out_from,
                      }
            result = DBLogoutUser(details)
            if (result['result'] == 1 ):
                ClearLoginIdFromLoggedInUsersDict(self.encrypt.encrypt(str(details['loginid'])))
            return result
        except:
            exception_log = ('[%s] %s')%('LogoutUser',loginid)
            self.UserLogger.exception(exception_log)
            return (-1,'Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon')
            
    def ChangeUserGroup(self,userid,GroupName):
    	try:	
    		user_obj = self.getUserObjectByUserId(userid)
    		GroupFnxObj = GroupFnx()
    		groupobj = GroupFnxObj.getGroupByName(GroupName)
    		groupobj = groupobj[0]
    		self.UserLogger.debug('ChangeUserGroup %d, %s' % (userid,GroupName))
    		details = {
                       'email':user_obj.UserEmail,
                       'pass':user_obj.UserPassword,
                       'bday':str(user_obj.UserBirthDate),
                       'fname':user_obj.UserFirstName,
                       'mname':user_obj.UserMiddleName,
                       'lname':user_obj.UserLastName,
                       'entity':user_obj.UserEntity.id,
                       'gender':user_obj.UserGender,
                       'LogsDesc':'GROUP CHANGED',
                       'PreviousState':str(user_obj.Group.id),
                       'group':groupobj.id,
                       'op':op,
                       'by':by,
                       'ip':ip,
                      }
           result = DBUpdateUser(details)
           self.UserLogger.debug('result = %s' % (result))
           return (1,result)
    	except:
    	    exception_log = ('[%s] %s %s')%('ChangeUserGroup',userid,GroupName)
            self.UserLogger.exception(exception_log)
            return (-1,'Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon')

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
    
