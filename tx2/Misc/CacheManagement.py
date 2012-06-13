from django.core.cache import cache


PREFIXKEY = "CM_"
def setCache(key,value,timeout=1*7*24*60*60):
	try:
		cache.set(PREFIXKEY + key,value,timeout)
	except:
		pass

def getCache(key):
	try:
		return cache.get(PREFIXKEY + key)
	except:
		pass
		

def deleteCacheKey(key):
	try:
		if getCache(key) is not None:
			cache.delete(PREFIXKEY + key)
	except:
		pass
