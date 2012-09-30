from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList, replaceContentUrls
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
import logging
from tx2.Users.models import User as _User
from tx2.Communication.BusinessFunctions import CommunicationFunctions
LogUser = logging.getLogger(LoggerUser)
from tx2.Communication.BusinessFunctions.CommunicationFunctions import *
from cPickle import loads
def home(HttpRequest):
    
    M=GetCommunicationFnx().getNCommunicationsbyPageIndex("NEWS", n=3)[0]
    if(M==-5):
        return render_to_response('index.html',{'HappeningsFlag':False,'title':'Home', },context_instance=RequestContext(HttpRequest))
    else:        
    
        list2=[]
        
        for i in M:
            list1=[]
            list1.append(loads(i.Title.decode("base64").decode("zip")))
            list1.append(i.Timestamp)
            list1.append(i.User)
            content=loads(i.Content.decode("base64").decode("zip"))
            content=replaceContentUrls(content)
            preview=content.split(" ")
            preview=preview[:40]
            preview.append(".....")
            preview= " ".join(preview)
            list1.append(preview)
            list1.append(content)
            list1.append(i.id)
            list2.append(list1)
        list1=zip(list2)
        return render_to_response('index.html',{'HappeningsFlag':True,'Happenings':list1,'title':'Home', },context_instance=RequestContext(HttpRequest))

def recruitersIndex(HttpRequest):
    return render_to_response('Public/recruiters.html',{'title':'Past Recruiters', },context_instance=RequestContext(HttpRequest))
