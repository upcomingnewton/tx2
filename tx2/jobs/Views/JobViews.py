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
from tx2.jobs.models import BranchJob, StudentJob
from tx2.UserProfile.models import StudentDetails
from django.core.exceptions import ObjectDoesNotExist
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
      return render_to_response('Jobs/AddJobNotification.html',{'Edit':False,'BranchList':BranchList,'CompanyID':CompanyID},context_instance=RequestContext(HttpRequest))
    else:
      # edit company
      details = GetLoginDetails(HttpRequest)
      if( details['userid'] == -1):
        return HttpResponseRedirect('/user/login/')
      JobFunctionsObj = JobFunctions()
      result = JobFunctionsObj.getObjectByID(JobID)
      if result[0] != 1:
        messages.error(HttpRequest,"ERROR " + str(result[1]))
        return HttpResponseRedirect('/message/')
      else:
        BranchJobFunctionsObj = BranchJobFunctions()
        BranchJobList = BranchJobFunctionsObj.getObjectsbyJob(JobID)
        if BranchJobList[0] != 1:
          messages.error(HttpRequest,"ERROR " + str(BranchJobList[1]))
          return HttpResponseRedirect('/message/')
        JobTypeFunctionsObj = JobTypeFunctions()
        JobTypeList = JobTypeFunctionsObj.getObjectsAll()
        if JobTypeList[0] != 1:
          messages.error(HttpRequest,"ERROR " + str(JobTypeList[1]))
          return HttpResponseRedirect('/message/')
        BranchJobListID = [ x.Branch.id for x in BranchJobList[1]]
        return render_to_response('Jobs/EditJobNotification.html',{'Edit':True,'BranchList':BranchList,'CompanyID':CompanyID,'JobObj':result[1],'BranchJobList':BranchJobList[1],'JobTypeList':JobTypeList[1],'BranchJobListID':BranchJobListID},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def ListJobsForStudents(HttpRequest):
  details = GetLoginDetails(HttpRequest)
  userid = -1
  if( details['userid'] == -1):
    return HttpResponseRedirect('/user/login/')
  try:
    JobFunctionsObj = JobFunctions()
    JobsList = JobFunctionsObj.getObjectsAll()
    if JobsList[0] != 1:
      messages.error(HttpRequest,"ERROR " + str(JobsList[1]))
      return HttpResponseRedirect('/message/')
    else:
      return render_to_response('Jobs/ListJobs.html',{'JobsList':JobsList[1]},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def ListJobsByCompany(HttpRequest,CompanyID):
  details = GetLoginDetails(HttpRequest)
  userid = -1
  if( details['userid'] == -1):
    return HttpResponseRedirect('/user/login/')
  try:
    JobFunctionsObj = JobFunctions()
    JobsList = JobFunctionsObj.getObjectByCompanyId(CompanyID)
    if JobsList[0] != 1:
      messages.error(HttpRequest,"ERROR " + str(JobsList[1]))
      return HttpResponseRedirect('/message/')
    else:
      return render_to_response('Jobs/ListJobs.html',{'JobsList':JobsList[1], 'Edit':True},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
      
def ListJobDetailsForStudents(HttpRequest,JobID):
  details = GetLoginDetails(HttpRequest)
  userid = -1
  if( details['userid'] == -1):
    return HttpResponseRedirect('/user/login/')
  try:
    JobFunctionsObj = JobFunctions()
    JobsList = JobFunctionsObj.getObjectByID(JobID)
    if JobsList[0] != 1:
      messages.error(HttpRequest,"ERROR " + str(JobsList[1]))
      return HttpResponseRedirect('/message/')
    else:
      BranchID=StudentDetails.objects.get(User__id=int(details["userid"])).BranchMajor.id
      JobBranchID = BranchJob.objects.get(Job__id = JobID,Branch__id = BranchID).id
      try:
        obj = StudentJob.objects.get(User__id = int(details['userid']), BranchJob__id = JobBranchID)
        Status = obj.Status
      except ObjectDoesNotExist:
        Status = -1
      print '====' + str(Status) + '======' 
      return render_to_response('Jobs/ListJobDetails.html',{'JobObj':JobsList[1],'JobBranchID':JobBranchID,'Status':Status},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerJobs.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def AddJob(HttpRequest,CompanyID):
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
    if 'RecruitmentRounds' in HttpRequest.POST:
      RecruitmentRounds = HttpRequest.POST['RecruitmentRounds']
    try:
      DateOfVisit = datetime.date(int(DateOfVisitYear),int(DateOfVisitMonth),int(DateOfVisitDay))
    except ValueError as err:
      messages.error(HttpRequest,'Invalid Date of visit')
      flag = True
    if flag == True:
      return HttpResponseRedirect('/jobs/company/' + str(CompanyID) + '/jobs/add/')
      #add
    JobFunctionsObj = JobFunctions()
    result = JobFunctionsObj.Add(CompanyID,Profile,Designation,Package,DateOfVisit,JobDetails1,JobDetails2,RecruitmentRounds,ContactPersonName,ContactPersonMobile,ContactPersonEmail,ContactPersonDetails,DateOfVisit,userid,HttpRequest.META['REMOTE_ADDR'])
    if result[0] == 1:
      jobid = int(result[1])
      JobTypeFunctionsObj = JobTypeFunctions()
      JobTypeRes = JobTypeFunctionsObj.getObjectbyName('Not classified')
      if JobTypeRes[0] == 1:
        JobTypeRes = JobTypeRes[1]
      else:
        messages.error(HttpRequest,"ERROR : " + str(JobTypeRes[1]))
        return HttpResponseRedirect('/jobs/company/' + str(CompanyID) + '/jobs/add/')
      for branch in BranchList:
        beligible = 'Eligible_' + str(branch.id)
        if (beligible) in HttpRequest.POST:
          isbeligible = HttpRequest.POST[beligible]
          if isbeligible == '1':
            # this branch is eligible, add it to database
            BranchJobFunctionsObj = BranchJobFunctions()
            result = BranchJobFunctionsObj.Add(branch.id,jobid,JobTypeRes.id,HttpRequest.POST['Criteria_' + str(branch.id)],'',userid,HttpRequest.META['REMOTE_ADDR'])
            print str(result) + '==' + branch.BranchName
            if result[0] != 1:
              messages.error(HttpRequest,'ERROR : ' + result[1])
              return HttpResponseRedirect('/jobs/company/' + str(CompanyID) + '/jobs/add/')
            #def Add(self,Branch,Job,JobType,Comments1,Comments2,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
      messages.error(HttpRequest,"SUCESS. Job details have been recorded sucessfully.You can add more job notifications here.")
      return HttpResponseRedirect('/jobs/company/' + str(CompanyID) + '/jobs/add/')
    else:
      messages.error(HttpRequest,"ERROR  " + str(result[1]))
      return HttpResponseRedirect('/jobs/company/' + str(CompanyID) + '/jobs/add/')
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
  if( details['userid'] == -1):
    return HttpResponseRedirect('/user/login/')
  try:
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
    if 'RegistrationsUpto' in HttpRequest.POST:
      RegistrationsUpto = HttpRequest.POST['RegistrationsUpto']
    if 'RecruitmentRounds' in HttpRequest.POST:
      RecruitmentRounds = HttpRequest.POST['RecruitmentRounds']
    try:
      DateOfVisit = datetime.date(int(DateOfVisitYear),int(DateOfVisitMonth),int(DateOfVisitDay))
    except ValueError as err:
      messages.error(HttpRequest,'Invalid Date of visit')
    try:
      RegistrationsUpto = RegistrationsUpto.split('/')
      RegistrationsUpto = datetime.datetime(int(RegistrationsUpto[0]),int(RegistrationsUpto[1]),int(RegistrationsUpto[2]),int(RegistrationsUpto[3]),int(RegistrationsUpto[4]))
    except ValueError as err:
      messages.error(HttpRequest,'Invalid Registration Time data')
      flag = True
    if flag == True:
      return HttpResponseRedirect('/message/')
    JobFunctionsObj = JobFunctions()
    result = JobFunctionsObj.Update(JobID, CompanyID,Profile,Designation,Package,DateOfVisit,JobDetails1,JobDetails2,RecruitmentRounds,ContactPersonName,ContactPersonMobile,ContactPersonEmail,ContactPersonDetails,RegistrationsUpto,int(details["userid"]),HttpRequest.META['REMOTE_ADDR'])
    if result[0] == 1:
      messages.error(HttpRequest,"SUCESS")
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
      
def BranchJobEdit(HttpRequest,CompanyID, JobID):
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    return HttpResponseRedirect('/user/login/')
  try:
    BranchList = Branch.objects.all()
    BranchJobFunctionsObj = BranchJobFunctions()
    JobTypeFunctionsObj = JobTypeFunctions()
    JobTypeRes = JobTypeFunctionsObj.getObjectbyName('Not classified')
    if JobTypeRes[0] == 1:
       JobTypeRes = JobTypeRes[1]
    for branch in BranchList:
        isinitial = 'Initial_' + str(branch.id)
        if (isinitial) in HttpRequest.POST:
          isinitial = HttpRequest.POST[isinitial]
          result = [1,-1]
          if isinitial != "-1":
            # edit
            _id = int(isinitial)
            JobTypeID = HttpRequest.POST["JobType_" + str(branch.id)]
            Comments1 = HttpRequest.POST["Criteria_" + str(branch.id)]
            Comments2 = HttpRequest.POST["Remarks_" + str(branch.id)]
            result = BranchJobFunctionsObj.Update(_id,branch.id,JobID,JobTypeID,Comments1,Comments2,int(details['userid']),HttpRequest.META['REMOTE_ADDR'])
          else:
            if HttpRequest.POST["Eligible_" + str(branch.id)] == "1":
            #add, if this branch is eligible, add it to database
              Comments1 = HttpRequest.POST["Criteria_" + str(branch.id)]
              Comments2 = HttpRequest.POST["Remarks_" + str(branch.id)]
              JobTypeID = HttpRequest.POST["JobType_" + str(branch.id)]
              result = BranchJobFunctionsObj.Add(branch.id,JobID,JobTypeID,Comments1,Comments2,int(details['userid']),HttpRequest.META['REMOTE_ADDR'])
          #print str(result) + '==' + branch.BranchName
          if result[0] != 1:
             messages.error(HttpRequest,'ERROR : ' + result[1])
             return HttpResponseRedirect('/message/')
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
