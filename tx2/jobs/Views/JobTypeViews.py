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

def JobTypeIndex(HttpRequest):
  try:
    JobTypeFunctionsObj = JobTypeFunctions()
    JobTypeList = JobTypeFunctionsObj.getObjectsAll()
    if JobTypeList[0] != 1:
      messages.error(HttpRequest,'ERROR : ' + str(JobTypeList[1]))
      return HttpResponseRedirect('/message/')
    else:
      return render_to_response('Jobs/ListJobType.html',{'JobTypeList':JobTypeList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def JobTypeAdd(HttpRequest):
  details = GetLoginDetails(HttpRequest)
  userid = -1
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    Name = ''
    flag = False
    if 'Name' in HttpRequest.POST:
     Name = HttpRequest.POST['Name']
    else: 
      flag = True
      messages.error(HttpRequest,'ERROR. Name required.')
    if len(Name) == 0:
      flag = True
      messages.error(HttpRequest,'ERROR.Proper Name required.')
    JobTypeFunctionsObj = JobTypeFunctions()
    result = JobTypeFunctionsObj.Add(Name,int(details['userid']),HttpRequest.META['REMOTE_ADDR'])
    if result[0] == 1:
      #HttpRequest.session['CompanyID'] = result[1]
      messages.error(HttpRequest,'Jobtype Updated sucessfully in our database.')
      return HttpResponseRedirect('/jobs/jobtype/')
    else:
      messages.error(HttpRequest,'ERROR.' + str(result[1]))
      return HttpResponseRedirect('/jobs/jobtype/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      

