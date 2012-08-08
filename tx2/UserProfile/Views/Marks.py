'''
Created on 26-Jul-2012

@author: jivjot
'''
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerSecurity
from tx2.UserProfile.BusinessFunctions.Marks import Marks
from tx2.UserProfile.models import Board
from tx2.UserProfile.models import DegreeType
import logging
Logger_User = logging.getLogger(LoggerSecurity)


def BoardIndex(HttpRequest):
    return render_to_response("UserProfile/Board.html",context_instance=RequestContext(HttpRequest))
def DegreeTypeIndex(HttpRequest):
    return render_to_response("UserProfile/DegreeType.html",context_instance=RequestContext(HttpRequest))
def DegreeIndex(HttpRequest):
    return render_to_response("UserProfile/Degree.html",context_instance=RequestContext(HttpRequest))
def SessionTypeIndex(HttpRequest):
    return render_to_response("UserProfile/SessionType.html",context_instance=RequestContext(HttpRequest))
def MarksIndex(HttpRequest):
    return render_to_response("UserProfile/Marks.html",context_instance=RequestContext(HttpRequest))

def BoardInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "BoardName" in HttpRequest.POST:
            BoardName=HttpRequest.POST["BoardName"]
        else:
            msglist.append("Error fetching data from form for BoardName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.InsertBoard(BoardName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
def DegreeTypeInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeTypeName" in HttpRequest.POST:
            DegreeTypeName=HttpRequest.POST["DegreeTypeName"]
        else:
            msglist.append("Error fetching data from form for DegreeTypeName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.InsertDegreeType(DegreeTypeName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
def DegreeInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeName" in HttpRequest.POST:
            DegreeName=HttpRequest.POST["DegreeName"]
        else:
            msglist.append("Error fetching data from form for DegreeName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.InsertDegree(DegreeName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
def SessionTypeInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "SessionTypeName" in HttpRequest.POST:
            SessionTypeName=HttpRequest.POST["SessionTypeName"]
        else:
            msglist.append("Error fetching data from form for SessionTypeName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.InsertSessionType(SessionTypeName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
def MarksInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "SessionStart" in HttpRequest.POST:
            SessionStart=HttpRequest.POST["SessionStart"]
        else:
            msglist.append("Error fetching data from form for SessionStart");
            flag=-1;
        if "SessionEnd" in HttpRequest.POST:
            SessionEnd=HttpRequest.POST["SessionEnd"]
        else:
            msglist.append("Error fetching data from form for SessionEnd");
            flag=-1;
        if "SessionNumber" in HttpRequest.POST:
            SessionNumber=HttpRequest.POST["SessionNumber"]
        else:
            msglist.append("Error fetching data from form for SessionNumber");
            flag=-1;
        if "SessionType" in HttpRequest.POST:
            SessionType=HttpRequest.POST["SessionType"]
        else:
            msglist.append("Error fetching data from form for SessionType");
            flag=-1;
        if "TotaMarks" in HttpRequest.POST:
            TotaMarks=HttpRequest.POST["TotaMarks"]
        else:
            msglist.append("Error fetching data from form for TotaMarks");
            flag=-1;
        if "SecuredMarks" in HttpRequest.POST:
            SecuredMarks=HttpRequest.POST["SecuredMarks"]
        else:
            msglist.append("Error fetching data from form for SecuredMarks");
            flag=-1;
        if "TotalReappears" in HttpRequest.POST:
            TotalReappears=HttpRequest.POST["TotalReappears"]
        else:
            msglist.append("Error fetching data from form for TotalReappears");
            flag=-1;
        if "ReappearsRemaining" in HttpRequest.POST:
            ReappearsRemaining=HttpRequest.POST["ReappearsRemaining"]
        else:
            msglist.append("Error fetching data from form for ReappearsRemaining");
            flag=-1;
        if "DegreeType" in HttpRequest.POST:
            DegreeType=HttpRequest.POST["DegreeType"]
        else:
            msglist.append("Error fetching data from form for DegreeType");
            flag=-1;
        if "Board" in HttpRequest.POST:
            Board=HttpRequest.POST["Board"]
        else:
            msglist.append("Error fetching data from form for Board");
            flag=-1;
        if "Degree" in HttpRequest.POST:
            Degree=HttpRequest.POST["Degree"]
        else:
            msglist.append("Error fetching data from form for Degree");
            flag=-1;
        if "UserId" in HttpRequest.POST:
            UserId=HttpRequest.POST["UserId"]
        else:
            msglist.append("Error fetching data from form for UserId");
            flag=-1;
                            
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        
        result=MarksObj.InsertMarks(SessionStart, SessionEnd, SessionNumber, SessionType, TotaMarks, SecuredMarks, TotalReappears, ReappearsRemaining, DegreeType, Board, Degree, UserId,logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y

def BoardSelect(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        mylist=Board.objects.all()
        
        return render_to_response("UserProfile/ViewData.html",{'mydata':mylist,})
        
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
def DegreeTypeSelect(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        mylist=DegreeType.objects.all()
        
        return render_to_response("UserProfile/ViewData.html",{'mydata':mylist,})
        
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y


def BoardDelete(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "BoardId" in HttpRequest.POST:
            BoardId=HttpRequest.POST["BoardId"]
        else:
            msglist.append("Error fetching data from form for BoardId");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.DeleteBoard(BoardId, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y

def DegreeTypeDelete(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeTypeId" in HttpRequest.POST:
            DegreeTypeId=HttpRequest.POST["DegreeTypeId"]
        else:
            msglist.append("Error fetching data from form for DegreeTypeId");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.DeleteDegreeType(DegreeTypeId, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y


def BoardUpdate(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "BoardName" in HttpRequest.POST:
            BoardName=HttpRequest.POST["BoardName"]
        else:
            msglist.append("Error fetching data from form for BoardName");
            flag=-1;
        if "BoardId" in HttpRequest.POST:
            BoardId=HttpRequest.POST["BoardId"]
        else:
            msglist.append("Error fetching data from form for BoardId");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.UpdateBoard(BoardId,BoardName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y

def DegreeTypeUpdate(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeTypeId" in HttpRequest.POST:
            DegreeTypeId=HttpRequest.POST["DegreeTypeId"]
        else:
            msglist.append("Error fetching data from form for DegreeTypeId");
            flag=-1;
        if "DegreeTypeName" in HttpRequest.POST:
            DegreeTypeName=HttpRequest.POST["DegreeTypeName"]
        else:
            msglist.append("Error fetching data from form for DegreeTypeName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.UpdateDegreeType(DegreeTypeId, DegreeTypeName,logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
         
        
def DegreeUpdate(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeId" in HttpRequest.POST:
            DegreeId=HttpRequest.POST["DegreeId"]
        else:
            msglist.append("Error fetching data from form for DegreeId");
            flag=-1;
        if "DegreeName" in HttpRequest.POST:
            DegreeName=HttpRequest.POST["DegreeName"]
        else:
            msglist.append("Error fetching data from form for DegreeName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.UpdateDegree(DegreeId, DegreeName,logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
        
        
        
        