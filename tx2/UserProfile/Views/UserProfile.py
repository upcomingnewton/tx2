'''
Created on 26-Jul-2012

@author: jivjot
'''
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.BusinessFunctions.UserProfile import UserProfile
from tx2.UserProfile.models import Degree,Branch,Category, StudentDetails
from tx2.Misc.MIscFunctions1 import is_integer
import logging
import inspect
from django.contrib import messages
LogUser = logging.getLogger(LOGGER_USER_PROFILE)


#def UserHome(HttpRequest):
    

def BranchIndex(HttpRequest):
    return render_to_response("UserProfile/Branch.html",context_instance=RequestContext(HttpRequest))
def BranchInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "BranchName" in HttpRequest.POST:
            BranchName=HttpRequest.POST["BranchName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for BranchName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=UserProfileObj.InsertBranch(BranchName, logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
    
def BranchUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Id");
            flag=-1;
        if "BranchName" in HttpRequest.POST:
            BranchName=HttpRequest.POST["BranchName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for BranchName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=UserProfileObj.UpdateBranch(Id, BranchName,logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
def CategoryIndex(HttpRequest):
    return render_to_response("UserProfile/Category.html",context_instance=RequestContext(HttpRequest))
def CategoryInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "CategoryName" in HttpRequest.POST:
            CategoryName=HttpRequest.POST["CategoryName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for CategoryName");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=UserProfileObj.InsertCategory(CategoryName, logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
def CategoryUpdate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "CategoryName" in HttpRequest.POST:
            CategoryName=HttpRequest.POST["CategoryName"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for CategoryName");
            flag=-1;
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for Id");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        result=UserProfileObj.UpdateCategory(Id, CategoryName,logindetails["userid"], ip)
        messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')


############## COMMON VIEW FOR BOTH INSERT AND UPDATE ############################

def StudentDetailsIndex(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
            messages.error(HttpRequest,'Please Login to continue')
            return HttpResponseRedirect('/user/login/')
    try:
      StudentDetailsObj = StudentDetails.objects.get(User=int(logindetails["userid"]))
      # exists
      StudDetailStatus= True
      return render_to_response("UserProfile/StudentDetails.html",{'StudDetailStatus':StudDetailStatus,'BranchList':Branch.objects.all(),'CategoryList':Category.objects.all(),'DegreeList':Degree.objects.all(),'StudentDetailsObj':StudentDetailsObj},context_instance=RequestContext(HttpRequest))
    except ObjectDoesNotExist:
      # does not exists
      StudDetailStatus= False
      StudentDetailsObj = False
      return render_to_response("UserProfile/StudentDetails.html",{'StudDetailStatus':StudDetailStatus,'BranchList':Branch.objects.all(),'CategoryList':Category.objects.all(),'DegreeList':Degree.objects.all(),'StudentDetailsObj':StudentDetailsObj},context_instance=RequestContext(HttpRequest))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
  
############## COMMON VIEW FOR BOTH INSERT AND UPDATE ############################
  
def StudentDetailsInsert(HttpRequest):
        ip = HttpRequest.META['REMOTE_ADDR']
        logindetails = GetLoginDetails(HttpRequest)
        if( logindetails["userid"] == -1):
            messages.error(HttpRequest,'Please Login to continue')
            return HttpResponseRedirect('/user/login/')
        try:
            
            flag=1
            UserId=int(logindetails["userid"])
            RollNo = -1
            BranchMajor = -1
            BranchMinor = -1
            Degree = -1
            Category = -1
            ComputerProficiency = ""
            aieee='null'
            if "RollNo" in HttpRequest.POST:
                RollNo=HttpRequest.POST["RollNo"]
                if len(RollNo) == 0:
                      messages.error(HttpRequest,"RollNo is required");
                      flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for RollNo");
                flag=-1;
            
            if "AIEEERank" in HttpRequest.POST:
                aieee= (HttpRequest.POST["AIEEERank"])
                if is_integer(aieee):
                  aieee=int(aieee)
                else:
                  messages.error(HttpRequest,"Error AIEEE Rank should be number only");
                  flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for aieee");
                flag=-1;
                
            if "BranchMajor" in HttpRequest.POST:
                BranchMajor= int(HttpRequest.POST["BranchMajor"])
                if BranchMajor == -1:
                    messages.error(HttpRequest,"Please select value for BranchMajor");
                    flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for BranchMajor");
                flag=-1;
            
            if "BranchMinor" in HttpRequest.POST:
                BranchMinor= int(HttpRequest.POST["BranchMinor"])
            else:
                messages.error(HttpRequest,"Error fetching data from form for BranchMinor");
                flag=-1;                    
            
            if "Degree" in HttpRequest.POST:
                Degree=int(HttpRequest.POST["Degree"])
                if Degree == -1:
                    messages.error(HttpRequest,"Please select value for Degree");
                    flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for Degree");
                flag=-1;
            
            if "Category" in HttpRequest.POST:
                Category=int(HttpRequest.POST["Category"])
                if Category == -1:
                    messages.error(HttpRequest,"Please select value for Category");
                    flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for Category");
                flag=-1;
            
            if "ComputerProficiency" in HttpRequest.POST:
                ComputerProficiency=HttpRequest.POST["ComputerProficiency"]
            else:
                ComputerProficiency = "Not applicable"  
            if flag==-1:
                return HttpResponseRedirect('/message/')
            else:
                UserProfileObj=UserProfile()
                BranchObj = Branch.objects.get(id=BranchMajor)
                Group = "GROUP_"  + BranchObj.BranchName  + "_UN-AUTHENTICATED"
                result = UserProfileObj.InsertStudentDetails(UserId, RollNo, BranchMajor, BranchMinor, Degree, Category, ComputerProficiency,aieee,UserId, ip, Group)
                messages.error(HttpRequest,result[1])
                return HttpResponseRedirect('/message/')
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          messages.error(HttpRequest,'ERROR: ' + str(ex))
          return HttpResponseRedirect('/message/')

#def StudentDetailsUpdateIndex(HttpRequest):
#    print "here"
#    msglist = AppendMessageList(HttpRequest)
#    logindetails = GetLoginDetails(HttpRequest)
#    if( logindetails["userid"] == -1):
#            messages.error(HttpRequest,'Please Login to continue')
#            HttpRequest.session[SESSION_MESSAGE] = msglist
#            return HttpResponseRedirect('/user/login/')
#            
#   # if( StudentDetails.objects.filter(User=logindetails["userid"]).exists()):
#    #    StudDetailStatus= False
#   # else:
#    StudDetailStatus= True
#    return render_to_response("UserProfile/StudentDetailsUpdate.html",{'StudDetailStatus':StudDetailStatus,'BranchList':Branch.objects.all(),'CategoryList':Category.objects.all(),'DegreeList':Degree.objects.all()},context_instance=RequestContext(HttpRequest))
#    except Exception, ex:
#      frame = inspect.currentframe()
#      args, _, _, values = inspect.getargvalues(frame)
#      msg = ''
#      for i in args:
#        msg += "[%s : %s]" % (i,values[i])
#      LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
#      messages.error(HttpRequest,'ERROR: ' + str(ex))
#      return HttpResponseRedirect('/message/')
      
def StudentDetailsUpdate(HttpRequest):
        ip = HttpRequest.META['REMOTE_ADDR']
        logindetails = GetLoginDetails(HttpRequest)
        if( logindetails["userid"] == -1):
            messages.error(HttpRequest,'Please Login to continue')
            return HttpResponseRedirect('/user/login/')
        try:
            
            flag=1
            UserId=int(logindetails["userid"])
            RollNo = -1
            BranchMajor = -1
            BranchMinor = -1
            Degree = -1
            Category = -1
            ComputerProficiency = ""
            aieee = 'null'
            if "Id" in HttpRequest.POST:
                Id=HttpRequest.POST["Id"]
                if len(Id) == 0:
                      messages.error(HttpRequest,"Id is required");
                      flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for Id");
                flag=-1;
            if "AIEEERank" in HttpRequest.POST:
                aieee= int(HttpRequest.POST["AIEEERank"])
                if is_integer(aieee):
                  aieee=int(aieee)
                else:
                  messages.error(HttpRequest,"Error AIEEE Rank should be number only");
                  flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for aieee");
                flag=-1;
            
            if "RollNo" in HttpRequest.POST:
                RollNo=HttpRequest.POST["RollNo"]
                if len(RollNo) == 0:
                      messages.error(HttpRequest,"RollNo is required");
                      flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for RollNo");
                flag=-1;
            
            if "BranchMajor" in HttpRequest.POST:
                BranchMajor= int(HttpRequest.POST["BranchMajor"])
                if BranchMajor == -1:
                    messages.error(HttpRequest,"Please select value for BranchMajor");
                    flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for BranchMajor");
                flag=-1;
            
            if "BranchMinor" in HttpRequest.POST:
                BranchMinor= int(HttpRequest.POST["BranchMinor"])
            else:
                messages.error(HttpRequest,"Error fetching data from form for BranchMinor");
                flag=-1;                    
            
            if "Degree" in HttpRequest.POST:
                Degree=int(HttpRequest.POST["Degree"])
                if Degree == -1:
                    messages.error(HttpRequest,"Please select value for Degree");
                    flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for Degree");
                flag=-1;
            
            if "Category" in HttpRequest.POST:
                Category=int(HttpRequest.POST["Category"])
                if Category == -1:
                    messages.error(HttpRequest,"Please select value for Category");
                    flag=-1;
            else:
                messages.error(HttpRequest,"Error fetching data from form for Category");
                flag=-1;
            
            if "ComputerProficiency" in HttpRequest.POST:
                ComputerProficiency=HttpRequest.POST["ComputerProficiency"]
            else:
                ComputerProficiency = "Not applicable"  
            if flag==-1:
                return HttpResponseRedirect('/message/')
            else:
                UserProfileObj=UserProfile()
                BranchObj = Branch.objects.get(id=BranchMajor)
                Group = "GROUP_"  + BranchObj.BranchName  + "_UN-AUTHENTICATED"
                result=UserProfileObj.UpdateStudentDetails(Id,UserId, RollNo, BranchMajor, BranchMinor, Degree, Category, ComputerProficiency,aieee,UserId, ip,Group)
                messages.error(HttpRequest,result[1])
                return HttpResponseRedirect('/message/')
        except Exception, ex:
            frame = inspect.currentframe()
            args, _, _, values = inspect.getargvalues(frame)
            msg = ''
            for i in args:
              msg += "[%s : %s]" % (i,values[i])
            LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
            messages.error(HttpRequest,'ERROR: ' + str(ex))
            return HttpResponseRedirect('/message/')

