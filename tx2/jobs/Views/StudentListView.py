'''
Created on 12-Sep-2012

@author: jivjot
'''
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
from tx2.DataBaseHelper import DBhelper
from tx2.Misc.ExcelResponse import ExcelResponse
LoggerJobs = logging.getLogger(LoggerJob)

def ExcelJobApplied(HttpRequest,JobId):
  details = GetLoginDetails(HttpRequest)
  userid = -1
  if( details['userid'] == -1):
    return HttpResponseRedirect('/user/login/')
  try:
    obj=[('UserId','Email','DOB','FirstName','MiddleName','LastName','Gender','Age','RollNo','BranchMajor','BranchMinor','Degree','Category','10th','12th','BE_AGG','BE_ReappearRemaining','AIEEE','MobileNo','PresentAdressNo','PresentStreetAdress1','PresentStreetAdress2','PresentCityName','PresentStateName','PresentPinCode')]
    sql='Select * from "View_Student" where "Id" in(select distinct "User_id" from "jobs_studentjob" where "BranchJob_id" in (select id from "jobs_branchjob" where "Job_id"='+JobId+') and "Status"=0);'
    obj=obj+DBhelper.CallSelectFunction(sql)
    return ExcelResponse(obj)
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
def ViewJobApplied(HttpRequest,JobId):
  details = GetLoginDetails(HttpRequest)
  userid = -1
  if( details['userid'] == -1):
    return HttpResponseRedirect('/user/login/')
  try:
    obj=[('UserId','Email','DOB','FirstName','MiddleName','LastName','Gender','Age','RollNo','BranchMajor','BranchMinor','Degree','Category','10th','12th','BE_AGG','BE_ReappearRemaining','AIEEE','MobileNo','PresentAdressNo','PresentStreetAdress1','PresentStreetAdress2','PresentCityName','PresentStateName','PresentPinCode')]
    sql='Select * from "View_Student" where "Id" in(select distinct "User_id" from "jobs_studentjob" where "BranchJob_id" in (select id from "jobs_branchjob" where "Job_id"='+JobId+') and "Status"=0);'
    obj=obj+DBhelper.CallSelectFunction(sql)
    download='/jobs/excel/job/'+JobId+'/applied'
    return render_to_response('Jobs/StudentList.html',{'StudentList':obj,'download':download},context_instance=RequestContext(HttpRequest))
    
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
