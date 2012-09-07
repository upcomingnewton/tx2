'''
Created on 01-Aug-2012

@author: jivjot
'''
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  LOGGER_USER_PROFILE
from tx2.UserProfile.BusinessFunctions.ExtraAcademicInfo import ExtraAcademicInfo
from django.contrib import messages
from tx2.UserProfile.models import ExtraAcademicInfoType
from tx2.UserProfile.models import ExtraAcademicInfoDetails 
import logging
import inspect
import datetime
from tx2.Misc.MIscFunctions1 import is_integer
from django.core.exceptions import ObjectDoesNotExist
Logger_User = logging.getLogger(LOGGER_USER_PROFILE)

def ExtraAcdemicInfoTypeIndex(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    
    try:
      return render_to_response("UserProfile/ExtraAcdemicInfoType.html",context_instance=RequestContext(HttpRequest))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def ExtraAcdemicInfoTypeInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "ExtraAcdemicInfoTypeName" in HttpRequest.POST:
            ExtraAcademicInfoTypeName=HttpRequest.POST["ExtraAcdemicInfoTypeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for ExtraAcdemicInfoTypeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=ExtraAcademicInfoObj.InsertExtraAcademicInfoType(ExtraAcademicInfoTypeName, logindetails["userid"], ip)
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
def ExtraAcdemicInfoTypeUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Id");
            flag=-1;
            
        if "ExtraAcdemicInfoTypeName" in HttpRequest.POST:
            ExtraAcademicInfoTypeName=HttpRequest.POST["ExtraAcdemicInfoTypeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for ExtraAcdemicInfoTypeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=ExtraAcademicInfoObj.UpdateExtraAcademicInfoType(Id, ExtraAcademicInfoTypeName, logindetails["userid"], ip);
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

def FunctionalAreaTypeIndex(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    
    return render_to_response("UserProfile/FunctionalAreaType.html",context_instance=RequestContext(HttpRequest))
def FunctionalAreaTypeInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "FunctionalAreaTypeName" in HttpRequest.POST:
            FunctionalAreaTypeName=HttpRequest.POST["FunctionalAreaTypeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for FunctionalAreaTypeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=ExtraAcademicInfoObj.InsertFunctionalAreaType(FunctionalAreaTypeName, logindetails["userid"], ip)
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
def FunctionalAreaTypeUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Id");
            flag=-1;
        
        if "FunctionalAreaTypeName" in HttpRequest.POST:
            FunctionalAreaTypeName=HttpRequest.POST["FunctionalAreaTypeName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for FunctionalAreaTypeName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=ExtraAcademicInfoObj.UpdateFunctionalAreaType(Id, FunctionalAreaTypeName, logindetails["userid"], ip)
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

def ExtraAcademicInfoDetailsIndex(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    try:
      
      if( logindetails["userid"] == -1):
          messages.error(HttpRequest,'Please Login to continue')
          return HttpResponseRedirect('/user/login/')
      yearlist=range(1985,2014);
      if 'v' in HttpRequest.GET:
        if is_integer(HttpRequest.GET['v']):
          _id=int(HttpRequest.GET['v'])
          try:
            obj=ExtraAcademicInfoDetails.objects.get(User=logindetails["userid"],id=_id)
            return render_to_response("UserProfile/ExtraAcademicInfoDetails.html",{'yearlist':yearlist,'ExtraAcadStatus':obj},context_instance=RequestContext(HttpRequest))
          except ObjectDoesNotExist:
            return render_to_response("UserProfile/ExtraAcademicInfoDetails.html",{'yearlist':yearlist,},context_instance=RequestContext(HttpRequest))
          
      
      else:
        return render_to_response("UserProfile/ExtraAcademicInfoDetails.html",{'yearlist':yearlist,},context_instance=RequestContext(HttpRequest))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
def ExtraAcademicInfoDetailsSelect(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    try:
      
      if( logindetails["userid"] == -1):
          messages.error(HttpRequest,'Please Login to continue')
          return HttpResponseRedirect('/user/login/')
      try:
        ObjList=ExtraAcademicInfoDetails.objects.filter(User=logindetails["userid"],State=1)
      except ObjectDoesNotExist:
        ObjList=[];
      return render_to_response("UserProfile/ExtraAcademicInfoDetailsSelect.html",{'ObjList':ObjList},context_instance=RequestContext(HttpRequest))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
def ExtraAcademicInfoDetailsDelete(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    try:
      
      if( logindetails["userid"] == -1):
          messages.error(HttpRequest,'Please Login to continue')
          return HttpResponseRedirect('/user/login/')
      if 'v' in HttpRequest.GET:
        if is_integer(HttpRequest.GET['v']):
          _id=int(HttpRequest.GET['v'])
          try:
            obj=ExtraAcademicInfoDetails.objects.get(User=logindetails["userid"],id=_id)
            ExtraAcademicInfoObj=ExtraAcademicInfo()
            result=ExtraAcademicInfoObj.DeleteExtraAcademicInfoDetails(_id,logindetails["userid"],logindetails["userid"], ip)
            if(result['result']==1):
              messages.info(HttpRequest,"Congrats Your details have been saved");
            elif(result['result']==2):
              messages.info(HttpRequest,"Does NOt Exist");
            elif(result['result']==-2):
              messages.error(HttpRequest,"You do not have the required privelege to this particular page.Either you do not have authenticated yourself or You have not completed your previous details ");
            else:
              messages.error(HttpRequest,"result is %s"%result);
              return HttpResponseRedirect('/message/')
            return HttpResponseRedirect('/message/')
          except ObjectDoesNotExist:
            messages.error(HttpRequest,"Does NOt Exist");
            return HttpResponseRedirect('/message/')
      
      else:
        messages.info(HttpRequest,"Does NOt Exist");
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def ExtraAcademicInfoDetailsInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "IsOrganisation" in HttpRequest.POST:
            isorganisation=1;
            ExtraAcadmicInfoType_id=ExtraAcademicInfoType.objects.get(Name='Organisation').id;
        else:
            isorganisation=0;
            ExtraAcadmicInfoType_id=ExtraAcademicInfoType.objects.get(Name='Personal').id;
        if "Title" in HttpRequest.POST:
            Title=HttpRequest.POST["Title"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Title");
            flag=-1;
        if "StartMonth" in HttpRequest.POST:
            StartMonth=HttpRequest.POST["StartMonth"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for StartMonth");
            flag=-1;
        if "StartYear" in HttpRequest.POST:
            StartYear=HttpRequest.POST["StartYear"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for StartYear");
            flag=-1;
        if flag!=-1:
          _Start="1 "+StartMonth+" "+StartYear;
        if "EndMonth" in HttpRequest.POST:
            EndMonth=HttpRequest.POST["EndMonth"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for EndMonth");
            flag=-1;
        if "EndYear" in HttpRequest.POST:
            EndYear=HttpRequest.POST["EndYear"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for EndYear");
            flag=-1;
        if flag!=-1:
          End="1 "+EndMonth+" "+EndYear;
        if "Organisation" in HttpRequest.POST and isorganisation==1:
            _Organisation=HttpRequest.POST["Organisation"]
        elif isorganisation==0:
            _Organisation=''
        
        else:
            messages.error(HttpRequest,"Error fetching data from form for Organisation");
            flag=-1;    
        if "Designation" in HttpRequest.POST and isorganisation==1:
            Designation=HttpRequest.POST["Designation"]
        elif isorganisation==0:
            Designation=''
        else:
            messages.error(HttpRequest,"Error fetching data from form for Designation");
            flag=-1;
        if "Details" in HttpRequest.POST and isorganisation==1:
            Details=HttpRequest.POST["Details"]
        elif isorganisation==0:
            Details=''
        
        else:
            messages.error(HttpRequest,"Error fetching data from form for Details");
            flag=-1;
        if "PlaceOfWork" in HttpRequest.POST and isorganisation==1:
            PlaceOfWork=HttpRequest.POST["PlaceOfWork"]
        elif isorganisation==0:
            PlaceOfWork=''
        else:
            messages.error(HttpRequest,"Error fetching data from form for PlaceOfWork");
            flag=-1;
        if "FunctionalArea" in HttpRequest.POST:
            FunctionalArea=HttpRequest.POST["FunctionalArea"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for FunctionalArea");
            flag=-1;        
        
        if "References" in HttpRequest.POST and isorganisation==1:
            References=HttpRequest.POST["References"]
        elif isorganisation==0:
          References=''
        else:
            messages.error(HttpRequest,"Error fetching data from form for References");
            flag=-1;
        if "Summary" in HttpRequest.POST:
            Summary=HttpRequest.POST["Summary"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Summary");
            flag=-1;    
        if flag==-1:
            return HttpResponseRedirect('/message/')
        if "Id" in HttpRequest.POST:
          _id=int(HttpRequest.POST["Id"])
          result=ExtraAcademicInfoObj.UpdateExtraAcademicInfoDetails(_id,logindetails["userid"], Title, _Start, End, _Organisation, Designation, Details, PlaceOfWork, FunctionalArea, ExtraAcadmicInfoType_id, References, Summary, logindetails["userid"], ip);
          if(result['result']==-2):
            messages.error(HttpRequest,"You do not have the required privelege to this particular page.Either you do not have authenticated yourself or You have not completed your previous details ");
          elif(result['result']==1):
              messages.info(HttpRequest,"Congrats Your details have been saved");
          elif(result['result']==-4):
              messages.error(HttpRequest,"Details does not exist");
          elif(result['result']==-3):
              messages.error(HttpRequest,"Already Exists");
          else:
            messages.error(HttpRequest,"result is %s"%result);
            return HttpResponseRedirect('/message/')
        else:
          result=ExtraAcademicInfoObj.InsertExtraAcademicInfoDetails(logindetails["userid"], Title, _Start, End, _Organisation, Designation, Details, PlaceOfWork, FunctionalArea, ExtraAcadmicInfoType_id, References, Summary, logindetails["userid"], ip);
          if(result['result']==-2):
            messages.error(HttpRequest,"You do not have the required privelege to this particular page.Either you do not have authenticated yourself or You have not completed your previous details ");
          elif(result['result']==1):
              messages.error(HttpRequest,"Congrats Your details have been saved");
              if(result['result']==2):
                dt=datetime.datetime.strptime(_Start,'%d %b %Y')
                dat=datetime.date(dt.year,dt.month,dt.day)
                _id=ExtraAcademicInfoDetails.objects.get(User=logindetails["userid"],Start=dat,Organisation=_Organisation).id
                updateres=ExtraAcademicInfoObj.UpdateExtraAcademicInfoDetails(_id,logindetails["userid"], Title, _Start, End, _Organisation, Designation, Details, PlaceOfWork, FunctionalArea, ExtraAcadmicInfoType_id, References, Summary, logindetails["userid"], ip);
                if(updateres['result']==1):
                    messages.error(HttpRequest,"We found a previous entry similar to Entered by You.");
                    messages.error(HttpRequest,"As Our System does not allow duplicate value.");
                    messages.error(HttpRequest,"We have updated your Entry with your current entered values");
                else:
                  messages.error(HttpRequest,"result is %s"%updateres);
                  return HttpResponseRedirect('/message/')
            
          
        
        
        #messages.error(HttpRequest,"result is %s"%result);
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
def ExtraAcademicInfoDetailsUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Id");
            flag=-1;
        if "User_id" in HttpRequest.POST:
            User_id=HttpRequest.POST["User_id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for User_id");
            flag=-1;
        if "Title" in HttpRequest.POST:
            Title=HttpRequest.POST["Title"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Title");
            flag=-1;
        if "Start" in HttpRequest.POST:
            Start=HttpRequest.POST["Start"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Start");
            flag=-1;
        if "End" in HttpRequest.POST:
            End=HttpRequest.POST["End"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for End");
            flag=-1;
        if "Organisation" in HttpRequest.POST:
            Organisation=HttpRequest.POST["Organisation"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Organisation");
            flag=-1;    
        if "Designation" in HttpRequest.POST:
            Designation=HttpRequest.POST["Designation"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Designation");
            flag=-1;
        if "Details" in HttpRequest.POST:
            Details=HttpRequest.POST["Details"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Details");
            flag=-1;
        if "PlaceOfWork_id" in HttpRequest.POST:
            PlaceOfWork_id=HttpRequest.POST["PlaceOfWork_id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for PlaceOfWork_id");
            flag=-1;
        if "FunctionalArea" in HttpRequest.POST:
            FunctionalArea=HttpRequest.POST["FunctionalArea"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for FunctionalArea");
            flag=-1;        
        if "ExtraAcadmicInfoType_id" in HttpRequest.POST:
            ExtraAcadmicInfoType_id=HttpRequest.POST["ExtraAcadmicInfoType_id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for ExtraAcadmicInfoType_id");
            flag=-1;
        if "References" in HttpRequest.POST:
            References=HttpRequest.POST["References"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for References");
            flag=-1;
        if "Summary" in HttpRequest.POST:
            Summary=HttpRequest.POST["Summary"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Summary");
            flag=-1;    
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=ExtraAcademicInfoObj.UpdateExtraAcademicInfoDetails(Id, User_id, Title, Start, End, Organisation, Designation, Details, PlaceOfWork_id, FunctionalArea, ExtraAcadmicInfoType_id, References, Summary, logindetails["userid"], ip);
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


def FunctionalAreaListIndex(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    
    return render_to_response("UserProfile/FunctionalAreaList.html",context_instance=RequestContext(HttpRequest))
def FunctionalAreaListInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "FunctionalAreaType_id" in HttpRequest.POST:
            FunctionalAreaType_id=HttpRequest.POST["FunctionalAreaType_id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for FunctionalAreaType_id");
            flag=-1;
        if "FunctionalArea" in HttpRequest.POST:
            FunctionalArea=HttpRequest.POST["FunctionalArea"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for FunctionalArea");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=ExtraAcademicInfoObj.InsertFunctionalAreaList(FunctionalAreaType_id, FunctionalArea, logindetails["userid"], ip);
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
def FunctionalAreaListUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        ExtraAcademicInfoObj=ExtraAcademicInfo()
        flag=1
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Id");
            flag=-1;
        if "FunctionalAreaType_id" in HttpRequest.POST:
            FunctionalAreaType_id=HttpRequest.POST["FunctionalAreaType_id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for FunctionalAreaType_id");
            flag=-1;
        if "FunctionalArea" in HttpRequest.POST:
            FunctionalArea=HttpRequest.POST["FunctionalArea"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for FunctionalArea");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=ExtraAcademicInfoObj.UpdateFunctionalAreaList(Id, FunctionalAreaType_id, FunctionalArea, logindetails["userid"], ip);
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
