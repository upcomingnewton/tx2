from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from tx2.Security.models import SecurityStates,Entity,SecurityPermissions
from tx2.conf.LocalProjectConfig import CACHE_CONTENTTYPES_LIST , CACHE_STATES_LIST , CACHE_PERMISSIONS_LIST
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_UPDATE,SYSTEM_STATE_DELETED

PREFIXKEY = "CM_"
def setCache(key,value,timeout=1*7*24*60*60):
	try:
		cache.set(PREFIXKEY + key,value,timeout)
		return 1
	except:
		return -1

def getCache(key):
	try:
		return cache.get(PREFIXKEY + key)
	except:
		return -1

def deleteCacheKey(key):
	try:
		if getCache(key) is not None:
			cache.delete(PREFIXKEY + key)
		return 1
	except:
		return -1
		
def getContentTypes():
	ctlist = getCache(CACHE_CONTENTTYPES_LIST)
	if ctlist is None:
		ContentTypeList = ContentType.objects.all()
		setCache(CACHE_CONTENTTYPES_LIST,ContentTypeList)
		return ContentTypeList
	else:
		return ctlist
		
def getContentTypeIdFromModelandAppLabel(AppLabel,Model):
  ctid = -1
  try:
    ctlist = getContentTypes()
    if( len(ctlist) == 0):
      return (-1,'There are no items in Content Type List.')
    for ctobj in ctlist:
      if ctobj.app_label == AppLabel and ctobj.model == Model:
        ctid = ctobj.id
        break
    if ctid == -1:
      return (-1,'Content Type Object does not exist for this App Label and Model.')
    return (1,ctid)
  except Exception, ex:
    return (-2,str(ex))

def getStates():
	state_list = getCache(CACHE_STATES_LIST)
	if state_list is None:
		StatesList = SecurityStates.objects.all()
		setCache(CACHE_STATES_LIST,StatesList)
		return StatesList
	else:
		return state_list
		
def getDeletedState():
  StatesList = getStates()
  for x in StatesList:
    #print '%s : %d' % (x.StateName,x.id)
    if x.StateName == SYSTEM_STATE_DELETED:
      return x.id
  return -1
		
def getPermissions():
	permissions_list = getCache(CACHE_PERMISSIONS_LIST)
	if permissions_list is None:
		PermissionsList = SecurityPermissions.objects.all()
		setCache(CACHE_PERMISSIONS_LIST,PermissionsList)
		return PermissionsList
	else:
		return permissions_list
		
def getContentTypesByAppNameAndModel(_AppLabel,_Model):
	ctid = -1
	ctlist = getContentTypes()
	if  ctlist is None:
		return  ctid
	for ctobj in ctlist:
		if ctobj.app_label == _AppLabel and ctobj.model == _Model:
			ctid = ctobj.id
	return ctid
	
def getStateIDbyStateName(_StateName):
	StateID = -1
	StateList = getStates()
	if  StateList is None:
		return  StateID
	for StateObj in StateList:
		if StateObj.StateName == _StateName:
			StateID = StateObj.id
	return StateID
