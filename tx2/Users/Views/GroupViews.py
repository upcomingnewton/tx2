from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
from tx2.Users.BusinessFunctions.GroupTypeFunctions import GroupTypeFnx
import logging
Logger_User = logging.getLogger(LoggerUser)

def GroupIndex(HttpRequest,__list,__create):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
    	GroupList = []
    	GroupTypeList = []
    	flag = 0
    	if __list == 'true':
		GroupFnxObj  = GroupFnx()
		GroupList = GroupFnxObj.ListAllGroups()
		if(GroupList[0] == 1):
		    GroupList  = GroupList[1]
		    if( len (GroupList) == 0):
		        msglist.append('There are no group in the system yet')
		else:
		    flag = 1
		    msglist.append('Error Occured while  fetching groups list for your request')
	if __create == 'true':
		GroupTypeFnxObj  = GroupTypeFnx()
        	GroupTypeList = GroupTypeFnxObj.ListAllGroupTypes()
        	if(GroupTypeList[0] == 1):
            		GroupTypeList  = GroupTypeList[1]
            		if( len (GroupTypeList) == 0):
                		msglist.append('There are no group types in the system yet')
                else:
                    flag = 1
		    msglist.append('Error Occured while fetching group-types for your request')
	
	if flag == 1:
		HttpRequest.session[SESSION_MESSAGE] = msglist
		HttpResponseRedirect('/message/')
	else:
		HttpRequest.session[SESSION_MESSAGE] = msglist
		return render_to_response("UserSystem/Group/EditGroup.html",{'GroupList':GroupList,'GroupTypeList':GroupTypeList,'list__t':__list,'create__t':__create},context_instance=RequestContext(HttpRequest))
		
				    
		    
    except:
        Logger_User.exception('[%s][%s] == EXCEPTION =='%('GroupIndex',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')

def CreateNewGroup(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
    	Group_Name = ""
    	Group_Desc = ""
    	Group_GroupType = ""
    	flag = 0
        if "Group_Name" in HttpRequest.POST:
        	Group_Name = HttpRequest.POST['Group_Name']
        else:
        	msglist.append('error performing operation. Problem in Name')
        	flag = 1
        if "Group_Desc" in HttpRequest.POST:
        	Group_Desc = HttpRequest.POST['Group_Desc']
        else:
        	msglist.append('error performing operation.Problem in desc')
        	flag = 1
        if 'Group_GroupType' in  HttpRequest.POST:
        	Group_GroupType = int(HttpRequest.POST['Group_GroupType'])
        	if Group_GroupType == -1:
        		msglist.append('Please select a proper group type')
        		flag = 1
        else:
        	msglist.append('error performing operation.Problem in GroupType')
        	flag = 1
        if flag == 1:
        	HttpRequest.session[SESSION_MESSAGE] = msglist
		return HttpResponseRedirect('/user/group/create/')
	else:
		GroupFnxObj  = GroupFnx()
		result = GroupList = GroupFnxObj.CreateGroup(Group_Name,Group_Desc,Group_GroupType,-1,logindetails["userid"],ip)
		msglist.append(result)
		HttpRequest.session[SESSION_MESSAGE] = msglist
		return HttpResponseRedirect('/user/group/')
		
    except:
        Logger_User.exception('[%s][%s] == EXCEPTION =='%('CreateNewGroup',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')
