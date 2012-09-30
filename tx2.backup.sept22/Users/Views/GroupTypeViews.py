from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
from tx2.Users.BusinessFunctions.GroupTypeFunctions import GroupTypeFnx
import logging
Logger_User = logging.getLogger(LoggerUser)

def GroupTypeIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        GroupTypeFnxObj  = GroupTypeFnx()
        GroupTypeList = GroupTypeFnxObj.ListAllGroupTypes()
        if(GroupTypeList[0] == 1):
            GroupTypeList  = GroupTypeList[1]
            if( len (GroupTypeList) == 0):
                msglist.append('There are no group types in the system yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserSystem/GroupTypes/EditGroupTypes.html",{'grouptypelist':GroupTypeList,'GroupTypesCreate':'true','GroupTypesList':'true',},context_instance=RequestContext(HttpRequest))
        else:
            msglist.append('Error Occured while fetching your request')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            HttpResponseRedirect('/message/')
    except:
        Logger_User.exception('[][] == EXCEPTION =='%('GroupTypeIndex',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')

def CreateNewGroup(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print 'CreateNewGroup'
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        print 'CreateNewGroup - not logged in'
        return HttpResponseRedirect('/user/login/')
    try:
    	name = ""
    	desc = ""
    	flag = 0
        if "GroupTypesCreate_Name" in HttpRequest.POST:
        	name = HttpRequest.POST['GroupTypesCreate_Name']
        else:
        	msglist.append('error performing operation. Problem in Name')
        	flag = 1
        if "GroupTypesCreate_Desc" in HttpRequest.POST:
        	desc = HttpRequest.POST['GroupTypesCreate_Desc']
        else:
        	msglist.append('error performing operation.Problem in desc')
        	flag = 1
        print name,desc
        if flag == 1:
        	HttpRequest.session[SESSION_MESSAGE] = msglist
		return HttpResponseRedirect('/user/grouptype/create/')
	else:
		GroupTypeFnxObj  = GroupTypeFnx()
		result = GroupTypeFnxObj.CreateGroupType(name,desc,int(logindetails["userid"]),ip)
		print result
		msglist.append(result)
		HttpRequest.session[SESSION_MESSAGE] = msglist
		return HttpResponseRedirect('/user/grouptype/')
		
    except:
        Logger_User.exception('[][] == EXCEPTION =='%('ListAllGroupTypes',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')
