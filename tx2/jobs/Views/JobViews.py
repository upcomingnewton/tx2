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
