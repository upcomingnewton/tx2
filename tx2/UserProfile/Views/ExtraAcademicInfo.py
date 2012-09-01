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
import logging
import inspect
Logger_User = logging.getLogger(LOGGER_USER_PROFILE)

def ExtraAcdemicInfoTypeIndex(HttpRequest):
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
    return render_to_response("UserProfile/ExtraAcademicInfoDetails.html",context_instance=RequestContext(HttpRequest))
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
        if "User_id" in HttpRequest.POST:
            User_id=HttpRequest.POST["User_id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for ExtraAcdemicInfoTypeName");
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
        result=ExtraAcademicInfoObj.InsertExtraAcademicInfoDetails(User_id, Title, Start, End, Organisation, Designation, Details, PlaceOfWork_id, FunctionalArea, ExtraAcadmicInfoType_id, References, Summary, logindetails["userid"], ip);
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
