from tx2.Misc.Encryption import Encrypt
from tx2.Users.DBFunctions.DatabaseFunctions import DBLoginUser ,DBLogoutUser,DBInsertUser
from tx2.Users.DBFunctions.DBMessages import decode
from tx2.Users.HelperFunctions.LoginDetails import AddLoginIdToLoggedInUsersDict, ClearLoginIdFromLoggedInUsersDict 
from tx2.conf.LocalProjectConfig import *
from tx2.Misc.CacheManagement import setCache,getCache
#from cPickle import dumps, loads 
from tx2.CONFIG import LoggerUser
import logging
from tx2.Misc.Email import sendMail



class UserFnx():
    
    def __init__(self):
        self.encrypt = Encrypt()
        self.UserLogger = logging.getLogger(LoggerUser)
        
#    def AuthenticateUserFromSite(self,emailid,ip):
#        try:
#            to_emailid = self.encrypt.decrypt(emailid)
#            s = to_emailid.split('___')
#            details = {
#                       'userid':int(s[0]),
#                       'by':1,
#                       'request_group':'authenticated_users',
#                       'request_permission':'USER_AU',
#                       'ip':ip,
#                       'logsdesc':'UserAuthentication',
#                       }
#            result = DB_ChangeStateOfASingleUser(details)
#            return(result, decode(int(result['result']),result['rescode']))
#        except:
#            exception_log = ('[%s] %s,%s')%('AuthenticateUserFromSite',ip,emailid)
#            self.UserLogger.exception(exception_log)
        
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
            	 send_mail_test(email,result['rescode'],fname,ip)
            return(result, decode(int(result['result']),result['rescode']))
        except:
            exception_log = ('[%s] %s,%s')%('InsertUserFromSite',ip,email)
            self.UserLogger.exception(exception_log)
    
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
                return(result, decode(int(result['result']),result['rescode']))
            else:
                return(result, decode(int(result['result']),result['rescode']))
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
            return(result, decode(int(result['result']),result['rescode']))
        except:
            exception_log = ('[%s] %s')%('LogoutUser',loginid)
            self.UserLogger.exception(exception_log)
            return (-1,'Something un-usual has happened while processing your request. Administrators have been alerted to rectify the error. We will send you a notification in this regard soon')

    def send_mail_test(self,email,userid,fname,ip):
    	try:
		token= self.encrypt.encrypt(str(userid) + '___' + email)
		import time
		refs = int(time.time())
		token="http://labs-nitin.thoughtxplore.com/user/authenticate/email/"+token+"/" + str(refs) + "/"
		sendMail([ "upcomingnewton@gmail.com"],"no-reply@thoughtxplore.com","authenticate",token)
	except:
		pass
    
    
