'''
Created on 14-Sep-2012

@author: jivjot
'''
from tx2.Search.Classes.Search import Search
from django.contrib import messages
import inspect
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from tx2.Misc.ExcelResponse import ExcelResponse

def SearchIndex(HttpRequest):
  try:
    
    if 'Add' in HttpRequest.POST:
      return SearchAdd(HttpRequest)
    if 'Search' in HttpRequest.POST:
      return Search_Search(HttpRequest)
    if 'Excel' in HttpRequest.POST:
      return Search_Excel(HttpRequest)
    
    contr=Search()
    return render_to_response('Search/search.html',{'options':contr.getOptions()},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      #LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def SearchAdd(HttpRequest):
  try:
    contr=Search()
    ControlsInfo=HttpRequest.POST['ControlsInfo']
    Search_Options=HttpRequest.POST['Search_Options']
    ControlsInfo=ControlsInfo+Search_Options+','
    data=HttpRequest.POST
    Search_Controls=contr.getSearchControls(ControlsInfo,data)
    return render_to_response('Search/search.html',{'options':contr.getOptions(),'ControlsInfo':ControlsInfo,'Search_Controls':Search_Controls},context_instance=RequestContext(HttpRequest))
    
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      #LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
def Search_Search(HttpRequest):
  try:
    contr=Search()
    ControlsInfo=HttpRequest.POST['ControlsInfo']
    data=HttpRequest.POST
    Search_Controls=contr.getSearchControls(ControlsInfo,data)
    obj=[('UserId','Email','DOB','FirstName','MiddleName','LastName','Gender','Age','RollNo','BranchMajor','BranchMinor','Degree','Category','10th','12th','BE_AGG','BE_ReappearRemaining','AIEEE','MobileNo','PresentAdressNo','PresentStreetAdress1','PresentStreetAdress2','PresentCityName','PresentStateName','PresentPinCode')]
    StudentList=contr.getSearchResults(ControlsInfo,data)
    if(StudentList<>None):
      StudentList=obj+StudentList
    return render_to_response('Search/search.html',{'options':contr.getOptions(),'ControlsInfo':ControlsInfo,'Search_Controls':Search_Controls,'StudentList':StudentList},context_instance=RequestContext(HttpRequest))
    
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      #LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def Search_Excel(HttpRequest):
  try:
    contr=Search()
    ControlsInfo=HttpRequest.POST['ControlsInfo']
    data=HttpRequest.POST
    obj=[('UserId','Email','DOB','FirstName','MiddleName','LastName','Gender','Age','RollNo','BranchMajor','BranchMinor','Degree','Category','10th','12th','BE_AGG','BE_ReappearRemaining','AIEEE','MobileNo','PresentAdressNo','PresentStreetAdress1','PresentStreetAdress2','PresentCityName','PresentStateName','PresentPinCode')]
    StudentList=contr.getSearchResults(ControlsInfo,data)
    if(StudentList<>None):
      StudentList=obj+StudentList
    
    return ExcelResponse(StudentList)
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      #LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
