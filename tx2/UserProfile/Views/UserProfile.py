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
from tx2.UserProfile.BusinessFunctions.UserProfile import UserProfile
from tx2.Misc.MIscFunctions1 import is_integer
import logging
Logger_User = logging.getLogger(LoggerSecurity)


def BranchIndex(HttpRequest):
    return render_to_response("UserProfile/Branch.html",context_instance=RequestContext(HttpRequest))
def BranchInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "BranchName" in HttpRequest.POST:
            BranchName=HttpRequest.POST["BranchName"]
        else:
            msglist.append("Error fetching data from form for BranchName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=UserProfileObj.InsertBranch(BranchName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y

def CategoryIndex(HttpRequest):
    return render_to_response("UserProfile/Category.html",context_instance=RequestContext(HttpRequest))
def CategoryInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "CategoryName" in HttpRequest.POST:
            CategoryName=HttpRequest.POST["CategoryName"]
        else:
            msglist.append("Error fetching data from form for CategoryName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=UserProfileObj.InsertCategory(CategoryName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y

def StudentDetailsIndex(HttpRequest):
    return render_to_response("UserProfile/StudentDetails.html",context_instance=RequestContext(HttpRequest))
def StudentDetailsInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "UserId" in HttpRequest.POST:
            UserId=HttpRequest.POST["UserId"]
            if is_integer(UserId):
                UserId=int(UserId)
            else:
                msglist.append("Error integer conversion from form for UserID");
                flag=-1
        else:
            msglist.append("Error fetching data from form for RollNo");
            flag=-1;
      
        if "RollNo" in HttpRequest.POST:
            RollNo=HttpRequest.POST["RollNo"]
        else:
            msglist.append("Error fetching data from form for RollNo");
            flag=-1;
        
        if "BranchMajor" in HttpRequest.POST:
            BranchMajor=HttpRequest.POST["BranchMajor"]
            if is_integer(BranchMajor):
                BranchMajor=int(BranchMajor)
            else:
                msglist.append("Error integer conversion from form for BranchMajor");
                flag=-1
        else:
            msglist.append("Error fetching data from form for BranchMajor");
            flag=-1;
        
        if "BranchMinor" in HttpRequest.POST:
            BranchMinor=HttpRequest.POST["BranchMinor"]
            if is_integer(BranchMinor):
                BranchMajor=int(BranchMinor)
            else:
                msglist.append("Error integer conversion from form for BranchMinor");
                flag=-1
        else:
            msglist.append("Error fetching data from form for BranchMinor");
            flag=-1;                    
        
        if "Degree" in HttpRequest.POST:
            Degree=HttpRequest.POST["Degree"]
            if is_integer(Degree):
                Degree=int(Degree)
            else:
                msglist.append("Error integer conversion from form for Degree");
                flag=-1
        else:
            msglist.append("Error fetching data from form for Degree");
            flag=-1;
        
        if "Category" in HttpRequest.POST:
            Category=HttpRequest.POST["Category"]
            if is_integer(Category):
                Category=int(Category)
            else:
                msglist.append("Error integer conversion from form for Category");
                flag=-1
        else:
            msglist.append("Error fetching data from form for Category");
            flag=-1;
        
        if "ComputerProficiency" in HttpRequest.POST:
            ComputerProficiency=HttpRequest.POST["ComputerProficiency"]
            
        else:
            msglist.append("Error fetching data from form for ComputerProficiency");
            flag=-1;     
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=UserProfileObj.InsertStudentDetails(UserId, RollNo, BranchMajor, BranchMinor, Degree, Category, ComputerProficiency,logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y





         
        
        
        
        
        