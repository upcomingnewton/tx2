# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.BusinessFunctions.UserFunctions import UserFnx
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.UserReg.BusinessFunctions.UserRegFunctions import UserRegFnx
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity,getSystemGroup_NewUsers, getSystemUser_DaemonCreateUser
from tx2.Misc.Encryption import Encrypt
from tx2.CONFIG import LOGGER_UserReg,SESSION_MESSAGE,Login_From_Type,LogOut_From_Type
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypes
import logging

Logger = logging.getLogger(LOGGER_UserReg)

def AddUserForRegIndex(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
    	UserObj = UserFnx()
    	UserList = UserObj.getAllUsers()
    	if( UserList[0] == 1):
    		UserList = UserList[1]
    		if len(UserList) == 0:
    			msglist.append('no user in the system')
    		ContentTypeList = getContentTypes()
    		HttpRequest.session[SESSION_MESSAGE] = msglist
    		return render_to_response("UserReg/UserRegTest.html",{'UserList':UserList, 'ContentTypeList':ContentTypeList},context_instance=RequestContext(HttpRequest))
    	else:
    		error_msg = 'some error occured while retrieving users	'
    		msglist.append(error_msg)
    		Logger.debug('[%s][%s] == %s ==' % (ip, 'AddUserForRegIndex',error_msg))
    		HttpRequest.session[SESSION_MESSAGE] = msglist
    		HttpResponseRedirect('/message/')
    except:
    	Logger.exception('[%s][%s] == EXCEPTION ==' % (ip, 'AddUserForRegIndex'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
        
def AddUserForReg(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
    	UserRegFnxObj = UserRegFnx()
    	_SelectedUsers = HttpRequest.POST.getlist('SelectedUsers')
    	_App_label,_Model = str(HttpRequest.POST['ContentType']).split('-')
    	_Record = int(HttpRequest.POST['RecordID'])
    	print _SelectedUsers,_App_label,_Model,_Record
    	result =  UserRegFnxObj.AdduserData(_App_label,_Model,_Record,'test',_SelectedUsers,int(details['userid']),ip)
    	msglist.append(result)
    	HttpRequest.session[SESSION_MESSAGE] = msglist
    	HttpResponseRedirect('/userreg/users/')
    except:
    	Logger.exception('[%s][%s] == EXCEPTION ==' % (ip, 'AddUserForReg'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
