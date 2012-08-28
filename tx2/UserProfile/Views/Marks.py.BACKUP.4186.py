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
from tx2.UserProfile.models import Board, SessionType, StudentDetails
from tx2.UserProfile.models import DegreeType
from tx2.UserProfile.models import Degree
from tx2.UserProfile.models import Marks as modelMarks
from django.contrib import messages
from tx2.Misc.MIscFunctions1 import is_integer
import logging
import inspect
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
  msglist = AppendMessageList(HttpRequest)
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
    msglist.append('Please Login to continue')
    HttpRequest.session[SESSION_MESSAGE] = msglist
    return HttpResponseRedirect('/user/login/')
  else:
    if( StudentDetails.objects.filter(User=logindetails["userid"]).exists()):
        StudDetailStatus= True
    else:
        StudDetailStatus= False
    return render_to_response("UserProfile/MarksCategory.html",context_instance=RequestContext(HttpRequest))

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
def MarksSave(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        flag=1
        v="";
        if "v" in HttpRequest.GET:
            v=HttpRequest.GET["v"]
        else:
            messages.error(HttpRequest,'Error fetching details.')
            flag=-1;
        if(v=="10th"):
          SessionYearlyId=SessionType.objects.get(Name='Yearly').id;
          DegreeTypeId10th=DegreeType.objects.get(Name="10th").id;
          DegreeId10th=Degree.objects.get(Name="10th").id;
          HttpRequest.session['SessionNumber']=1;
          HttpRequest.session['SessionType']=SessionYearlyId;
          HttpRequest.session['DegreeType']=DegreeTypeId10th;
          HttpRequest.session['Degree']=DegreeId10th;
        elif(v=="12th"):
          SessionYearlyId=SessionType.objects.get(Name='Yearly').id;
          DegreeTypeId12th=DegreeType.objects.get(Name="12th").id;
          DegreeId12th=Degree.objects.get(Name="12th").id;
          HttpRequest.session['SessionNumber']=1;
          HttpRequest.session['SessionType']=SessionYearlyId;
          HttpRequest.session['DegreeType']=DegreeTypeId12th;
          HttpRequest.session['Degree']=DegreeId12th;
        elif(v.find("Semester")!=-1):
          SessionSemesterId=SessionType.objects.get(Name='Semester').id;
          DegreeTypeIdUG=DegreeType.objects.get(Name="undergraduation").id;
          DegreeIdBE=Degree.objects.get(Name="B.E.").id;
          HttpRequest.session['SessionNumber']=int(v.split("Semester")[1]);
          HttpRequest.session['SessionType']=SessionSemesterId;
          HttpRequest.session['DegreeType']=DegreeTypeIdUG;
          HttpRequest.session['Degree']=DegreeIdBE;
        else:
<<<<<<< HEAD
           messages.error(HttpRequest,"Error: invalid url")
           flag=-1;
=======
          messages.error(HttpRequest,"Error: invalid url")
          flag=-1;
>>>>>>> 165c90ec2b97f99f50dde87513a4c20b4b8fd0e3
        if flag==-1:
            return render_to_response("UserProfile/Message.html")
        Boardobj=Board.objects.all();
        yearlist=range(1985,2014);
        relist=range(0,20);
        return render_to_response("UserProfile/MarksSave.html",{'BoardObject':Boardobj,'yearlist':yearlist,'relist':relist},context_instance=RequestContext(HttpRequest))
    except Exception, ex:
<<<<<<< HEAD
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
=======
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          messages.error(HttpRequest,'ERROR: ' + str(ex))
    return HttpResponseRedirect('/message/')
>>>>>>> 165c90ec2b97f99f50dde87513a4c20b4b8fd0e3

def MarksPostSave(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'ERROR : Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "SessionStartMonth" in HttpRequest.POST:
            SessionStartMonth=HttpRequest.POST["SessionStartMonth"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionStartMonth')
            msglist.append("Error fetching data from form for SessionStartMonth");
            flag=-1;
        if "SessionStartYear" in HttpRequest.POST:
            SessionStartYear=HttpRequest.POST["SessionStartYear"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionStartYear')
            flag=-1;
        if(flag!=-1):
          SessionStart="1 "+SessionStartMonth+" "+SessionStartYear; 
        if "SessionEndMonth" in HttpRequest.POST:
            SessionEndMonth=HttpRequest.POST["SessionEndMonth"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionEndMonth')
            msglist.append("Error fetching data from form for SessionEndMonth");
            flag=-1;
        if "SessionEndYear" in HttpRequest.POST:
            SessionEndYear=HttpRequest.POST["SessionEndYear"]
        else:
          messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionEndYear')
          msglist.append("Error fetching data from form for SessionEndYear");
          flag=-1;
        if(flag!=-1):
          SessionEnd="1 "+SessionEndMonth+" "+SessionEndYear;
        if "SessionNumber" in HttpRequest.session:
            _SessionNumber=HttpRequest.session["SessionNumber"]
        else:
          messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionNumber')
          msglist.append("Error fetching data from form for SessionNumber");
          flag=-1;
        if "SessionType" in HttpRequest.session:
            SessionType=HttpRequest.session["SessionType"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionType')
            msglist.append("Error fetching data from form for SessionType");
            flag=-1;
        if "TotalMarks" in HttpRequest.POST:
            TotaMarks=HttpRequest.POST["TotalMarks"]
            if is_integer(TotaMarks):
              TotaMarks=int(TotaMarks)
            else:
              messages.error(HttpRequest,'ERROR : TotaMarks should be a number')
              msglist.append("TotaMarks should be a number");
              flag=-1;
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for TotaMarks')
              
            msglist.append("Error fetching data from form for TotaMarks");
            flag=-1;
        if "SecuredMarks" in HttpRequest.POST:
            SecuredMarks=HttpRequest.POST["SecuredMarks"]
            if is_integer(SecuredMarks):
              SecuredMarks=int(SecuredMarks)
            else:
              messages.error(HttpRequest,'ERROR : SecuredMarks should be a number')
              msglist.append("SecuredMarks should be a number");
              flag=-1;
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SecuredMarks')
            msglist.append("Error fetching data from form for SecuredMarks");
            flag=-1;
        if "TotalReapears" in HttpRequest.POST:
            TotalReappears=HttpRequest.POST["TotalReapears"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for TotalReappears')
            msglist.append("Error fetching data from form for TotalReappears");
            flag=-1;
        if "RepearsRemaining" in HttpRequest.POST:
            ReappearsRemaining=HttpRequest.POST["RepearsRemaining"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for ReappearsRemaining')
            msglist.append("Error fetching data from form for RepearsRemaining");
            flag=-1;
        if "DegreeType" in HttpRequest.session:
            DegreeType=HttpRequest.session["DegreeType"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for DegreeType')
            msglist.append("Error fetching data from form for DegreeType");
            flag=-1;
        if "Board" in HttpRequest.POST:
            Boardid=HttpRequest.POST["Board"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for Board')
            msglist.append("Error fetching data from form for Board");
            flag=-1;
        if "Degree" in HttpRequest.session:
            _Degree=HttpRequest.session["Degree"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for Degree')
            msglist.append("Error fetching data from form for Degree");
            flag=-1;
        Boardobj=Board.objects.all();
        yearlist=range(1985,2014);
        relist=range(0,20);
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/MarksSave.html",{'BoardObject':Boardobj,'yearlist':yearlist,'relist':relist},context_instance=RequestContext(HttpRequest))
        if(modelMarks.objects.filter(SessionNumber=_SessionNumber,Degree=_Degree,UserId=logindetails["userid"]).count()==0):
          result=MarksObj.InsertMarks(SessionStart, SessionEnd, _SessionNumber, SessionType, TotaMarks, SecuredMarks, TotalReappears, ReappearsRemaining, DegreeType, Boardid, _Degree, logindetails["userid"],logindetails["userid"], ip)
        else:
          _id=modelMarks.objects.get(SessionNumber=_SessionNumber,Degree=_Degree,UserId=logindetails["userid"]).id;
          result=MarksObj.UpdateMarks(_id,SessionStart, SessionEnd, _SessionNumber, SessionType, TotaMarks, SecuredMarks, TotalReappears, ReappearsRemaining, DegreeType, Boardid, _Degree, logindetails["userid"],logindetails["userid"], ip)
        
        msglist.append("result is %s"%result);
        if(result['result']==1):
          messages.info(HttpRequest,"SUCCESS")
        else:
          messages.info(HttpRequest,"Error Occured please try again")
        return render_to_response("UserProfile/MarksSave.html",{'BoardObject':Boardobj,'yearlist':yearlist,'relist':relist},context_instance=RequestContext(HttpRequest))
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
def MarksUpdate(HttpRequest):
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
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            msglist.append("Error fetching data from form for SessionStart");
            flag=-1;
        
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
        
        result=MarksObj.UpdateMarks(Id,SessionStart, SessionEnd, SessionNumber, SessionType, TotaMarks, SecuredMarks, TotalReappears, ReappearsRemaining, DegreeType, Board, Degree, UserId,logindetails["userid"], ip)
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
        
def SessionTypeUpdate(HttpRequest):
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
        if "SessionTypeId" in HttpRequest.POST:
            SessionTypeId=HttpRequest.POST["SessionTypeId"]
        else:
            msglist.append("Error fetching data from form for SessionTypeId");
            flag=-1;
        if "SessionTypeName" in HttpRequest.POST:
            SessionTypeName=HttpRequest.POST["SessionTypeName"]
        else:
            msglist.append("Error fetching data from form for SessionTypeName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=MarksObj.UpdateSessionType(SessionTypeId, SessionTypeName,logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
        
        
        
