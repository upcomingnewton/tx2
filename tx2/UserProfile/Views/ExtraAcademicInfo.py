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

def ExtraAcademicInfoDetailsIndex(HttpRequest):
    return render_to_response("UserProfile/ExtraAcademicInfoDetails.html",context_instance=RequestContext(HttpRequest))
def ExtraAcademicInfoDetailsInsert(HttpRequest):
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
        if "User_id" in HttpRequest.POST:
            User_id=HttpRequest.POST["User_id"]
        else:
            msglist.append("Error fetching data from form for ExtraAcdemicInfoTypeName");
            flag=-1;
        if "Title" in HttpRequest.POST:
            Title=HttpRequest.POST["Title"]
        else:
            msglist.append("Error fetching data from form for Title");
            flag=-1;
        if "Start" in HttpRequest.POST:
            Start=HttpRequest.POST["Start"]
        else:
            msglist.append("Error fetching data from form for Start");
            flag=-1;
        if "End" in HttpRequest.POST:
            End=HttpRequest.POST["End"]
        else:
            msglist.append("Error fetching data from form for End");
            flag=-1;
        if "Organisation" in HttpRequest.POST:
            Organisation=HttpRequest.POST["Organisation"]
        else:
            msglist.append("Error fetching data from form for Organisation");
            flag=-1;    
        if "Designation" in HttpRequest.POST:
            Designation=HttpRequest.POST["Designation"]
        else:
            msglist.append("Error fetching data from form for Designation");
            flag=-1;
        if "Details" in HttpRequest.POST:
            Details=HttpRequest.POST["Details"]
        else:
            msglist.append("Error fetching data from form for Details");
            flag=-1;
        if "PlaceOfWork_id" in HttpRequest.POST:
            PlaceOfWork_id=HttpRequest.POST["PlaceOfWork_id"]
        else:
            msglist.append("Error fetching data from form for PlaceOfWork_id");
            flag=-1;
        if "FunctionalArea" in HttpRequest.POST:
            FunctionalArea=HttpRequest.POST["FunctionalArea"]
        else:
            msglist.append("Error fetching data from form for FunctionalArea");
            flag=-1;        
        if "ExtraAcadmicInfoType_id" in HttpRequest.POST:
            ExtraAcadmicInfoType_id=HttpRequest.POST["ExtraAcadmicInfoType_id"]
        else:
            msglist.append("Error fetching data from form for ExtraAcadmicInfoType_id");
            flag=-1;
        if "References" in HttpRequest.POST:
            References=HttpRequest.POST["References"]
        else:
            msglist.append("Error fetching data from form for References");
            flag=-1;
        if "Summary" in HttpRequest.POST:
            Summary=HttpRequest.POST["Summary"]
        else:
            msglist.append("Error fetching data from form for Summary");
            flag=-1;    
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=ExtraAcademicInfoObj.InsertExtraAcademicInfoDetails(User_id, Title, Start, End, Organisation, Designation, Details, PlaceOfWork_id, FunctionalArea, ExtraAcadmicInfoType_id, References, Summary, logindetails["userid"], ip);
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
