import logging
from tx2.conf.LocalProjectConfig import SYSTEM_INITIALISE_LOGGER
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION
from tx2.conf.LocalProjectConfig import SYSTEM_STATE,SYSTEM_STATE_ACTIVE
from tx2.Security.models import SecurityStates,SecurityPermissions,Entity,SecurityGroupContent
from tx2.Users.models import GroupType,Group,User,UserGroup
from tx2.Misc.CacheManagement import setCache,getCache
from tx2.Misc.Encryption import  Encrypt
from django.contrib.contenttypes.models import ContentType

import datetime

class AdminInitialize():
	def __init__(self):
		self.SecurityLogger = logging.getLogger(SYSTEM_INITIALISE_LOGGER)
		
	def _DefaultSecurityContentSystem(self):
		from tx2.conf.LocalProjectConfig import SYSTEM_GROUP,SYSTEM_PERMISSION_INSERT,SYSTEM_STATE_ACTIVE,SYSTEM_ENTITY,SYSTEM_GROUPTYPE
		SystemInsertPermissionObject = SecurityPermissions.objects.get(PermissionName=SYSTEM_PERMISSION_INSERT)
		SystemActiveStateObject = SecurityStates.objects.get(StateName=SYSTEM_STATE_ACTIVE)
		e_obj = Entity.objects.get(EntityName=SYSTEM_ENTITY)
		gt_obj = GroupType.objects.get(GroupTypeName=SYSTEM_GROUPTYPE);
		SystemGroupObject = Group.objects.get(GroupName=SYSTEM_GROUP,GroupType=gt_obj,GroupEntity=e_obj,State=SystemActiveStateObject)
		try:
			msg = ''
			msglist = []
			djangoctlist = ContentType.objects.all()
			for x in djangoctlist:
				if x.app_label == 'Security' or x.app_label == 'Users':
					Obj,created = SecurityGroupContent.objects.get_or_create(Group=SystemGroupObject.id,ContentType=x,Permission=SystemInsertPermissionObject,State=SystemActiveStateObject,Active=1)
					msg = 'OBJECT = %s, RESULT = %s\t%s'%(x.name,"object",created)
					self.SecurityLogger.debug('[%s] %s'%('_DefaultSecurityContentSystem',msg))
					msglist.append(msg)

			return (1,str(msglist))
		except:
			msg = "== EXCEPTION =="
			self.SecurityLogger.exception('[%s] %s'%('_DefaultSecurityContentSystem',msg))
			return (-1,'Error occured in DefaultSecurityContentSystem')
			
			
	def _DefaultUserSystem(self):
		
		StateActiveObj = SecurityStates.objects.get(StateName=SYSTEM_STATE_ACTIVE,StateDescription=SYSTEM_STATE_ACTIVE)
		enc_dec = Encrypt()
		try:
			msg = ''
			msglist = []
			# ENTITY
			from tx2.conf.LocalProjectConfig import SYSTEM_ENTITY
			EntityObj,created = Entity.objects.get_or_create(EntityName=SYSTEM_ENTITY,EntityDescription=SYSTEM_ENTITY)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("ENTITY",EntityObj.EntityName,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			
			# GROUP TYPE
			from tx2.conf.LocalProjectConfig import SYSTEM_GROUPTYPE
			GroupTypeObj,created = GroupType.objects.get_or_create(GroupTypeName=SYSTEM_GROUPTYPE,GroupTypeDescription=SYSTEM_GROUPTYPE)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("GroupType",GroupTypeObj.GroupTypeName,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			
			# GROUP
			from tx2.conf.LocalProjectConfig import SYSTEM_GROUP
			GroupObj,created = Group.objects.get_or_create(GroupName=SYSTEM_GROUP,GroupDescription=SYSTEM_GROUP,GroupType=GroupTypeObj,GroupEntity=EntityObj,State=StateActiveObj)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("Group",GroupObj.GroupName,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			
			# USER
			from tx2.conf.LocalProjectConfig import SYSTEM_INIT_USER
			UserObj,created = User.objects.get_or_create(UserEmail=SYSTEM_INIT_USER,UserPassword=enc_dec.encrypt(SYSTEM_INIT_USER),UserBirthDate=datetime.date.today(),UserFirstName='UserFirstName',UserMiddleName='UserMiddleName',UserLastName='UserLastName',UserEntity=EntityObj,State=StateActiveObj,UserGender='M')
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("User",UserObj.UserEmail,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			
			# USER GROUP
			from tx2.conf.LocalProjectConfig import SYSTEM_INIT_USER
			UserGroupObj,created = UserGroup.objects.get_or_create(State=StateActiveObj,User=UserObj,Group=GroupObj)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("UserGroup","object",created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			
			# LOGIN TYPE
    			from tx2.conf.LocalProjectConfig import SYSTEM_LOGINTYPE
			LoginTypeObj,created = LoginType.objects.get_or_create(LoginTypeName=SYSTEM_LOGINTYPE,LoginTypeDesc=SYSTEM_LOGINTYPE)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("LoginType",LoginTypeObj.LoginTypeName,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			return (1,str(msglist))
		except:
			msg = "== EXCEPTION =="
			self.SecurityLogger.exception('[%s] %s'%('_DefaultUserSystem',msg))
			return (-1,'Error occured in DefaultUserSystem')
	
	def _InsertSystemPermissions(self):
		try:
			msg = ''
			msglist = []
			for x in  SYSTEM_PERMISSION:
				obj,created = SecurityPermissions.objects.get_or_create(PermissionName=x,PermissionDescription=x)
				msg = 'OBJECT = %s, RESULT = %s\t%s'%(x,obj.PermissionName,created)
				msglist.append(msg)
				self.SecurityLogger.debug('[%s] %s'%('_InsertSystemPermissions',msg))
			return (1,str(msglist))
		except:
			msg = "== EXCEPTION =="
			self.SecurityLogger.exception('[%s] %s'%('_InsertSystemPermissions',msg))
			return (-1,'Error occured in InsertSystemPermissions')
	
	def _InsertSystemStates(self):
		try:
			msg = ''
			msglist = []
			for x in  SYSTEM_STATE:
				obj,created = SecurityStates.objects.get_or_create(StateName=x,StateDescription=x)
				msg = 'OBJECT = %s, RESULT = %s\t%s'%(x,obj.StateName,created)
				msglist.append(msg)
				self.SecurityLogger.debug('[%s] %s'%('_InsertSystemStates',msg))
			return (1,str(msglist))
		except:
			msg = "== EXCEPTION =="
			self.SecurityLogger.exception('[%s] %s'%('_InsertSystemStates',msg))
			return (-1,'Error occured in InsertSystemStates')
