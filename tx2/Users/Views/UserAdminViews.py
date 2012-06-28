# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.BusinessFunctions.UserFunctions import UserFnx
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
from tx2.Security.BusinessFunctions.StateFunctions import StateFnx
   #getAllUsers
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity,getSystemGroup_NewUsers, getSystemUser_DaemonCreateUser
from tx2.Misc.Encryption import Encrypt
from tx2.CONFIG import LoggerUser,SESSION_MESSAGE,Login_From_Type,LogOut_From_Type
import logging
import datetime

LoggerUser = logging.getLogger(LoggerUser)


def ListAllUsers(HttpRequest):
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
    		HttpRequest.session[SESSION_MESSAGE] = msglist
    		return render_to_response("UserSystem/User/ListUsers.html",{'UserList':UserList,'EditUsers':'true'},context_instance=RequestContext(HttpRequest))
    	else:
    		error_msg = 'some error occured while retrieving users	'
    		msglist.append(error_msg)
    		LoggerUser.debug('[%s][%s] == %s ==' % (ip, 'ListAllUsers',error_msg))
    		HttpRequest.session[SESSION_MESSAGE] = msglist
    		HttpResponseRedirect('/message/')
    except:
    	LoggerUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'ListAllUsers'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
        
        
def EditUserIndex(HttpRequest,userid):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
    	UserObj = UserFnx()
    	User_Obj = UserObj.getUserObjectByUserId(userid)
    	if( User_Obj is not None):
    		Group_Obj = GroupFnx()
    		GroupList = Group_Obj.ListAllGroups()
    		GroupList = GroupList[1]
    		State_Obj = StateFnx()
    		StateList = State_Obj.ListAllStates()
    		StateList = StateList[1]
    		HttpRequest.session[SESSION_MESSAGE] = msglist
    		return render_to_response("UserSystem/User/EditUser.html",{'user':User_Obj,'GroupList':GroupList, 'StateList':StateList},context_instance=RequestContext(HttpRequest))
    	else:
    		error_msg = 'some error occured while retrieving user	'
    		msglist.append(error_msg)
    		LoggerUser.debug('[%s][%s] == %s ==' % (ip, 'ListAllUsers',error_msg))
    		HttpRequest.session[SESSION_MESSAGE] = msglist
    		HttpResponseRedirect('/message/')
    except:
    	LoggerUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'ListAllUsers'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')



def EditUser(HttpRequest,userid):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
    	UserFnxObj = UserFnx()
    	UserObj = UserFnxObj.getUserObjectByUserId(userid)
    	if UserObj is None
    		# error here
    	flag = 1
    	emailid = -1
    	password = -1
    	fname = -1
    	mname = -1
    	lname = -1
    	dob = -1
    	state = -1
    	group = -1
    	gender = -1
    	error_msg = []
    	if "UserEmail" in HttpRequest.POST:
    		emailid = HttpRequest.POST["UserEmail"]
    	else:
    		flag = -1
    		error_msg.append('Error while retrieving emailid')
    	if "Password" in HttpRequest.POST:
    		password = HttpRequest.POST["Password"]
    	else:
    		flag = -1
    		error_msg.append('Error while retrieving Password')
    	if "FirstName" in HttpRequest.POST:
    		fname = HttpRequest.POST["FirstName"]
    	else:
    		flag = -1
    		error_msg.append('Error while retrieving FirstName')
    	if "MiddleName" in HttpRequest.POST:
    		mname = HttpRequest.POST["MiddleName"]
    	else:
    		flag = -1
    		error_msg.append('Error while retrieving MiddleName')
    	if "LastName" in HttpRequest.POST:
    		lname = HttpRequest.POST["LastName"]
    	else:
    		flag = -1
    		error_msg.append('Error while retrieving LastName')
    	if "DateofBirth" in HttpRequest.POST:
    		dob = HttpRequest.POST["DateofBirth"]
    	else:
    		flag = -1
    		error_msg.append('Error while retrieving DateofBirth')
    	if "Gender" in HttpRequest.POST:
    		gender = HttpRequest.POST["Gender"]
    	else:
    		flag = -1
    		error_msg.append('Error while retrieving Gender')
    	if "State" in HttpRequest.POST:
    		state = HttpRequest.POST["State"]
    	else:
    		flag = -1
    		error_msg.append('Error while retrieving State')
    	if "Group" in HttpRequest.POST:
    		group = HttpRequest.POST["Group"]
    	else:
    		flag = -1
    		error_msg.append('Error while retrieving group')
    	if flag == -1:
    		# error here
    		msglist = error_msg
    		LoggerUser.debug('[%s][%s] == %s ==' % (ip, 'ListAllUsers',error_msg))
    		HttpRequest.session[SESSION_MESSAGE] = msglist
    		HttpResponseRedirect('/message/')
    	else:
    		#update here
    except:
    	LoggerUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'ListAllUsers'))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')

