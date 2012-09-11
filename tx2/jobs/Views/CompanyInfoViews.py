from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.jobs.BussinessFunctions.CompanyInfoFunctions import CompanyInfoFunctions
from tx2.jobs.BussinessFunctions.JobFunctions import JobFunctions
from tx2.jobs.BussinessFunctions.JobTypeFunctions import JobTypeFunctions
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
import inspect
from datetime import date
import logging
from tx2.CONFIG import LoggerJob

LoggerJobs = logging.getLogger(LoggerJob)

def ObjectIndex(HttpRequest, CompanyID):
  try:
    if ( CompanyID == -1):
      # add company
      return render_to_response('Jobs/CompanyEdit.html',{'Edit':False,'CompanyObj':'NULL'},context_instance=RequestContext(HttpRequest))
    else:
      # edit company
      CompanyInfoFunctionsObj = CompanyInfoFunctions()
      ReqObj = CompanyInfoFunctionsObj.getObjectById(CompanyID)
      if ReqObj[0] != 1:
        messages.error(HttpRequest,'ERROR : ' + str(ReqObj[1]))
        return HttpResponseRedirect('/message/')
      else:
        return render_to_response('Jobs/CompanyEdit.html',{'Edit':True,'CompanyObj':ReqObj[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def ListIndex(HttpRequest):
  try:
      CompanyInfoFunctionsObj = CompanyInfoFunctions()
      ReqList = CompanyInfoFunctionsObj.getObjectsAll()
      if ReqList[0] != 1:
        messages.error(HttpRequest,'ERROR : ' + str(ReqObj[1]))
        return HttpResponseRedirect('/message/')
      else:
        return render_to_response('Jobs/ListCompanyInfo.html',{'CompanyList':ReqList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def EditCompany(HttpRequest,CompanyID):
  details = GetLoginDetails(HttpRequest)
  userid = -1
  if( details['userid'] != -1):
    userid = int(details['userid'])
  try:
    CompanyName = ''
    CompanyAdress = ''
    CompanyWebsite = ''
    CompanyAbout = 'Not Provided'
    CompanyOtherDetails1 = 'Not Provided'
    CompanyOtherDetails2 = 'Not Provided'
    flag = False
    if 'CompanyName' in HttpRequest.POST:
     CompanyName = HttpRequest.POST['CompanyName']
    else: 
      flag = True
      messages.error(HttpRequest,'ERROR. Company Name required.')
    if 'CompanyAdress' in HttpRequest.POST:
     CompanyAdress = HttpRequest.POST['CompanyAdress']
    else: 
      flag = True
      messages.error(HttpRequest,'ERROR. Company Adress required.')
    if 'CompanyWebsite' in HttpRequest.POST:
     CompanyWebsite = HttpRequest.POST['CompanyWebsite']
    else: 
      flag = True
      messages.error(HttpRequest,'ERROR. Company Website required.')
    if len(CompanyName) == 0:
      flag = True
      messages.error(HttpRequest,'ERROR.Proper Company Name required.')
    if len(CompanyAdress) == 0:
      flag = True
      messages.error(HttpRequest,'ERROR.Proper Company Adress required.')
    if len(CompanyWebsite) == 0:
      flag = True
      messages.error(HttpRequest,'ERROR.Proper Company Website required.')
    if 'CompanyAbout' in HttpRequest.POST:
     CompanyAbout = HttpRequest.POST['CompanyAbout']
    if 'CompanyOtherDetails1' in HttpRequest.POST:
     CompanyOtherDetails1 = HttpRequest.POST['CompanyOtherDetails1']
    if 'CompanyOtherDetails2' in HttpRequest.POST:
     CompanyOtherDetails2 = HttpRequest.POST['CompanyOtherDetails2']
    CompanyInfoFunctionsObj = CompanyInfoFunctions()
    if flag == True:
      if CompanyID == -1:
        return HttpResponseRedirect('/jobs/company/add/')
      else:
        return HttpResponseRedirect('/jobs/company/' + str(CompanyID) +'/edit/')
    if CompanyID == -1:
      result = CompanyInfoFunctionsObj.Add(CompanyName,CompanyAdress,CompanyWebsite,CompanyAbout,CompanyOtherDetails1,CompanyOtherDetails2,userid,userid,HttpRequest.META['REMOTE_ADDR'])
    else:
      result = CompanyInfoFunctionsObj.Update(CompanyID,CompanyName,CompanyAdress,CompanyWebsite,CompanyAbout,CompanyOtherDetails1,CompanyOtherDetails2,userid,userid,HttpRequest.META['REMOTE_ADDR'])
    if result[0] == 1:
      #HttpRequest.session['CompanyID'] = result[1]
      messages.error(HttpRequest,'Company Updated sucessfully in our database.')
      return HttpResponseRedirect('/jobs/company/list/')
    else:
      messages.error(HttpRequest,'ERROR.' + str(result[1]))
      return HttpResponseRedirect('/jobs/company/list/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      

