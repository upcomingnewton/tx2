'''
Created on 06-Aug-2012

@author: jivjot
'''
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerSecurity
from tx2.UserProfile.BusinessFunctions.UserProfileMisc import UserProfileMisc
import logging
Logger_User = logging.getLogger(LoggerSecurity)

def MedicalInfoIndex(HttpRequest):
    return render_to_response("UserProfile/MedicalInfo.html",context_instance=RequestContext(HttpRequest))
def MedicalInfoInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileMiscObj=UserProfileMisc()
        flag=1
        if "User_id" in HttpRequest.POST:
            User_id=HttpRequest.POST["User_id"]
        else:
            msglist.append("Error fetching data from form for User_id");
            flag=-1;
        if "Height" in HttpRequest.POST:
            Height=HttpRequest.POST["Height"]
        else:
            msglist.append("Error fetching data from form for Height");
            flag=-1;
        if "Weight" in HttpRequest.POST:
            Weight=HttpRequest.POST["Weight"]
        else:
            msglist.append("Error fetching data from form for Weight");
            flag=-1;
        if "LeftEye" in HttpRequest.POST:
            LeftEye=HttpRequest.POST["LeftEye"]
        else:
            msglist.append("Error fetching data from form for LeftEye");
            flag=-1;
        if "RightEye" in HttpRequest.POST:
            RightEye=HttpRequest.POST["RightEye"]
        else:
            msglist.append("Error fetching data from form for RightEye");
            flag=-1;
        if "DisabilityInfo" in HttpRequest.POST:
            DisabilityInfo=HttpRequest.POST["DisabilityInfo"]
        else:
            msglist.append("Error fetching data from form for DisabilityInfo");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=UserProfileMiscObj.InsertMedicalInfo(User_id, Height, Weight, LeftEye, RightEye, DisabilityInfo, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y