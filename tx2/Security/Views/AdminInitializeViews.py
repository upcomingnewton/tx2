# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Security.BusinessFunctions.AdminInitialize import AdminInitialize
#from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Misc.Encryption import Encrypt
from tx2.conf.LocalProjectConfig import SYSTEM_INITIALISE_LOGGER, SYSTEM_INITIALISE_SESSION_NAME
from tx2.conf.LocalProjectConfig import SYSTEM_INITIALISE_USERNAME
from tx2.conf.LocalProjectConfig import SYSTEM_INITIALISE_PASSWORD
from tx2.CONFIG import SESSION_MESSAGE
import logging


InitAdminLogger = logging.getLogger(SYSTEM_INITIALISE_LOGGER)



def AdminLogin(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        if SYSTEM_INITIALISE_SESSION_NAME in HttpRequest.session.keys():
        	del HttpRequest.session[SYSTEM_INITIALISE_SESSION_NAME]
        	InitAdminLogger.debug('[%s][%s] Session was already there. Deleted now before proceeding ahead'%('AdminLogin',ip))
        username = ""
        password = ""
	flag  = 0
        if 'LoginUser_email' in HttpRequest.POST:
        	username = HttpRequest.POST['LoginUser_email']
        else:
        	msglist.append('Error proceeding request for username. Please try later')
        	InitAdminLogger.exception('[%s][%s] LoginUser_email not there in POST list'%('AdminLogin',ip))
        	flag = 1
        if 'LoginUser_pass' in HttpRequest.POST:
        	password = HttpRequest.POST['LoginUser_pass']
        else:
        	msglist.append('Error proceeding request for password. Please try later')
        	InitAdminLogger.exception('[%s][%s] LoginUser_pass not there in POST list'%('AdminLogin',ip))
        	flag = 1
        if flag == 1:
        	HttpRequest.session[SESSION_MESSAGE] = msglist
        	return HttpResponseRedirect('/security/admin/')
        else:
        	if ( username != SYSTEM_INITIALISE_USERNAME ):
        		#error
        		msg  = 'Error : WRONG USERNAME'
        		msglist.append(msg)
        		InitAdminLogger.debug('[%s][%s] %s'%('AdminLogin',ip,msg))
        		HttpRequest.session[SESSION_MESSAGE] = msglist
        		return HttpResponseRedirect('/security/admin/')
        	if ( password != SYSTEM_INITIALISE_PASSWORD ):
        		msg  = 'Error : WRONG PASSWORD'
        		msglist.append(msg)
        		InitAdminLogger.debug('[%s][%s] %s'%('AdminLogin',ip,msg))
        		HttpRequest.session[SESSION_MESSAGE] = msglist
        		return HttpResponseRedirect('/security/admin/')
        	else:
        		#proceed
        		HttpRequest.session[SYSTEM_INITIALISE_SESSION_NAME] = 1
        		import time
        		msg = "USER LOGGED IN - TIME %s"%(str(time.time()))
        		InitAdminLogger.debug('[%s][%s] %s'%('AdminLogin',ip,msg))
        		return HttpResponseRedirect('/security/admin/welcome/')
    except:
    	msg = "== UNKNOWN SYSTEM EXCEPTION GENERATED =="
        InitAdminLogger.exception('[%s][%s] %s'%('AdminLogin',ip,msg))
        msglist.append(msg)
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    
def AdminLogout(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        if SYSTEM_INITIALISE_SESSION_NAME in HttpRequest.session.keys():
        	del HttpRequest.session[SYSTEM_INITIALISE_SESSION_NAME]
        	import time
        	InitAdminLogger.debug('[%s][%s] Deleted session - TIME %s'%('AdminLogout',ip,str(time.time())))
        else:
        	InitAdminLogger.exception('[%s][%s]NO SESSION WAS THERE'%('AdminLogout',ip))
	return HttpResponseRedirect('/security/admin/')
    except:
    	msg = "== UNKNOWN SYSTEM EXCEPTION GENERATED =="
        InitAdminLogger.exception('[%s][%s] %s'%('AdminLogout',ip,msg))
        msglist.append(msg)
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    
def AdminIndex(HttpRequest):
	msglist = AppendMessageList(HttpRequest)
	ip = HttpRequest.META['REMOTE_ADDR']
	try:
		isLoggedIn = 'false'
		#if logged in 
		if SYSTEM_INITIALISE_SESSION_NAME in HttpRequest.session.keys():
			isLoggedIn = 'true'
		HttpRequest.session[SESSION_MESSAGE] = msglist
		return render_to_response("SecuritySystem/Admin/SecurityAdminLogin.html",{'isLoggedIn':isLoggedIn},context_instance=RequestContext(HttpRequest))
	except:
		msg = "== UNKNOWN SYSTEM EXCEPTION GENERATED =="
        	InitAdminLogger.exception('[%s][%s] %s'%('AdminIndex',ip,msg))
        	msglist.append(msg)
        	HttpRequest.session[SESSION_MESSAGE] = msglist
        	return HttpResponseRedirect('/user/login/')
    
    

def  InsertSystemStates(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        if SYSTEM_INITIALISE_SESSION_NAME in HttpRequest.session.keys():
        	#process here
        	AdminObj = AdminInitialize()
        	result = AdminObj._InsertSystemStates()
        	msglist.append(result[1])
        	HttpRequest.session[SESSION_MESSAGE] = msglist
        	del HttpRequest.session[SYSTEM_INITIALISE_SESSION_NAME]
		return HttpResponseRedirect('/security/admin/')
    except:
    	msg = "== UNKNOWN SYSTEM EXCEPTION GENERATED =="
        InitAdminLogger.exception('[%s][%s] %s'%('InsertSystemStates',ip,msg))
        msglist.append(msg)
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
	
def  InsertSystemPermissions(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        if SYSTEM_INITIALISE_SESSION_NAME in HttpRequest.session.keys():
        	#process here
        	AdminObj = AdminInitialize()
        	result = AdminObj._InsertSystemPermissions()
        	msglist.append(result[1])
        	HttpRequest.session[SESSION_MESSAGE] = msglist
        	del HttpRequest.session[SYSTEM_INITIALISE_SESSION_NAME]
		return HttpResponseRedirect('/security/admin/')
    except:
    	msg = "== UNKNOWN SYSTEM EXCEPTION GENERATED =="
        InitAdminLogger.exception('[%s][%s] %s'%('InsertSystemPermissions',ip,msg))
        msglist.append(msg)
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
        
def  DefaultUserSystem(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        if SYSTEM_INITIALISE_SESSION_NAME in HttpRequest.session.keys():
        	#process here
        	AdminObj = AdminInitialize()
        	result = AdminObj._DefaultUserSystem()
        	msglist.append(result[1])
        	HttpRequest.session[SESSION_MESSAGE] = msglist
        	del HttpRequest.session[SYSTEM_INITIALISE_SESSION_NAME]
		return HttpResponseRedirect('/security/admin/')
    except:
    	msg = "== UNKNOWN SYSTEM EXCEPTION GENERATED =="
        InitAdminLogger.exception('[%s][%s] %s'%('DefaultUserSystem',ip,msg))
        msglist.append(msg)
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
        
def  DefaultSecurityContentSystem(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        if SYSTEM_INITIALISE_SESSION_NAME in HttpRequest.session.keys():
        	#process here
        	AdminObj = AdminInitialize()
        	result = AdminObj._DefaultSecurityContentSystem()
        	msglist.append(result[1])
        	HttpRequest.session[SESSION_MESSAGE] = msglist
        	del HttpRequest.session[SYSTEM_INITIALISE_SESSION_NAME]
    return HttpResponseRedirect('/security/admin/')
    except:
    	msg = "== UNKNOWN SYSTEM EXCEPTION GENERATED =="
        InitAdminLogger.exception('[%s][%s] %s'%('DefaultSecurityContentSystem',ip,msg))
        msglist.append(msg)
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')

def  RegisterUserFromSiteSystem(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        if SYSTEM_INITIALISE_SESSION_NAME in HttpRequest.session.keys():
        	#process here
        	AdminObj = AdminInitialize()
        	result = AdminObj._RegisterUserFromSiteSystem()
        	msglist.append(result[1])
        	HttpRequest.session[SESSION_MESSAGE] = msglist
        	del HttpRequest.session[SYSTEM_INITIALISE_SESSION_NAME]
		return HttpResponseRedirect('/security/admin/')
    except:
    	msg = "== UNKNOWN SYSTEM EXCEPTION GENERATED =="
        InitAdminLogger.exception('[%s][%s] %s'%('RegisterUserFromSiteSystem',ip,msg))
        msglist.append(msg)
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')


