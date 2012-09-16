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
LogUser = logging.getLogger(LoggerUser)


def adminNoticeIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    else:
        return render_to_response("Communication/Admin/PostNotices.html",{'type':['NOTICE'],'title':"Post Notice"},context_instance=RequestContext(HttpRequest))

def adminNewsIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    else:
        msglist.append('News')
        return render_to_response("Communication/Admin/PostNotices.html",{'type':['NEWS'],'title':"Post News"},context_instance=RequestContext(HttpRequest))

def adminNewsPost(HttpRequest):
    
    msglist = AppendMessageList(HttpRequest)
    logindetails = GetLoginDetails(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    

    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
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
            result= comm_call.PostNews(title, _content, tstamp,logindetails["userid"],ip)
            print result
            if(result["result"]==-2):
                return HttpResponseRedirect('/user/login')
            elif(result["result"]==1):
                msglist.append("Notice Posted Successfully")
            else:
                msglist.append(result[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            print msglist
            return HttpResponseRedirect('/message/')
            
        except Exception as inst:
            LogUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'NoticePost'))
            msglist.append('Some Error has occoured')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')    

def adminNoticePost(HttpRequest):
    
    msglist = AppendMessageList(HttpRequest)
    logindetails = GetLoginDetails(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']

    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    else:
        try:
            comm_call=CommunicationFunctions.PostCommunicationFnx()
            title= HttpRequest.POST['Title']
            _content=HttpRequest.POST['Content']
            
            Users='0'
            
            result= comm_call.PostNotice(title, _content, datetime.datetime.now(),Users, "Notice Post by Admin", logindetails["userid"], ip)
            #msglist.append(result[1])
            if(result[1]["result"]==-2):
                return HttpResponseRedirect('/user/login')
            elif(result[1]["result"]==1):
                msglist.append("Notice Posted Successfully")
            else:
                msglist.append(result[1])
            #print msglist
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
            
        except Exception as inst:
            LogUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'NoticePost'))
            msglist.append('Some Error has occoured')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')    
        
