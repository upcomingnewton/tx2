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
    return render_to_response('index.html',{'title':'Home', },context_instance=RequestContext(HttpRequest))