# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Security.BusinessFunctions.StateFunctions import StateFnx
from tx2.Security.models import Entity
from tx2.Users.models import User
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.Users.HelperFunctions.DefaultValues import getSystemEntity,getSystemGroup_NewUsers, getSystemUser_DaemonCreateUser
from tx2.Misc.Encryption import Encrypt
from tx2.CONFIG import LoggerUser,SESSION_MESSAGE,Login_From_Type,LogOut_From_Type
from django.contrib import messages
import logging
import datetime
import inspect


LoggerUser = logging.getLogger(LoggerUser)

#TODO if anything is there in search user session, 
# then delete it here
def SearchUserIndex(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    StateList = []
    GroupList = []
    EntityList = []
    StateFnxObj = StateFnx()
    StateList = StateFnxObj.ListAllStates()
    if StateList[0] != 1:
      messages.error(HttpRequest,"ERROR. " + str(StateList[1]))
    EntityList = Entity.objects.all()
    GroupFnxObj = GroupFnx()
    GroupList = GroupFnxObj.ListAllGroups()
    if GroupList[0] != 1:
      messages.error(HttpRequest,"ERROR. " + str(GroupList[1]))
    if 'SearchUserAppModel' in HttpRequest.session:
      del HttpRequest.session['SearchUserAppModel']
    return render_to_response('UserSystem/User/SearchUserIndex.html',{'StateList':StateList[1],'GroupList':GroupList[1],'EntityList':EntityList},context_instance=RequestContext(HttpRequest))
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
      
def SearchUser(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    query = 'SELECT * FROM "Users_user"'
    HasWhereStarted = False
    if 'Include_UserID' in HttpRequest.POST:
      q = ''
      if HasWhereStarted == True:
        q += ' ' + HttpRequest.POST['AndOr_UserID']
      else:
        query += ' WHERE '
        HasWhereStarted = True
      q += ' id = '
      q += HttpRequest.POST['Search_UserID']
      query += q
    if 'Include_Email' in HttpRequest.POST:
      q = ''
      if HasWhereStarted == True:
        q += ' ' +  HttpRequest.POST['AndOr_Email']
      else:
        query += ' WHERE '
        HasWhereStarted = True
      q += ' "UserEmail" = '
      q += "'" +  HttpRequest.POST['Search_Email'] + "'"
      query += q
    if 'Include_FirstName' in HttpRequest.POST:
      q = ''
      if HasWhereStarted == True:
        q += ' ' +  HttpRequest.POST['AndOr_FirstName']
      else:
        HasWhereStarted = True
        query += ' WHERE '
      q += ' "UserFirstName" = '
      q += "'" +  HttpRequest.POST['Search_FirstName'] + "'"
      query += q
    if 'Include_MiddleName' in HttpRequest.POST:
      q = ''
      if HasWhereStarted == True:
        q += ' ' +  HttpRequest.POST['AndOr_MiddleName']
      else:
        HasWhereStarted = True
        query += ' WHERE '
      q += ' "UserMiddleName" = '
      q += "'" +  HttpRequest.POST['Search_MiddleName'] + "'"
      query += q
    if 'Include_LastName' in HttpRequest.POST:
      q = ''
      if HasWhereStarted == True:
        q += ' ' +  HttpRequest.POST['AndOr_LastName']
      else:
        HasWhereStarted = True
        query += ' WHERE '
      q += ' "UserLastName" = '
      q += "'" +  HttpRequest.POST['Search_LastName'] + "'"
      query += q
    if 'Include_DOB' in HttpRequest.POST:
      q = ''
      if HasWhereStarted == True:
        q += ' ' +  HttpRequest.POST['AndOr_DOB']
      else:
        HasWhereStarted = True
        query += ' WHERE '
      q += ' "UserBirthDate" = '
      q += "'" +  HttpRequest.POST['Search_DOB'] + "'"
      query += q
    if 'Include_Entity' in HttpRequest.POST:
      q = ''
      if HasWhereStarted == True:
        q += ' ' +  HttpRequest.POST['AndOr_Entity']
      else:
        HasWhereStarted = True
        query += ' WHERE '
      q += ' "Entity_id" = '
      q += HttpRequest.POST['Search_Entity']
      query += q
    if 'Include_Group' in HttpRequest.POST:
      q = ''
      if HasWhereStarted == True:
        q += ' ' +  HttpRequest.POST['AndOr_Group']
      else:
        HasWhereStarted = True
        query += ' WHERE '
      q += ' "Group_id" = '
      q += HttpRequest.POST['Search_Group']
      query += q
    if 'Include_State' in HttpRequest.POST:
      q = ''
      if HasWhereStarted == True:
        q += ' ' +  HttpRequest.POST['AndOr_State']
      else:
        HasWhereStarted = True
        query += ' WHERE '
      q += ' "State_id" = '
      q += HttpRequest.POST['Search_State']
      query += q
    query += ";"
    if 'SearchUserAppModel' in HttpRequest.session:
      del HttpRequest.session['SearchUserAppModel']
    HttpRequest.session['SearchUserAppModel'] = query
    return HttpResponseRedirect('/user/list/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')

def ListUser(HttpRequest):
  ip = HttpRequest.META['REMOTE_ADDR']
  details = GetLoginDetails(HttpRequest)
  if( details['userid'] == -1):
    messages.error(HttpRequest,'Please Login to continue')
    return HttpResponseRedirect('/user/login/')
  try:
    if 'SearchUserAppModel' in HttpRequest.session:
      query = HttpRequest.session['SearchUserAppModel']
      UserList = User.objects.raw(query)
      return render_to_response('UserSystem/User/ListUserIndex.html',{'UserList':UserList},context_instance=RequestContext(HttpRequest))
    else:
      return HttpResponseRedirect('/user/search/')
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      LoggerUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
