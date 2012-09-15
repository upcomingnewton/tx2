from django.http import HttpResponseRedirect, HttpResponse
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE
from django.shortcuts import render_to_response
from django.template import RequestContext
from tx2.Misc.CacheManagement import deleteCacheKey
from tx2.Misc.MIscFunctions1 import replaceContentUrls
from cPickle import loads

from tx2.Communication.BusinessFunctions.CommunicationFunctions import GetCommunicationFnx

def newsIndex(HttpRequest,token):
    res=GetCommunicationFnx().getNCommunicationsbyPageIndex("NEWS", index=int(token))
    if(res[0]==-1 ):
        return HttpResponse("OOPS PAGE REQUESTED DOESNOT EXIST")
    elif(res[0]==-5):
        return HttpResponse("OOPS!!!! Something went wrong....Please Try sometime later, while we try to fix it")
    else:
        list2=[]
        
        for i in res[0]:
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
        
        
        
    return render_to_response("Communication/User/ViewNews.html",{'pagerange':res[3],'next':res[1],'next_p':int(token)+1,'prev_p':int(token)-1,'prev':res[2],'list':list1,'title':"Happenings@UIET"},context_instance=RequestContext(HttpRequest))
    

def newsitemIndex(HttpRequest,page,item):
    try:
        item=int(item)
        res=GetCommunicationFnx().getNCommunicationsbyPageIndex("NEWS", index=int(page))
        if(res[0]==-1 ):
            return HttpResponse("OOPS PAGE REQUESTED DOESNOT EXIST")
        elif(res[0]==-5):
            return HttpResponse("OOPS!!!! Something went wrong....Please Try sometime later, while we try to fix it")
        else:
            #print res
            for i in res[0]:
                if(i.id==item):
                    M=i
            ##print loads(M.Title.decode("base64").decode("zip"))
            #print list
            list1=[]
            list1.append(str(loads(M.Title.decode("base64").decode("zip"))))
            list1.append(str(M.Timestamp))
            list1.append(str(loads(M.Content.decode("base64").decode("zip"))))
            list1=zip(list1)
            return render_to_response("Communication/User/ViewNewsitem.html",{'message':list1},context_instance=RequestContext(HttpRequest))
            
    except:
            return HttpResponse("OOPS PAGE REQUESTED DOESNOT EXIST")



def noticeIndex(HttpRequest,token):
    msglist = AppendMessageList(HttpRequest)
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        #return render_to_response("TwoColumnMaster.html",{'type':['NOTICE'],'title':"Notices"},context_instance=RequestContext(HttpRequest))
        
        return HttpResponseRedirect('/user/login/')
    else:
            res=GetCommunicationFnx().getNCommunicationsbyPageIndex("NOTICES", index=int(token))
            if(res[0]==-1 ):
                return HttpResponse("OOPS PAGE REQUESTED DOESNOT EXIST")
            elif(res[0]==-5):
                return HttpResponse("OOPS!!!! Something went wrong....Please Try sometime later, while we try to fix it")
            else:
                list2=[]
                
                for i in res[0]:
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
                
                
                
            return render_to_response("Communication/User/ViewNotices.html",{'pagerange':res[3],'next':res[1],'next_p':int(token)+1,'prev_p':int(token)-1,'prev':res[2],'list':list1,'title':"Notices"},context_instance=RequestContext(HttpRequest))
def noticeitemIndex(HttpRequest,page,item):
    try:
        msglist = AppendMessageList(HttpRequest)
        logindetails = GetLoginDetails(HttpRequest)
        if( logindetails["userid"] == -1):
            msglist.append('Please Login to continue')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            #return render_to_response("TwoColumnMaster.html",{'type':['NOTICE'],'title':"Notices"},context_instance=RequestContext(HttpRequest))
            
            return HttpResponseRedirect('/user/login/')
        else:
            item=int(item)
            res=GetCommunicationFnx().getNCommunicationsbyPageIndex("NOTICES", index=int(page))
            if(res[0]==-1 ):
                return HttpResponse("OOPS PAGE REQUESTED DOESNOT EXIST")
            elif(res[0]==-5):
                return HttpResponse("OOPS!!!! Something went wrong....Please Try sometime later, while we try to fix it")
            else:
                #print res
                for i in res[0]:
                    if(i.id==item):
                        M=i
                ##print loads(M.Title.decode("base64").decode("zip"))
                #print list
                list1=[]
                list1.append(str(loads(M.Title.decode("base64").decode("zip"))))
                list1.append(str(M.Timestamp))
                list1.append(str(loads(M.Content.decode("base64").decode("zip"))))
                list1=zip(list1)
                return render_to_response("Communication/User/ViewNewsitem.html",{'message':list1},context_instance=RequestContext(HttpRequest))
    except:
            return HttpResponse("OOPS PAGE REQUESTED DOESNOT EXIST")

        
     
    