from tx2.CONFIG import TEMPLATE_PARAM_USER_NOT_LOGGED_IN, GROUP_MENU_PREFIX, SESSION_MESSAGE, LoggerUser
from tx2.conf.LocalProjectConfig import  SESSION_SELECTED_GROUPS
from django.core.cache import cache
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
#from ThoughtXplore.txMenu.BusinessFunctions.LoginMenuFunctions import MakeGroupMenu
import logging

LOGGERUSER = logging.getLogger(LoggerUser)





def TEMPLATE_PARAM_USER_NOT_LOGGED_IN(request):
    try:
        return {'TEMPLATE_PARAM_USER_NOT_LOGGED_IN':TEMPLATE_PARAM_USER_NOT_LOGGED_IN}
    except:
        LOGGERUSER.exception('EXCEPTION IN TEMPLATE_PARAM_USER_NOT_LOGGED_IN')

#def MenuContextProcessor(request):
#    try:
#        if "details" in request.session.keys():
#            token = request.session["details"]
#            groupid = token['groupid']
#            menulist = MakeGroupMenu(groupid)
#            return { 'menulist':menulist}
#        else:
#            return {'menulist':TEMPLATE_PARAM_USER_NOT_LOGGED_IN}
#    except:
#        LOGGERUSER.exception('EXCEPTION IN MenuContextProcessor')
        
        
def UserContextProcessor(request):
    try:
      logindetails = GetLoginDetails(request)
      #LOGGERUSER.debug("==== IT IS HERE %d" % (logindetails["userid"]))
      if( logindetails["userid"] != -1):
        return {"userid":logindetails['userid'],"groupid":logindetails['groupid'],"loginid":logindetails['loginid'],"fname":logindetails["fname"], "loggedin":True}
      else:
        return {"userid":TEMPLATE_PARAM_USER_NOT_LOGGED_IN,"groupid":TEMPLATE_PARAM_USER_NOT_LOGGED_IN,"loginid":TEMPLATE_PARAM_USER_NOT_LOGGED_IN, "fname":[], "loggedin":False }
    except:
        LOGGERUSER.exception('EXCEPTION IN UserContextProcessor')

def GroupContextProcessor(request):
    #print request.session['SESSION_SELECTED_GROUPS']
    try:
      if 'SESSION_SELECTED_GROUPS' in request.session.keys():
        SelectedGroups = str(request.session['SESSION_SELECTED_GROUPS'])
        print '==== VALUE FOUND AND ADDED TO CP ===='
      else:
        SelectedGroups = []
        print '==== VALUE **NOT** FOUND AND ADDED TO CP ===='
      return {"SelectedGroups":SelectedGroups }
    except:
        LOGGERUSER.exception('EXCEPTION IN UserContextProcessor')
    
        
#def MessageContextProcessor(request):
#    try:
#        if SESSION_MESSAGE in request.session.keys():
#            msglist = request.session[SESSION_MESSAGE]
#            del request.session[SESSION_MESSAGE]
#            return {'msglist':msglist,}
#        else:
#            return {'msglist':[],}
#    except:
#        LOGGERUSER.exception('EXCEPTION IN MessageContextProcessor')
