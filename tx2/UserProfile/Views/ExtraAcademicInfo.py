'''
Created on 01-Aug-2012

@author: jivjot
'''
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerSecurity
from tx2.UserProfile.BusinessFunctions.ExtraAcademicInfo import ExtraAcademicInfo
import logging
Logger_User = logging.getLogger(LoggerSecurity)

def ExtraAcdemicInfoTypeIndex(HttpRequest):
    return render_to_response("UserProfile/ExtraAcdemicInfoType.html",context_instance=RequestContext(HttpRequest))
def ExtraAcdemicInfoTypeInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "ExtraAcdemicInfoTypeName" in HttpRequest.POST:
            ExtraAcademicInfoTypeName=HttpRequest.POST["ExtraAcdemicInfoTypeName"]
        else:
            msglist.append("Error fetching data from form for ExtraAcdemicInfoTypeName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=ExtraAcademicInfoObj.InsertExtraAcademicInfoType(ExtraAcademicInfoTypeName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
def FunctionalAreaTypeIndex(HttpRequest):
    return render_to_response("UserProfile/FunctionalAreaType.html",context_instance=RequestContext(HttpRequest))
def FunctionalAreaTypeInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "FunctionalAreaTypeName" in HttpRequest.POST:
            FunctionalAreaTypeName=HttpRequest.POST["FunctionalAreaTypeName"]
        else:
            msglist.append("Error fetching data from form for ExtraAcdemicInfoTypeName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=ExtraAcademicInfoObj.InsertFunctionalAreaType(FunctionalAreaTypeName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
