'''
Created on 26-Jul-2012

@author: jivjot
'''
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  LOGGER_USER_PROFILE
from tx2.UserProfile.BusinessFunctions.Marks import Marks
from tx2.UserProfile.models import Board, SessionType, StudentDetails
from tx2.UserProfile.models import DegreeType
from tx2.UserProfile.models import Degree
from tx2.UserProfile.models import Marks as modelMarks
from django.contrib import messages
from tx2.Misc.MIscFunctions1 import is_integer
import logging
import inspect
import datetime
Logger_User = logging.getLogger(LOGGER_USER_PROFILE)


def BoardIndex(HttpRequest):
    return render_to_response("UserProfile/Board.html",context_instance=RequestContext(HttpRequest))
def DegreeTypeIndex(HttpRequest):
    return render_to_response("UserProfile/DegreeType.html",context_instance=RequestContext(HttpRequest))
def DegreeIndex(HttpRequest):
    return render_to_response("UserProfile/Degree.html",context_instance=RequestContext(HttpRequest))
def SessionTypeIndex(HttpRequest):
    return render_to_response("UserProfile/SessionType.html",context_instance=RequestContext(HttpRequest))
def MarksIndex(HttpRequest):
  logindetails = GetLoginDetails(HttpRequest)
  if( logindetails["userid"] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  else:
    if( StudentDetails.objects.filter(User=logindetails["userid"]).exists()):
        return render_to_response("UserProfile/MarksCategory.html",{},context_instance=RequestContext(HttpRequest))
    else:
        messages.error(HttpRequest,'Please fill in your students details first.')
        return HttpResponseRedirect('/userprofile/UserProfile/StudentDetails/')

def BoardInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "BoardName" in HttpRequest.POST:
            BoardName=HttpRequest.POST["BoardName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for BoardName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.InsertBoard(BoardName, logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
def DegreeTypeInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeTypeName" in HttpRequest.POST:
            DegreeTypeName=HttpRequest.POST["DegreeTypeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for DegreeTypeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.InsertDegreeType(DegreeTypeName, logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def DegreeInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeName" in HttpRequest.POST:
            DegreeName=HttpRequest.POST["DegreeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for DegreeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.InsertDegree(DegreeName, logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def SessionTypeInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "SessionTypeName" in HttpRequest.POST:
            SessionTypeName=HttpRequest.POST["SessionTypeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for SessionTypeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.InsertSessionType(SessionTypeName, logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def MarksSave(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        flag=1
        v="";
        Message_MarksFillingFor = ''
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
          Message_MarksFillingFor = 'class 10th'
          
        elif(v=="12th"):
          SessionYearlyId=SessionType.objects.get(Name='Yearly').id;
          DegreeTypeId12th=DegreeType.objects.get(Name="12th").id;
          DegreeId12th=Degree.objects.get(Name="12th").id;
          HttpRequest.session['SessionNumber']=1;
          HttpRequest.session['SessionType']=SessionYearlyId;
          HttpRequest.session['DegreeType']=DegreeTypeId12th;
          HttpRequest.session['Degree']=DegreeId12th;
          Message_MarksFillingFor = 'class 12th'
        elif(v.find("Semester")!=-1):
          SessionSemesterId=SessionType.objects.get(Name='Semester').id;
          DegreeTypeIdUG=DegreeType.objects.get(Name="undergraduation").id;
          DegreeIdBE=Degree.objects.get(Name="B.E.").id;
          HttpRequest.session['SessionNumber']=int(v.split("Semester")[1]);
          HttpRequest.session['SessionType']=SessionSemesterId;
          HttpRequest.session['DegreeType']=DegreeTypeIdUG;
          HttpRequest.session['Degree']=DegreeIdBE;
          Message_MarksFillingFor = 'semester ' + str(v.split("Semester")[1])
        else:
          messages.error(HttpRequest,"Error: invalid url")
          flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        HttpRequest.session['Message_MarksFillingFor'] = Message_MarksFillingFor
        
        ############
        try:
          MarksObj = modelMarks.objects.get(SessionNumber=HttpRequest.session['SessionNumber'],Degree=HttpRequest.session['Degree'],UserId=logindetails["userid"],SessionType=HttpRequest.session['SessionType'])
          HttpRequest.session['MarksObjExists'] = MarksObj.id
        except ObjectDoesNotExist:
          MarksObj = False
          HttpRequest.session['MarksObjExists'] = -1
        
        Boardobj=Board.objects.all();
        yearlist=range(1985,2014);
        relist=range(0,20);
        messages.error(HttpRequest,"You are filling marks for %s" % (Message_MarksFillingFor))
        return render_to_response("UserProfile/MarksSave.html",{'BoardObject':Boardobj,'yearlist':yearlist,'relist':relist,'MarksObj':MarksObj},context_instance=RequestContext(HttpRequest))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def MarksPostSave(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'ERROR : Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "SessionStartMonth" in HttpRequest.POST:
            SessionStartMonth=HttpRequest.POST["SessionStartMonth"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionStartMonth')
            flag=-1;
        if "SessionStartYear" in HttpRequest.POST:
            SessionStartYear=HttpRequest.POST["SessionStartYear"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionStartYear')
            flag=-1;
        if(flag!=-1):
#          datetime.date.
          #datetime.date(int(SessionStartYear),int(SessionStartMonth),1)
          SessionStart= "1 "+SessionStartMonth+" "+SessionStartYear; 
        if "SessionEndMonth" in HttpRequest.POST:
            SessionEndMonth=HttpRequest.POST["SessionEndMonth"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionEndMonth')
            flag=-1;
        if "SessionEndYear" in HttpRequest.POST:
            SessionEndYear=HttpRequest.POST["SessionEndYear"]
        else:
          messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionEndYear')
          flag=-1;
        if(flag!=-1):
          SessionEnd="1 "+SessionEndMonth+" "+SessionEndYear;
        if "SessionNumber" in HttpRequest.session:
            _SessionNumber=HttpRequest.session["SessionNumber"]
            del HttpRequest.session['SessionNumber']
        else:
          messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionNumber')
          flag=-1;
        if "SessionType" in HttpRequest.session:
            SessionType=HttpRequest.session["SessionType"]
            del HttpRequest.session["SessionType"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SessionType')
            flag=-1;
        if "TotalMarks" in HttpRequest.POST:
            TotaMarks=HttpRequest.POST["TotalMarks"]
            if is_integer(TotaMarks):
              TotaMarks=int(TotaMarks)
            else:
              messages.error(HttpRequest,'ERROR : TotaMarks should be a number')
              flag=-1;
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for TotaMarks')
            flag=-1;
        if "SecuredMarks" in HttpRequest.POST:
            SecuredMarks=HttpRequest.POST["SecuredMarks"]
            if is_integer(SecuredMarks):
              SecuredMarks=int(SecuredMarks)
            else:
              messages.error(HttpRequest,'ERROR : SecuredMarks should be a number')
              flag=-1;
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for SecuredMarks')
            flag=-1;
        if "TotalReapears" in HttpRequest.POST:
            TotalReappears=HttpRequest.POST["TotalReapears"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for TotalReappears')
            flag=-1;
        if "RepearsRemaining" in HttpRequest.POST:
            ReappearsRemaining=HttpRequest.POST["RepearsRemaining"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for ReappearsRemaining')
            flag=-1;
        if "DegreeType" in HttpRequest.session:
            DegreeType=HttpRequest.session["DegreeType"]
            del HttpRequest.session["DegreeType"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for DegreeType')
            flag=-1;
        if "Board" in HttpRequest.POST:
            Boardid=HttpRequest.POST["Board"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for Board')
            flag=-1;
        if "Degree" in HttpRequest.session:
            _Degree=HttpRequest.session["Degree"]
            del HttpRequest.session["Degree"]
        else:
            messages.error(HttpRequest,'ERROR : Error fetching data from form for Degree')
            flag=-1;
        Boardobj=Board.objects.all();
        yearlist=range(1985,2014);
        relist=range(0,20);
        if flag==-1:
            return HttpResponseRedirect('/message/')
        if 'MarksObjExists' in HttpRequest.session:
          if(HttpRequest.session['MarksObjExists'] == -1):
            result=MarksObj.InsertMarks(SessionStart, SessionEnd, _SessionNumber, SessionType, TotaMarks, SecuredMarks, TotalReappears, ReappearsRemaining, DegreeType, Boardid, _Degree, logindetails["userid"],logindetails["userid"], ip)
          else:
            result=MarksObj.UpdateMarks(HttpRequest.session['MarksObjExists'],SessionStart, SessionEnd, _SessionNumber, SessionType, TotaMarks, SecuredMarks, TotalReappears, ReappearsRemaining, DegreeType, Boardid, _Degree, logindetails["userid"],logindetails["userid"], ip)
          del HttpRequest.session['MarksObjExists']
        else:
          if(modelMarks.objects.filter(SessionNumber=_SessionNumber,Degree=_Degree,UserId=logindetails["userid"]).count()==0):
            result=MarksObj.InsertMarks(SessionStart, SessionEnd, _SessionNumber, SessionType, TotaMarks, SecuredMarks, TotalReappears, ReappearsRemaining, DegreeType, Boardid, _Degree, logindetails["userid"],logindetails["userid"], ip)
          else:
            _id=modelMarks.objects.get(SessionNumber=_SessionNumber,Degree=_Degree,UserId=logindetails["userid"]).id;
            result=MarksObj.UpdateMarks(_id,SessionStart, SessionEnd, _SessionNumber, SessionType, TotaMarks, SecuredMarks, TotalReappears, ReappearsRemaining, DegreeType, Boardid, _Degree, logindetails["userid"],logindetails["userid"], ip)
        if(result['result']==1):
          messages.info(HttpRequest,"SUCCESS.Your details have been recorded for %s" % (HttpRequest.session['Message_MarksFillingFor']))
        else:
          messages.info(HttpRequest,"Some Error Occured please try again")
        if 'Message_MarksFillingFor' in HttpRequest.session:
          del HttpRequest.session['Message_MarksFillingFor']
        return HttpResponseRedirect('/userprofile/Marks/Marks/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

      
def MarksUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        
        flag=1
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for SessionStart");
            flag=-1;
        
        if "SessionStart" in HttpRequest.POST:
            SessionStart=HttpRequest.POST["SessionStart"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for SessionStart");
            flag=-1;
        if "SessionEnd" in HttpRequest.POST:
            SessionEnd=HttpRequest.POST["SessionEnd"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for SessionEnd");
            flag=-1;
        if "SessionNumber" in HttpRequest.POST:
            SessionNumber=HttpRequest.POST["SessionNumber"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for SessionNumber");
            flag=-1;
        if "SessionType" in HttpRequest.POST:
            SessionType=HttpRequest.POST["SessionType"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for SessionType");
            flag=-1;
        if "TotaMarks" in HttpRequest.POST:
            TotaMarks=HttpRequest.POST["TotaMarks"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for TotaMarks");
            flag=-1;
        if "SecuredMarks" in HttpRequest.POST:
            SecuredMarks=HttpRequest.POST["SecuredMarks"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for SecuredMarks");
            flag=-1;
        if "TotalReappears" in HttpRequest.POST:
            TotalReappears=HttpRequest.POST["TotalReappears"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for TotalReappears");
            flag=-1;
        if "ReappearsRemaining" in HttpRequest.POST:
            ReappearsRemaining=HttpRequest.POST["ReappearsRemaining"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for ReappearsRemaining");
            flag=-1;
        if "DegreeType" in HttpRequest.POST:
            DegreeType=HttpRequest.POST["DegreeType"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for DegreeType");
            flag=-1;
        if "Board" in HttpRequest.POST:
            Board=HttpRequest.POST["Board"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Board");
            flag=-1;
        if "Degree" in HttpRequest.POST:
            Degree=HttpRequest.POST["Degree"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Degree");
            flag=-1;
        if "UserId" in HttpRequest.POST:
            UserId=HttpRequest.POST["UserId"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for UserId");
            flag=-1;
                            
        if flag==-1:
            return HttpResponseRedirect('/message/')
        
        result=MarksObj.UpdateMarks(Id,SessionStart, SessionEnd, SessionNumber, SessionType, TotaMarks, SecuredMarks, TotalReappears, ReappearsRemaining, DegreeType, Board, Degree, UserId,logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def BoardSelect(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        mylist=Board.objects.all()
        
        return render_to_response("UserProfile/ViewData.html",{'mydata':mylist,})
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
      
def DegreeTypeSelect(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        mylist=DegreeType.objects.all()
        
        return render_to_response("UserProfile/ViewData.html",{'mydata':mylist,})
        
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')


def BoardDelete(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "BoardId" in HttpRequest.POST:
            BoardId=HttpRequest.POST["BoardId"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for BoardId");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.DeleteBoard(BoardId, logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def DegreeTypeDelete(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeTypeId" in HttpRequest.POST:
            DegreeTypeId=HttpRequest.POST["DegreeTypeId"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for DegreeTypeId");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.DeleteDegreeType(DegreeTypeId, logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')


def BoardUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "BoardName" in HttpRequest.POST:
            BoardName=HttpRequest.POST["BoardName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for BoardName");
            flag=-1;
        if "BoardId" in HttpRequest.POST:
            BoardId=HttpRequest.POST["BoardId"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for BoardId");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.UpdateBoard(BoardId,BoardName, logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def DegreeTypeUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeTypeId" in HttpRequest.POST:
            DegreeTypeId=HttpRequest.POST["DegreeTypeId"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for DegreeTypeId");
            flag=-1;
        if "DegreeTypeName" in HttpRequest.POST:
            DegreeTypeName=HttpRequest.POST["DegreeTypeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for DegreeTypeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.UpdateDegreeType(DegreeTypeId, DegreeTypeName,logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
         
        
def DegreeUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "DegreeId" in HttpRequest.POST:
            DegreeId=HttpRequest.POST["DegreeId"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for DegreeId");
            flag=-1;
        if "DegreeName" in HttpRequest.POST:
            DegreeName=HttpRequest.POST["DegreeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for DegreeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.UpdateDegree(DegreeId, DegreeName,logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
        
def SessionTypeUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        MarksObj=Marks()
        flag=1
        if "SessionTypeId" in HttpRequest.POST:
            SessionTypeId=HttpRequest.POST["SessionTypeId"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for SessionTypeId");
            flag=-1;
        if "SessionTypeName" in HttpRequest.POST:
            SessionTypeName=HttpRequest.POST["SessionTypeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for SessionTypeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=MarksObj.UpdateSessionType(SessionTypeId, SessionTypeName,logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
        
        
        
