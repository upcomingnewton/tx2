from tx2.conf.LocalProjectConfig import *
from tx2.Users.models import *
from tx2.Security.models import *
from tx2.Misc.CacheManagement import setCache,getCache
from tx2.CONFIG import LoggerUser
import logging

UserLogger = logging.getLogger(LoggerUser)

def getSystemEntity():
	s_entity = -1
	try:
		s_entity = getCache(CACHE_KEY_SYSTEM_ENTITY)
		if s_entity is None or s_entity == -1:
			e_obj = Entity.objects.get(EntityName=SYSTEM_ENTITY)
			setCache(CACHE_KEY_SYSTEM_ENTITY,e_obj.id)
			s_entity = e_obj.id
		return s_entity
	except:
		return s_entity
		
def getSystemGroup_NewUsers():
	s_entity = -1
	try:
		s_entity = getCache(CACHE_KEY_NEW_USERS_GROUP)
		if s_entity is None or s_entity == -1:
			e_obj = Group.objects.get(GroupName=SYSTEM_DAEMON_CREATE_USER_GROUP)
			setCache(CACHE_KEY_NEW_USERS_GROUP,e_obj.id)
			s_entity = e_obj.id
		return s_entity
	except:
		return s_entity
		
def getSystemGroup_EmailAU():
	s_entity = -1
	try:
		s_entity = getCache(CACHE_KEY_SYSTEM_DAEMON_USERAU_USER_GROUP)
		if s_entity is None or s_entity == -1:
			e_obj = Group.objects.get(GroupName=SYSTEM_DAEMON_USERAU_USER_GROUP)
			setCache(CACHE_KEY_SYSTEM_DAEMON_USERAU_USER_GROUP,e_obj.id)
			s_entity = e_obj.id
		return s_entity
	except:
		return s_entity
		
def getSystemUser_DaemonCreateUser():
	s_entity = -1
	print 'DaemonCreateUser %d' % (s_entity)
	print  CACHE_KEY_SYSTEM_DAEMON_CREATE_USER , SYSTEM_DAEMON_CREATE_USER
	try:
		s_entity = getCache(CACHE_KEY_SYSTEM_DAEMON_CREATE_USER)
		if s_entity is None or s_entity == -1:
			e_obj = User.objects.get(UserEmail=SYSTEM_DAEMON_CREATE_USER)
			print 'DaemonCreateUser %d' % (e_obj.id)
			setCache(CACHE_KEY_SYSTEM_DAEMON_CREATE_USER,e_obj.id)
			s_entity = e_obj.id
		print 'DaemonCreateUser %d' % (s_entity)
		return s_entity
	except:
		UserLogger.exception(' Exception occured in getSystemUser_DaemonCreateUser')
		return s_entity
