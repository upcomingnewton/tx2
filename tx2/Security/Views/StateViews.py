from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerSecurity
from tx2.Security.BusinessFunctions.StateFunctions import StateFnx
import logging
Logger_User = logging.getLogger(LoggerSecurity)

def CreateNewStateIndex(HttpRequest,init):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    #print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return render_to_response("SecuritySystem/EditStates.html",{'StateList':{},'EditStateCreate':'true','EditStateList':'false','init_t':init,},context_instance=RequestContext(HttpRequest))
    except:
        Logger_User.exception('[][] == EXCEPTION =='%('CreateNewStateIndex',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')
        
        
def ListAllStates(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        StateFnxObj  = StateFnx()
        StateList = StateFnxObj.ListAllStates()
        if(StateList[0] == 1):
            StateList  = StateList[1]
            if( len (StateList) == 0):
                msglist.append('There are no states in the system yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("SecuritySystem/EditStates.html",{'StateList':StateList,'EditStateCreate':'false','EditStateList':'true','init_t':0,},context_instance=RequestContext(HttpRequest))
        else:
            msglist.append('Error Occured while fetching your request')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            HttpResponseRedirect('/message/')
    except:
        Logger_User.exception('[][] == EXCEPTION =='%('ListAllStates',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')

def StatesIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        StateFnxObj  = StateFnx()
        StateList = StateFnxObj.ListAllStates()
        if(StateList[0] == 1):
            StateList  = StateList[1]
            if( len (StateList) == 0):
                msglist.append('There are no group types in the system yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("SecuritySystem/EditStates.html",{'StateList':StateList,'EditStateCreate':'true','EditStateList':'true','init_t':0,},context_instance=RequestContext(HttpRequest))
        else:
            msglist.append('Error Occured while fetching your request')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            HttpResponseRedirect('/message/')
    except:
        Logger_User.exception('[][] == EXCEPTION =='%('StatesIndex',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')

def CreateNewState(HttpRequest,init):
    print init
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return render_to_response("SecuritySystem/EditStates.html",{},context_instance=RequestContext(HttpRequest))
    except:
        Logger_User.exception('[][] == EXCEPTION =='%('CreateNewState',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')