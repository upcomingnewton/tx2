from django.contrib import messages

from django.http import HttpResponseRedirect, HttpRequest
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
from django.shortcuts import render_to_response
from django.template import RequestContext
from tx2.Communication.BusinessFunctions import CommunicationFunctions
import datetime
from httplib import HTTP
import logging
from django.core.exceptions import ObjectDoesNotExist
import inspect

LogUser = logging.getLogger(LoggerUser)


def adminNoticeIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] == -1):
        
        return HttpResponseRedirect('/user/login/')
    else:
        return render_to_response("Communication/Admin/PostNotices.html",{'type':['NOTICE'],'title':"Post Notice"},context_instance=RequestContext(HttpRequest))

def adminNewsIndex(HttpRequest):
    details = GetLoginDetails(HttpRequest)
    if( details['userid'] == -1):
        
        return HttpResponseRedirect('/user/login/')
    else:
        
        return render_to_response("Communication/Admin/PostNotices.html",{'type':['NEWS'],'title':"Post News"},context_instance=RequestContext(HttpRequest))

def adminNewsPost(HttpRequest):
    
    
    details = GetLoginDetails(HttpRequest)
    
    ip = HttpRequest.META['REMOTE_ADDR']
    

    if( details['userid'] == -1):
        
        return HttpResponseRedirect('/user/login/') 
    else:
        try:
            print "1"
            comm_call=CommunicationFunctions.PostCommunicationFnx()
            print "2"
            title= HttpRequest.POST['Title']
            _content=HttpRequest.POST['Content']
            print "fine"
            tstamp=datetime.datetime.strptime(HttpRequest.POST["date_"], "%m/%d/%Y")
            #print "fine2"
            #print str(tstamp)
            
            print "here"
            result= comm_call.PostNews(title, _content, tstamp,details["userid"],ip)
            print result
            if(result["result"]==-2):
                return HttpResponseRedirect('/user/login')
            elif(result["result"]==1):
                messages.info(HttpRequest, "News Posted Successfully")
            else:
                messages.error(HttpRequest, result)
            return HttpResponseRedirect('/message/')
            
        except Exception as inst:
            LogUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'NoticePost'))
            messages.error(HttpRequest,'Some Error has occoured')
            return HttpResponseRedirect('/message/')    

def adminNoticePost(HttpRequest):
    
    logindetails = GetLoginDetails(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']

    if( logindetails['userid'] == -1):
        return HttpResponseRedirect('/user/login/')
    else:
        try:
            comm_call=CommunicationFunctions.PostCommunicationFnx()
            title= HttpRequest.POST['Title']
            _content=HttpRequest.POST['Content']
            Users='0'
            result= comm_call.PostNotice(title, _content, datetime.datetime.now(),Users, "Notice Post by Admin", logindetails["userid"], ip)
            #msglist.append(result[1])
            print "--------------"
            print result
            
            if(result["result"]==-2):
                return HttpResponseRedirect('/user/login')
            elif(result["result"]==1):
                messages.info(HttpRequest, "Notice Posted Successfully")
            else:
                messages.error(HttpRequest, result)
            return HttpResponseRedirect('/message/')
            print "here"
        except Exception as inst:
            LogUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'NoticePost'))
            messages.error(HttpRequest,'Some Error has occoured here')
            return HttpResponseRedirect('/message/')    
