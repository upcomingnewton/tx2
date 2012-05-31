# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.BusinessFunctions.UserFunctions import UserFnx
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Misc.Encryption import Encrypt
#from ThoughtXplore.txUser.views.Views_MiscFnx import CheckAndlogout
#from ThoughtXplore.txMisc.Validation.Validation import EmailValidate , StringValidate
#from ThoughtXplore.txMisc.Encryption.enc_dec import Encrypt
#from ThoughtXplore.txCommunications.CommunicationFunctions import send_validation_email
from tx2.CONFIG import LoggerUser,SESSION_MESSAGE,Login_From_Type,LogOut_From_Type
import logging


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
                    result = res[0]
                    if( result['result'] == 1):
                        token = {"userid":result['userid'],"groupid":result['groupid'],"loginid":encdec.encrypt( str(result['loginid']))}
                        #print token
                        HttpRequest.session["details"] = token
                        #print 'i have reached here'
                        return HttpResponseRedirect('/user/dashboard/')
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
    msglist = AppendMessageList(HttpRequest)
    try:
        if "details" in HttpRequest.session.keys():
            token = HttpRequest.session['details']
            print token
            logout_user = UserFnx()
            res =  logout_user.LogoutUser(token['loginid'],LogOut_From_Type)
            if ( res[0] != -1):
                    result = res[0]
                    if( result['result'] == 1):
                        del HttpRequest.session['details']
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
    except:
            LoggerUser.exception('[log_out][%s] Exception '%(ip))
            msglist.append('Some Error has occoured')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')

    
#@never_cache
#def CreateUserFromSite(HttpRequest):
#    return HttpResponse(str(HttpRequest))
#    ip = HttpRequest.META['REMOTE_ADDR']
#    msglist = []
#    try:
#        email = HttpRequest.POST['RegisterUser_email']
#        email_val = EmailValidate(email)
#        if( email_val.validate() != 1):
#            msglist.append('invalid email adress')
#        pass1 = HttpRequest.POST['RegisterUser_pass']
#        pass2 = HttpRequest.POST['RegisterUser_pass2']
#        if( pass1 != pass2):
#            msglist.append('passwords do not match')
#        str_val = StringValidate()
#        fname = HttpRequest.POST['RegisterUser_fname']
#        if(str_val.validate_alphastring(fname) != 1):
#                msglist.append('first name should contain only alphabets')
#        mname = HttpRequest.POST['RegisterUser_mname']
#        if( len(mname) > 0 ):
#            if(str_val.validate_alphastring(mname) != 1):
#                msglist.append('middle name should contain only alphabets')
#        lname = HttpRequest.POST['RegisterUser_lname']
#        if(str_val.validate_alphastring(lname) != 1):
#                msglist.append('last name should contain only alphabets')
#        bday = HttpRequest.POST['RegisterUser_dob']
#        bday = bday.split('/')
#        try:
#            bday = datetime.date(int(bday[2]),int(bday[0]),int(bday[1]))
#        except ValueError as err:
#            msglist.append('Invalid Birthdate, '+ err.message)
#        gender = HttpRequest.POST['RegisterUser_gender']
#        if gender== "-1" :
#            msglist.append('Please select your gender')
#            
#        if ( len(msglist) > 0 ):
#            HttpRequest.session[SESSION_MESSAGE] = msglist
#            return HttpResponseRedirect('/user/register/')
#        else:
#            insfnx = UserFunctions.UserFnx()
#            res = insfnx.InsertUserFromSite(email, pass2, fname, mname, lname, gender, bday,'system',HttpRequest.META['REMOTE_ADDR'])
#            result = res[0]
#            if( result['result'] >= 1 ):
#                msglist.append('account created. an email has been sent in this regard.')
#                HttpRequest.session[SESSION_MESSAGE] = msglist
#                insfnx.send_mail_test(email, result['rescode'], fname, HttpRequest.META['REMOTE_ADDR'])
#                encrypt = Encrypt()
#                return HttpResponseRedirect('/user/register')
#            else:
#                LoggerUser.error(res)
#                msglist.append(res[1])
#                HttpRequest.session[SESSION_MESSAGE] = msglist
#                return HttpResponseRedirect('/error/')
#    except:
#        LoggerUser.exception('[CreateUserFromSite][%s] Exception '%(ip))
#        msglist.append('Some Error has occoured')
#        HttpRequest.session[SESSION_MESSAGE] = msglist
#        return HttpResponseRedirect('/error/')
#        
#        
#@never_cache
#def AuthenticateUserFromEmail(HttpRequest,token,refs):
#    au_user = UserFunctions.UserFnx()
#    ip = HttpRequest.META['REMOTE_ADDR']
#    msglist = []
#    try:
#        res = au_user.AuthenticateUserFromSite(token, ip)
#        result = res[0]
#        if( result['result'] >= 1 ):
#            encrypt = Encrypt()
#            return HttpResponseRedirect('/user/login/')
#        else:
#            msglist.append(res[1])
#            HttpRequest.session[SESSION_MESSAGE] = msglist
#            return HttpResponseRedirect('/error/')
#    except:
#        LoggerUser.exception('[AuthenticateUserFromEmail][%s] Exception token=%s'%(ip,token))
#        msglist.append('Some Error has occoured')
#        HttpRequest.session[SESSION_MESSAGE] = msglist
#        return HttpResponseRedirect('/error/')
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
#def CreateUserIndex(request):
#    return render_to_response('UserSystem/User/CreateUser.html',{'title':'create user page'},context_instance=RequestContext(request))
#
#
# HELPER FUNCTION
#
#FOLLOWING FUNCTION LOGS OUT A USER
def CheckAndlogout(HttpRequest):
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
                        del HttpRequest.session['details']
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