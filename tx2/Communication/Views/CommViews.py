from django.http import HttpResponseRedirect, HttpRequest
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
from django.shortcuts import render_to_response
from django.template import RequestContext



def noticeIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return render_to_response("TwoColumnMaster.html",{'type':['NOTICE'],'title':"Notices"},context_instance=RequestContext(HttpRequest))
        
        #return HttpResponseRedirect('/user/login/')
    else:
        return render_to_response("TwoColumnMaster.html",{'type':['NOTICE'],'title':"Notices"},context_instance=RequestContext(HttpRequest))
