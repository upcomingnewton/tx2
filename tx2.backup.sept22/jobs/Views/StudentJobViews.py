from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.jobs.BussinessFunctions.CompanyInfoFunctions import CompanyInfoFunctions
from tx2.jobs.BussinessFunctions.JobFunctions import JobFunctions
from tx2.jobs.BussinessFunctions.JobTypeFunctions import JobTypeFunctions
from tx2.jobs.BussinessFunctions.BranchJobFunctions import BranchJobFunctions
from tx2.jobs.BussinessFunctions.StudentJobFunctions import StudentJobFunctions
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.UserProfile.models import Degree,Branch,Category, StudentDetails
from tx2.jobs.models import BranchJob,StudentJob
from tx2.UserProfile.models import StudentDetails
from django.core.exceptions import ObjectDoesNotExist
import inspect
import datetime
from datetime import date
import logging
from tx2.CONFIG import LoggerJob
LoggerJobs = logging.getLogger(LoggerJob)

def EditStudentJob(HttpRequest,JobBranchID,Status):
  details = GetLoginDetails(HttpRequest)
  userid = -1
  if( details['userid'] == -1):
    return HttpResponseRedirect('/user/login/')
  try:
    obj = StudentJob.objects.get(User__id = int(details['userid']), BranchJob__id = JobBranchID)
    StudentJobFunctionsObj = StudentJobFunctions()
    result = StudentJobFunctionsObj.Update(obj.id,int(details['userid']),JobBranchID,Status,int(details['userid']),HttpRequest.META['REMOTE_ADDR'])
    if result[0] == 1:
      messages.error(HttpRequest,"SUCESS. Operation was sucessful.")
    else:
      messages.error(HttpRequest,"ERROR." + str(result[1]))
    return HttpResponseRedirect('/jobs/details/list/')
  except ObjectDoesNotExist:
    StudentJobFunctionsObj = StudentJobFunctions()
    result = StudentJobFunctionsObj.Add(int(details['userid']),JobBranchID,Status,int(details['userid']),HttpRequest.META['REMOTE_ADDR'])
    if result[0] == 1:
      messages.error(HttpRequest,"SUCESS. Operation was sucessful.")
    else:
      messages.error(HttpRequest,"ERROR." + str(result[1]))
    return HttpResponseRedirect('/jobs/details/list/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
