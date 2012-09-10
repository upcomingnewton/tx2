from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.jobs.BussinessFunctions.CompanyInfoFunctions import CompanyInfoFunctions
from tx2.jobs.BussinessFunctions.JobFunctions import JobFunctions
from tx2.jobs.BussinessFunctions.JobTypeFunctions import JobTypeFunctions
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.UserProfile.models import Degree,Branch,Category, StudentDetails
import inspect
import datetime
from datetime import date
import logging
from tx2.CONFIG import LoggerJob
LoggerJobs = logging.getLogger(LoggerJob)

def EditJobIndex(HttpRequest,CompanyID, JobID):
  try:
    BranchList = Branch.objects.all()
    if ( JobID == -1):
      # add company
      return render_to_response('Jobs/EditJobNotification.html',{'Edit':False,'BranchList':BranchList,'CompanyID':CompanyID},context_instance=RequestContext(HttpRequest))
    else:
      # edit company
      return render_to_response('Jobs/EditJobNotification.html',{'Edit':False,'BranchList':BranchList,'CompanyID':CompanyID},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def EditJob(HttpRequest,CompanyID, JobID):
  details = GetLoginDetails(HttpRequest)
  userid = -1
  if( details['userid'] != -1):
    userid = int(details['userid'])
  try:
    BranchList = Branch.objects.all()
    ContactPersonName = ''
    ContactPersonMobile = ''
    ContactPersonEmail = ''
    ContactPersonDetails = ''
    Profile = ''
    Designation = ''
    Package = ''
    DateOfVisit = ''
    DateOfVisitDay = ''
    DateOfVisitMonth = ''
    DateOfVisitYear = ''
    JobDetails1 = ''
    JobDetails2 = ''
    flag = False
    RecruitmentRounds = ''
    if 'ContactPersonName' in HttpRequest.POST:
      ContactPersonName = HttpRequest.POST['ContactPersonName']
    else:
      flag = True
      messages.error(HttpRequest,'ERROR. Contact Person Name is required.')
    if 'ContactPersonMobile' in HttpRequest.POST:
      ContactPersonMobile = HttpRequest.POST['ContactPersonMobile']
    if 'ContactPersonEmail' in HttpRequest.POST:
      ContactPersonEmail = HttpRequest.POST['ContactPersonEmail']
    if 'ContactPersonDetails' in HttpRequest.POST:
      ContactPersonDetails = HttpRequest.POST['ContactPersonDetails']
    if 'Profile' in HttpRequest.POST:
      Profile = HttpRequest.POST['Profile']
    if 'Designation' in HttpRequest.POST:
      Designation = HttpRequest.POST['Designation']
    if 'Package' in HttpRequest.POST:
      Package = HttpRequest.POST['Package']
    if 'DateOfVisitDay' in HttpRequest.POST:
      DateOfVisitDay = HttpRequest.POST['DateOfVisitDay']
    if 'DateOfVisitMonth' in HttpRequest.POST:
      DateOfVisitMonth = HttpRequest.POST['DateOfVisitMonth']
    if 'DateOfVisitYear' in HttpRequest.POST:
      DateOfVisitYear = HttpRequest.POST['DateOfVisitYear']
    if 'JobDetails1' in HttpRequest.POST:
      JobDetails1 = HttpRequest.POST['JobDetails1']
    if 'JobDetails2' in HttpRequest.POST:
      JobDetails2 = HttpRequest.POST['JobDetails2']
    try:
      DateOfVisit = datetime.date(int(DateOfVisitYear),int(DateOfVisitMonth),int(DateOfVisitDay))
    except ValueError as err:
      messages.error(HttpRequest,'Invalid Date of visit')
      flag = True
    if flag == True:
      print '=====error====='
      return HttpResponseRedirect('/message/')
    elif ( JobID == -1):
      #add
      print '===DDING==='
      JobFunctionsObj = JobFunctions()
      result = JobFunctionsObj.Add(CompanyID,Profile,Designation,Package,DateOfVisit,JobDetails1,JobDetails2,RecruitmentRounds,ContactPersonName,ContactPersonMobile,ContactPersonEmail,ContactPersonDetails,DateOfVisit,userid,HttpRequest.META['REMOTE_ADDR'])
    else:
      #edit
      pass
    print result
    if result[0] == 1:
      jobid = int(result[1])
      for branch in BranchList:
        beligible = 'Eligible_' + str(branch.id)
        if (beligible) in HttpRequest.POST:
          isbeligible = HttpRequest.POST[beligible]
          if isbeligible == '1':
            # this branch is eligible, add it to database
      
      messages.error(HttpRequest,"ERROR " +  str(result[1]))
      return HttpResponseRedirect('/message/')
    else:
      messages.error(HttpRequest,"ERROR  " + str(result[1]))
      return HttpResponseRedirect('/message/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
