from django.core.cache import cache


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
