from tx2.CONFIG import LoggerUser ,  CACHE_LOGGED_IN_USERS_DICT
from django.core.cache import cache
from tx2.Misc.Encryption import Encrypt
from time import time
import logging
from tx2.Users.models import User

LOGGERUSER = logging.getLogger(LoggerUser)

def GetLoginDetails(request):
    encdec  = Encrypt()
    #obj=User.objects.get(UserEmail='SystemInit1@init.com')
    #return {"userid":obj.id,"groupid":obj.Group.id,"loginid": 1,"fname":obj.UserFirstName,}
    
    try:
        if "details" in request.session.keys():
            token = request.session["details"]
            UpdateLoggedInUsersDict(token['loginid'])
            return {"userid":token['userid'],"groupid":token['groupid'],"loginid": encdec.decrypt(token['loginid']),"fname":token['fname'],}
        else:
            return {"userid":-1}
    except:
        LOGGERUSER.exception('EXCEPTION IN GetLoginDetails')
        return {"userid":-1}
    
def AddLoginIdToLoggedInUsersDict(loginid):
    print loginid
    try:
        # 1. check if there is already some cached dict
        LoggedInUsers = {}
        CacheKey = CACHE_LOGGED_IN_USERS_DICT
        LoggedInUsers = cache.get(CacheKey)
        if LoggedInUsers is None:
            print 'LoggedInUsers is None- making a new one'
            LoggedInUsers = {loginid:str(time())}
            # make a new dictionary
            #LoggedInUsers[str()] = 
            cache.set(CacheKey,LoggedInUsers)
            LOGGERUSER.debug('[AddLoginIdToLoggedInUsersDict] Adding.. %s: %s'%(loginid,str(time())) )
        else:
            #get this dict
            if loginid in LoggedInUsers:
                print 'loginid in LoggedInUsers'
                LoggedInUsers[loginid] = time()
                print 'UpdateLoggedInUsersDict, THERE %s'%(loginid)
            else:
                print 'loginid in LoggedInUsers'
                LoggedInUsers[loginid] = time()
                print 'UpdateLoggedInUsersDict,NOT THERE %s'%(loginid)
            cache.set(CacheKey,LoggedInUsers)
            LOGGERUSER.debug('[AddLoginIdToLoggedInUsersDict] Updating.. %s: %s'%(loginid,str(time())) )
    except:
        LOGGERUSER.exception('EXCEPTION IN AddLoginIdToLoggedInUsersDict')
        
        
def UpdateLoggedInUsersDict(loginid):
    try:
        LoggedInUsers = {}
        CacheKey = CACHE_LOGGED_IN_USERS_DICT
        LoggedInUsers = cache.get(CacheKey)
        if LoggedInUsers is None:
            # make a new dictionary
            LoggedInUsers = {}
            LoggedInUsers[loginid] = time()
            cache.add(CacheKey,LoggedInUsers)
            LOGGERUSER.debug('[UpdateLoggedInUsersDict] Adding... %s: %s'%(loginid,str(time())) )
        else:
            #get this dict
            if loginid in LoggedInUsers:
                LoggedInUsers[loginid] = time()
                print 'UpdateLoggedInUsersDict, THERE %s'%(loginid)
            else:
                LoggedInUsers[loginid] = time()
                print 'UpdateLoggedInUsersDict,NOT THERE %s'%(loginid)
            cache.set(CacheKey,LoggedInUsers)
            LOGGERUSER.debug('[UpdateLoggedInUsersDict] Updating... %s: %s'%(loginid,str(time())) )
    except:
        LOGGERUSER.exception('EXCEPTION IN UpdateLoggedInUsersDict')
        
def ClearLoginIdFromLoggedInUsersDict(loginid):
    try:
        LoggedInUsers = {}
        CacheKey = CACHE_LOGGED_IN_USERS_DICT
        LoggedInUsers = cache.get(CacheKey)
        if LoggedInUsers is not None:
            if loginid in LoggedInUsers:
                del LoggedInUsers[loginid] 
            LOGGERUSER.debug('[ClearLoginIdFromLoggedInUsersDict]  %s'%(loginid) )
        print (str(LoggedInUsers))
        cache.set(CacheKey,LoggedInUsers)
    except:
        LOGGERUSER.exception('EXCEPTION IN ClearLoginIdFromLoggedInUsersDict')
        
def ClearAllValuesFromLoggedInUserDict():
    try:
        LoggedInUsers = {}
        CacheKey = CACHE_LOGGED_IN_USERS_DICT
        LoggedInUsers = cache.get(CacheKey)
        if LoggedInUsers is not None:
            LoggedInUsers.clear()
            LOGGERUSER.debug('[ClearAllValuesFromLoggedInUserDict] Clearing All values' )
        cache.delete(CacheKey)
    except:
        LOGGERUSER.exception('EXCEPTION IN ClearAllValuesFromLoggedInUserDict')
        
def GetLoggedInUserDict():
    try:
        LoggedInUsers = {}
        CacheKey = CACHE_LOGGED_IN_USERS_DICT
        LoggedInUsers = cache.get(CacheKey)
        if LoggedInUsers is None:
            LoggedInUsers = {}
        LOGGERUSER.debug('[GetLoggedInUserDict] returning All values' )
        return LoggedInUsers
    except:
        LOGGERUSER.exception('EXCEPTION IN GetLoggedInUserDict')


