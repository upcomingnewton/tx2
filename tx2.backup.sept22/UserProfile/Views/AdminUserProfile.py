from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.BusinessFunctions.UserProfile import UserProfile
from tx2.UserProfile.models import Degree,Branch,Category, StudentDetails
from tx2.Misc.MIscFunctions1 import is_integer
import logging
import inspect
from django.contrib import messages
LogUser = logging.getLogger(LOGGER_USER_PROFILE)

def BranchAdminAuthenticateIndex(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
      if 'BranchAdminChangeGroupSession' in HttpRequest.session.keys():
        # get the key, and show the users list
        BranchName = HttpRequest.session['BranchAdminChangeGroupSession']
        del HttpRequest.session['BranchAdminChangeGroupSession']
        PresentGroupName = "GROUP_"  + BranchName + "_UN-AUTHENTICATED"
        TargetGroupName = "GROUP_"  + BranchName
        # get the id of this group
        GroupFnxObj = GroupFnx()
        gid = GroupFnxObj.getGroupObjectByName(TargetGroupName)
        pgid = GroupFnxObj.getGroupObjectByName(PresentGroupName)
        if gid[0] == 1:
          gid = gid[1]
        if pgid[0] == 1:
          pgid = pgid[1]
          # get all students who are in this group
          StudentList = StudentDetails.objects.filter(User__Group__id=pgid.id)
          BranchList = Branch.objects.all()
          return render_to_response("UserProfile/Category.html",{'StudentList':StudentList,'BranchList':BranchList,'gid':gid.id},context_instance=RequestContext(HttpRequest))
      else:
        # ask for selection of a branch
        messages.error(HttpRequest,'ERROR. Please request branch for verifying students of that branch.')
        # get branch list and show to user
        return render_to_response()
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def BranchAdminAuthenticate_SetSession(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
      if 'SelectedBranch' in HttpRequest.POST:
        # get the key, and show the users list
        BranchName = HttpRequest.POST['SelectedBranch']
        if 'BranchAdminChangeGroupSession' in HttpRequest.session.keys():
          del HttpRequest.session['BranchAdminChangeGroupSession']
        HttpRequest.session['BranchAdminChangeGroupSession'] = BranchName
        return HttpResponseRedirect('')
      else:
        messages.error(HttpRequest,'Could not get the selected branch value. Please try again.')
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
