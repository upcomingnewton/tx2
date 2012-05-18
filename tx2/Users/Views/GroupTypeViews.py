from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
from tx2.Users.BusinessFunctions.GroupTypeFunctions import GroupFnx
import logging
Logger_User = logging.getLogger(LoggerUser)

def CreateNewGroupTypeIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return render_to_response("UserSystem/GroupTypes/EditGroupTypes.html",{'grouptypelist':{},'GroupTypesCreate':'true','GroupTypesList':'false',},context_instance=RequestContext(HttpRequest))
    except:
        Logger_User.exception('[][] == EXCEPTION =='%('CreateNewGroupTypeIndex',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')
        
        
def ListAllGroupTypes(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        GroupFnxObj  = GroupFnx()
        GroupTypeList = GroupFnxObj.ListAllGroupTypes()
        if(GroupTypeList[0] == 1):
            GroupTypeList  = GroupTypeList[1]
            if( len (GroupTypeList) == 0):
                msglist.append('There are no group types in the system yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserSystem/GroupTypes/EditGroupTypes.html",{'grouptypelist':GroupTypeList,'GroupTypesCreate':'false','GroupTypesList':'true',},context_instance=RequestContext(HttpRequest))
        else:
            msglist.append('Error Occured while fetching your request')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            HttpResponseRedirect('/message/')
    except:
        Logger_User.exception('[][] == EXCEPTION =='%('ListAllGroupTypes',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')

def GroupTypeIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        GroupFnxObj  = GroupFnx()
        GroupTypeList = GroupFnxObj.ListAllGroupTypes()
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
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return render_to_response("UserSystem/User/Login.html",{},context_instance=RequestContext(HttpRequest))
    except:
        Logger_User.exception('[][] == EXCEPTION =='%('ListAllGroupTypes',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')