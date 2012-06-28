from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from tx2.conf.LocalProjectConfig import CACHE_CONTENTTYPES_LIST

PREFIXKEY = "CM_"
def setCache(key,value,timeout=1*7*24*60*60):
	try:
		cache.set(PREFIXKEY + key,value,timeout)
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
	
