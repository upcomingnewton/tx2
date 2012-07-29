# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.BusinessFunctions.UserFunctions import UserFnx
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity,getSystemGroup_NewUsers, getSystemUser_DaemonCreateUser
from tx2.Misc.Encryption import Encrypt
#from ThoughtXplore.txUser.views.Views_MiscFnx import CheckAndlogout
#from ThoughtXplore.txMisc.Validation.Validation import EmailValidate , StringValidate
#from ThoughtXplore.txMisc.Encryption.enc_dec import Encrypt
#from ThoughtXplore.txCommunications.CommunicationFunctions import send_validation_email
from tx2.CONFIG import LoggerUser,SESSION_MESSAGE,Login_From_Type,LogOut_From_Type
import logging
import datetime

LoggerUser = logging.getLogger(LoggerUser)



def Login_index(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
            mlist = CheckAndlogout(HttpRequest)
            msglist += mlist
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserSystem/User/Login.html",{},context_instance=RequestContext(HttpRequest))
    except:
        LoggerUser.exception('[Login_index][%s] == exception message == '%(ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
    
    
def log_in(HttpRequest):
        msglist = AppendMessageList(HttpRequest)
        usrfn = UserFnx()
        ip = HttpRequest.META['REMOTE_ADDR']
        encdec = Encrypt()
        try:
            #CheckAndlogout(HttpRequest)
            email = ''
            password = ''
            if 'LoginUser_email' in HttpRequest.POST.keys():
                email = HttpRequest.POST['LoginUser_email']
                #email_val = EmailValidate(email)
                #if( email_val.validate() != 1):
                #    msglist.append('invalid email adress')
            else:
                msglist.append('email required')
            if 'LoginUser_pass' in HttpRequest.POST.keys():
                password = HttpRequest.POST['LoginUser_pass']
                if( len(password) < 1):
                    msglist.append('password required')
            else:
                msglist.append('password required')
            if len(msglist) > 0:
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return HttpResponseRedirect('/user/login/')
            else:
                res = usrfn.LoginUser(email, password,Login_From_Type, ip)
                if ( res[0] != -1):
                    result = res[1]
                    if( result['result'] == 1):
                        token = {"userid":result['userid'],"groupid":result['groupid'],"loginid":encdec.encrypt( str(result['loginid']))}
                        #print token
                        HttpRequest.session["details"] = token
                        #print 'i have reached here'
                        return HttpResponseRedirect('/userprofile/UserProfile/StudentDetails/')
                    else:
                        # handle other cases here like user is not active and all that
                        LoggerUser.error(res)
                        msglist.append(res[1])
                        HttpRequest.session[SESSION_MESSAGE] = msglist
                        return HttpResponseRedirect('/message/')
                else:
                    msglist.append(res[1])
                    HttpRequest.session[SESSION_MESSAGE] = msglist
                    return HttpResponseRedirect('/message/')
        except:
            LoggerUser.exception('[log_in][%s] Exception '%(ip))
            msglist.append('Some Error has occoured')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
            
        
def log_out(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    print '*** ip ', str(ip)
    msglist = AppendMessageList(HttpRequest)
    try:
        if "details" in HttpRequest.session.keys():
            print '---+++--- yes it is there'
            token = HttpRequest.session['details']
            print token
            logout_user = UserFnx()
            #res =  logout_user.LogoutUser(token['loginid'],LogOut_From_Type)
            res =  logout_user.LogoutUser(token['loginid'],10)
            if ( res[0] != -1):
                    result = res[0]
                    if( result['result'] == 1):
                    	for sesskey in HttpRequest.session.keys():
                    		print '++-- SESSION KEY = ' + str(sesskey)
                        	del HttpRequest.session[sesskey]
                        return HttpResponseRedirect('/user/login/')
                    else:
                        # handle other cases here like user is not active and all that
                        LoggerUser.error(res)
                        msglist.append(res[1])
                        HttpRequest.session[SESSION_MESSAGE] = msglist
                        return HttpResponseRedirect('/message/')
            else:
                    msglist.append(res[1])
                    HttpRequest.session[SESSION_MESSAGE] = msglist
                    return HttpResponseRedirect('/message/')
        else:
                print '||==|| NO SESSION DATA'
    		return HttpResponse('error')
    except:
            LoggerUser.exception('[log_out][%s] Exception '%(ip))
            msglist.append('Some Error has occoured')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')

    
#@never_cache
def CreateUserFromSite(HttpRequest):
    msglist = []
    errmsg = []
    ip = HttpRequest.META['REMOTE_ADDR']
    details = GetLoginDetails(HttpRequest)
    by = getSystemUser_DaemonCreateUser()
    #return HttpResponse('good')
    if( details['userid'] != -1):
        by = int(details['userid'])
    try:
        email = HttpRequest.POST['RegisterUser_email']
        if len(email) < 4:
            errmsg.append('email required')
        pass1 = HttpRequest.POST['RegisterUser_pass']
        if len(pass1) < 4 or len(pass1) > 10:
            errmsg.append('password should be between 4 to 10 characters')
        pass2 = HttpRequest.POST['RegisterUser_pass2']
        if pass1 != pass2:
            errmsg.append('passwords do not match ')
        fname = HttpRequest.POST['RegisterUser_fname']
        if len(fname) < 2:
            errmsg.append('first name required')
        mname = HttpRequest.POST['RegisterUser_mname']
        if len(mname) < 2 or mname == "":
            mname = "--"
        lname = HttpRequest.POST['RegisterUser_lname']
        if len(lname) < 4:
            errmsg.append('last name required')
        bday = HttpRequest.POST['RegisterUser_dob']
        if len(bday) < 10:
            errmsg.append('birth date required')
        bday = bday.split('/')
        try:
            bday = datetime.date(int(bday[2]),int(bday[0]),int(bday[1]))
        except ValueError as err:
            msglist.append('Invalid Birthdate, '+ err.message)
        gender = HttpRequest.POST['RegisterUser_gender']
        if gender== "-1" :
            errmsg.append('Please select your gender')
        msglist = errmsg
        if ( len(errmsg) > 0 ):
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
        else:
            insfnx = UserFnx()
            res = insfnx.InsertUser(email, pass2, fname, mname, lname, gender, bday,getSystemEntity(),getSystemGroup_NewUsers(),by,ip)
            msglist.append(res[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
    except:
        LoggerUser.exception('[CreateUserFromSite][%s] Exception '%(ip))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
#        
#        
#@never_cache
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
    except:
        LoggerUser.exception('[AuthenticateUserFromEmail][%s] Exception token=%s'%(ip,token))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
#    
#        
#
#
#
#def MessageIndex(request,message):
#    encrypt = Encrypt()
#    return render_to_response("txMisc/Message.html",{'message':encrypt.decrypt(message)},context_instance=RequestContext(request))    
#
#
#def ListUsers(request):
#    return render_to_response("txUser/ListUsers.html",{'title':'list users', 'users':User.objects.all()},context_instance=RequestContext(request))
#
#
def CreateUserIndex(request):
    return render_to_response('UserSystem/User/CreateUser.html',{'title':'create user page'},context_instance=RequestContext(request))
#
#
# HELPER FUNCTION
#
#FOLLOWING FUNCTION LOGS OUT A USER
def CheckAndlogout(HttpRequest):
    LoggerUser.debug('enterted CheckAndlogout')
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        if "details" in HttpRequest.session.keys():
            token = HttpRequest.session['details']
            LoggerUser.debug('[CheckAndlogout][%s]logging out user, %s'%(ip,str(token)))
            logout_user = UserFnx()
            res =  logout_user.LogoutUser(token['loginid'],-9)
            if ( res[0] != -1):
                    result = res[0]
                    if( result['result'] == 1):
                        for sesskey in HttpRequest.session.keys():
                    		print '++-- SESSION KEY = ' + str(sesskey)
                        	del HttpRequest.session[sesskey]
                    else:
                        # handle other cases here like user is not active and all that
                        LoggerUser.error(res)
                        msglist.append(res[1])
                        HttpRequest.session[SESSION_MESSAGE] = msglist
            else:
                    msglist.append(res[1])
                    HttpRequest.session[SESSION_MESSAGE] = msglist
        else:
            #msglist.append('user not logged in')
            LoggerUser.debug('==||== no session data is present for this request')
            pass
        return msglist
    except:
            LoggerUser.exception('[CheckAndlogout][%s] Exception '%(ip))
            msglist.append('Some Error has occoured')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return []


def view_dashboard(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] == -1):
        msglist.append('Please Login.')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/user/login/')
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        #print 'i am here, i have come here', HttpRequest.session.keys()
        if "details" in HttpRequest.session:
            #return HttpResponse(str(HttpRequest.session["details"]))
            return render_to_response('UserSystem/User/home.html',{"details":str(HttpRequest.session["details"]), 'msglist':msglist},context_instance=RequestContext(HttpRequest))
        else:
            return HttpResponseRedirect('/user/login/')
    except:
        LoggerUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'view_dashboard'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
        
        
########################## FUNCTIONS FOR CHANGING AND RESETTING PASSWORD ############################
def ChangePassIndex(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
    	HttpRequest.session[SESSION_MESSAGE] = msglist
    	return render_to_response("UserSystem/User/ChangePass.html",{},context_instance=RequestContext(HttpRequest))
    except:
    	LoggerUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'ChangePassIndex'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
	
def ResetPasswordIndex(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] != -1):
	CheckAndlogout(HttpRequest)
    try:
    	HttpRequest.session[SESSION_MESSAGE] = msglist
    	return render_to_response("UserSystem/User/ResetPassword.html",{},context_instance=RequestContext(HttpRequest))
    except:
    	LoggerUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'ResetPasswordIndex'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
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
    		HttpResponseRedirect('/user/password/change/')
    	else:
    		UserObj = UserFnx()
    		res = UserObj.ChangePassword(oldpass,newpass,int(details['userid']),ip,userid=int(details['userid']))
    		msglist.append(res)
    		HttpRequest.session[SESSION_MESSAGE] = msglist
    		HttpResponseRedirect('/user/password/change/')
    except:
    	LoggerUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'ResetPasswordIndex'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
	
def ResetPass(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] != -1):
	CheckAndlogout(HttpRequest)
    try:
    	HttpRequest.session[SESSION_MESSAGE] = msglist
    	if 'ResetPasswordEmail' in HttpRequest.POST:
    		emailid = HttpRequest.POST['ResetPasswordEmail']
    		UserObj = UserFnx()
    		obj = UserObj.getUserObjectByEmailid(emailid)
    		if obj is None:
    			msglist.append('user does not exist')
    			HttpRequest.session[SESSION_MESSAGE] = msglist
    			return render_to_response("UserSystem/User/ResetPassword.html",{},context_instance=RequestContext(HttpRequest))
    		else:
    			res = UserObj.ForgetPassword(emailid,obj.id,ip)
    			msglist.append(res)
    			HttpRequest.session[SESSION_MESSAGE] = msglist
    			HttpResponseRedirect('/user/password/reset/')
    			
    	else:
    		msglist.append('email required')
    		HttpRequest.session[SESSION_MESSAGE] = msglist
    		return render_to_response("UserSystem/User/ResetPassword.html",{},context_instance=RequestContext(HttpRequest))
    except:
    	LoggerUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'ResetPasswordIndex'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
        
def ShowMessages(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return render_to_response("message.html",{},context_instance=RequestContext(HttpRequest))
