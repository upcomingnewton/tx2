from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerSecurity
from tx2.Security.BusinessFunctions.ContentTypes import ContentTypeFnx
from tx2.Security.BusinessFunctions.StateFunctions import StateFnx
from tx2.Security.BusinessFunctions.PermissionFunctions import PermissionFnx
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
import logging
Logger_User = logging.getLogger(LoggerSecurity)
import inspect
from django.contrib import messages

        
def index():
	print 'hi'

def ListAllContentTypes(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        print 'in try'
        ContentTypeObj  = ContentTypeFnx()
        ContentTypeList = ContentTypeObj.getDjangoContentTypes()
        if(ContentTypeList[0] == 1):
            print ContentTypeList
            ContentTypeList  = ContentTypeList[1]
            if( len (ContentTypeList) == 0):
                msglist.append('There are no content types in the system yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            print 'here'
            return render_to_response("SecuritySystem/ContentType.html",{'ContentTypeList':ContentTypeList,'ListContentTypes':'true',},context_instance=RequestContext(HttpRequest))
        else:
            print 'in else'
            msglist.append('Error Occured while fetching your request')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            HttpResponseRedirect('/message/')
    except:
        Logger_User.exception('[%s][%s] == EXCEPTION =='%('ListAllContentTypes',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')

def GroupSecurity(HttpRequest,ctid):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print ctid
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        ContentTypeObj  = ContentTypeFnx()
        ContentSecurityList = ContentTypeObj.getGroupSecuritybyContentTypes(ctid)
        if(ContentSecurityList[0] == 1):
            ContentSecurityList  = ContentSecurityList[1]
            if( len (ContentSecurityList) == 0):
                msglist.append('There are no content types in the system yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("SecuritySystem/GroupContentSecurity.html",{'ContentSecurityList':ContentSecurityList,'GroupSecurityList':'true'},context_instance=RequestContext(HttpRequest))
        else:
            msglist.append('Error Occured while fetching your request')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            HttpResponseRedirect('/message/')
    except:
        Logger_User.exception('[%s][%s] == EXCEPTION =='%('GroupSecurity',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')


def GroupSecurityCreateIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        ContentTypeObj  = ContentTypeFnx()
        StatesObj = StateFnx()
        PermissionObj = PermissionFnx()
        GroupObj = GroupFnx()
        ContentSecurityList = ContentTypeObj.getDjangoContentTypes()
        StatesList = StatesObj.ListAllStates()
        PermissionsList = PermissionObj.ListAllPermissions()
        GroupsList = GroupObj.ListAllGroups()
        if(ContentSecurityList[0] == 1 and StatesList[0] == 1 and PermissionsList[0] == 1 and GroupsList[0] == 1):
            ContentSecurityList  = ContentSecurityList[1]
            StatesList = StatesList[1]
            PermissionsList = PermissionsList[1]
            GroupsList = GroupsList[1]
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("SecuritySystem/GroupContentSecurity.html",{'ContentSecurityList':ContentSecurityList,'StatesList':StatesList,'PermissionsList':PermissionsList,'GroupList':GroupsList,'GroupSecurityInsert':'true','GroupSecurityList':'false'},context_instance=RequestContext(HttpRequest))
        else:
            msglist.append('Error Occured while fetching your request')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            HttpResponseRedirect('/message/')
    except:
        Logger_User.exception('[%s][%s] == EXCEPTION =='%('GroupSecurityCreate',ip))
        msglist.append('Error Occured while fetching your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        HttpResponseRedirect('/message/')
        
        
        
def GroupSecurityCreate(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
    	PermissionId = -1
    	StateId = -1
    	ContentTypeId = -1
    	GroupId = -1
    	flag = 1
    	if "GroupSecurity_permission" in HttpRequest.POST:
    		PermissionId = int(HttpRequest.POST["GroupSecurity_permission"])
    	else:
    		messages.error(HttpRequest,"Error fetching data from form for permission")
    		flag = -1
    	if "GroupSecurity_state" in HttpRequest.POST:
    		StateId = int( HttpRequest.POST["GroupSecurity_state"])
    	else:
    		messages.error(HttpRequest,"Error fetching data from form for state")
    		flag = -1
    	if "GroupSecurity_contenttype" in HttpRequest.POST:
    		ContentTypeId = int(HttpRequest.POST["GroupSecurity_contenttype"])
    	else:
    		messages.error(HttpRequest,"Error fetching data from form for contenttype")
    		flag = -1
    	if "GroupSecurity_group" in HttpRequest.POST:
    		GroupId = int ( HttpRequest.POST["GroupSecurity_group"] )
    	else:
    		messages.error(HttpRequest,"Error fetching data from form for group")
    		flag = -1
    	if flag == -1:
    		return HttpResponseRedirect('/message/')
    	else:
    		if ( PermissionId == -1) or  (StateId == -1) or  (ContentTypeId == -1)  or  (GroupId == -1 ):
    			messages.error(HttpRequest,'Invalid Values. Please select proper values')
    			return HttpResponseRedirect('/message/')
    		else:
    			ContentTypeObj = ContentTypeFnx()
    			_str = 'GroupId %d , StateId %d, PermissionId %d, ContentTypeId %d' % (GroupId,StateId,PermissionId,ContentTypeId)
    			messages.error(HttpRequest,_str)
    			res = ContentTypeObj.CreateGroupContentSecurity(GroupId,StateId,PermissionId,ContentTypeId, int(logindetails["userid"]),ip)
    			messages.error(HttpRequest,str(res))
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
