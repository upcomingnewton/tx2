from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
import logging
from tx2.Users.models import User
LogUser = logging.getLogger(LoggerUser)


def home(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    LoggedUser=""
    
    if( logindetails["userid"] == -1):
        Logged_in=False
    else:
        Logged_in=True
        LoggedUser=User.objects.get(id= logindetails["userid"])
        #LoggedUserName=LoggedUser.UserFirstName
        
        
    return render_to_response('index.html',{'title':'Home', 'Logged_in':Logged_in, 'LoggedUser':LoggedUser},context_instance=RequestContext(HttpRequest))