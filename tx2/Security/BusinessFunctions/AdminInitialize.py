import logging
from tx2.conf.LocalProjectConfig import *
from tx2.Users.models import *
from tx2.Security.models import *
from tx2.Misc.CacheManagement import setCache,getCache
from tx2.Misc.Encryption import  Encrypt
from django.contrib.contenttypes.models import ContentType

import datetime

class AdminInitialize():
	def __init__(self):
		self.SecurityLogger = logging.getLogger(SYSTEM_INITIALISE_LOGGER)
		
	def _DefaultSecurityContentSystem(self):
		SystemInsertPermissionObject = SecurityPermissions.objects.get(PermissionName=SYSTEM_PERMISSION_INSERT)
		SystemDeletePermissionObject = SecurityPermissions.objects.get(PermissionName=SYSTEM_PERMISSION_DELETE)
		SystemUpdatePermissionObject = SecurityPermissions.objects.get(PermissionName=SYSTEM_PERMISSION_UPDATE)
		SystemActiveStateObject = SecurityStates.objects.get(StateName=SYSTEM_STATE_ACTIVE)
		SystemDeleteStateObject = SecurityStates.objects.get(StateName=SYSTEM_STATE_DELETED)
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
					
					Obj,created = SecurityGroupContent.objects.get_or_create(Group=SystemGroupObject.id,ContentType=x,Permission=SystemUpdatePermissionObject,State=SystemActiveStateObject,Active=1)
					msg = 'OBJECT = %s, RESULT = %s\t%s'%(x.name,"object",created)
					self.SecurityLogger.debug('[%s] %s'%('_DefaultSecurityContentSystem',msg))
					msglist.append(msg)
					
					Obj,created = SecurityGroupContent.objects.get_or_create(Group=SystemGroupObject.id,ContentType=x,Permission=SystemDeletePermissionObject,State=SystemDeleteStateObject,Active=1)
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
			EntityObj,created = Entity.objects.get_or_create(EntityName=SYSTEM_ENTITY,EntityDescription=SYSTEM_ENTITY)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("ENTITY",EntityObj.EntityName,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			
			# GROUP TYPE 
			GroupTypeObj,created = GroupType.objects.get_or_create(GroupTypeName=SYSTEM_GROUPTYPE,GroupTypeDescription=SYSTEM_GROUPTYPE)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("GroupType",GroupTypeObj.GroupTypeName,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			
			GroupTypeObj,created = GroupType.objects.get_or_create(GroupTypeName=SYSTEM_USERDEFINED_GROUPTYPE,GroupTypeDescription=SYSTEM_USERDEFINED_GROUPTYPE)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("GroupType",GroupTypeObj.GroupTypeName,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			
			# GROUP
			GroupObj,created = Group.objects.get_or_create(GroupName=SYSTEM_GROUP,GroupDescription=SYSTEM_GROUP,GroupType=GroupTypeObj,GroupEntity=EntityObj,State=StateActiveObj)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("Group",GroupObj.GroupName,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)
			
			# USER

			UserObj,created = User.objects.get_or_create(UserEmail=SYSTEM_INIT_USER,UserPassword=enc_dec.encrypt(SYSTEM_INIT_USER),UserBirthDate=datetime.date.today(),UserFirstName='UserFirstName',UserMiddleName='UserMiddleName',UserLastName='UserLastName',UserEntity=EntityObj,State=StateActiveObj,UserGender='S',Group=GroupObj)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("User",UserObj.UserEmail,created)
			self.SecurityLogger.debug('[%s] %s'%('_DefaultUserSystem',msg))
			msglist.append(msg)

			
			# LOGIN TYPE

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
	
	def _RegisterUserFromSiteSystem(self):
		try:
			msg = ''
			msglist = []
			enc_dec = Encrypt()
			StateActiveObj = SecurityStates.objects.get(StateName=SYSTEM_STATE_ACTIVE,StateDescription=SYSTEM_STATE_ACTIVE)
			SystemInsertPermissionObject = SecurityPermissions.objects.get(PermissionName=SYSTEM_PERMISSION_INSERT)
			SYSTEM_STATE_USER_REGISTER_Object = SecurityStates.objects.get(StateName=SYSTEM_STATE_USER_REGISTER,StateDescription=SYSTEM_STATE_USER_REGISTER)
			SYSTEM_PERMISSION_EMAIL_AUObject = SecurityPermissions.objects.get(PermissionName=SYSTEM_PERMISSION_EMAIL_AU)
			SYSTEM_STATE_USER_EMAIL_AUObject = SecurityStates.objects.get(StateName=SYSTEM_STATE_USER_EMAIL_AU,StateDescription=SYSTEM_STATE_USER_EMAIL_AU)
			# GROUP
			
			GroupTypeObj,created = GroupType.objects.get_or_create(GroupTypeName=SYSTEM_GROUPTYPE,GroupTypeDescription=SYSTEM_GROUPTYPE)
			
			EntityObj,created = Entity.objects.get_or_create(EntityName=SYSTEM_ENTITY,EntityDescription=SYSTEM_ENTITY)
			
			Group_CREATEUSERDAEMON_Obj,created = Group.objects.get_or_create(GroupName=SYSTEM_CREATEUSERDAEMON_GROUP,GroupDescription=SYSTEM_CREATEUSERDAEMON_GROUP,GroupType=GroupTypeObj,GroupEntity=EntityObj,State=StateActiveObj)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("Group",Group_CREATEUSERDAEMON_Obj.GroupName,created)
			self.SecurityLogger.debug('[%s] %s'%('_RegisterUserFromSiteSystem',msg))
			msglist.append(msg)
			
			Group_SYSTEM_DAEMON_CREATE_USER_GROUP_Obj,created = Group.objects.get_or_create(GroupName=SYSTEM_DAEMON_CREATE_USER_GROUP,GroupDescription=SYSTEM_DAEMON_CREATE_USER_GROUP,GroupType=GroupTypeObj,GroupEntity=EntityObj,State=StateActiveObj)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("Group",Group_SYSTEM_DAEMON_CREATE_USER_GROUP_Obj.GroupName,created)
			self.SecurityLogger.debug('[%s] %s'%('_RegisterUserFromSiteSystem',msg))
			msglist.append(msg)
			
			Group_SYSTEM_DAEMON_USERAU_USER_GROUP_Obj,created = Group.objects.get_or_create(GroupName=SYSTEM_DAEMON_USERAU_USER_GROUP,GroupDescription=SYSTEM_DAEMON_USERAU_USER_GROUP,GroupType=GroupTypeObj,GroupEntity=EntityObj,State=StateActiveObj)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%("Group",Group_SYSTEM_DAEMON_USERAU_USER_GROUP_Obj.GroupName,created)
			self.SecurityLogger.debug('[%s] %s'%('_RegisterUserFromSiteSystem',msg))
			msglist.append(msg)
			
			
			#get content type of Users_user
			ctlist = ContentType.objects.all()
			ctype = ContentType()
			for x in ctlist:
				if x.app_label == 'Users' and x.model == 'user':
					ctype = x
					
			Obj,created = SecurityGroupContent.objects.get_or_create(Group=Group_CREATEUSERDAEMON_Obj.id,ContentType=ctype,Permission=SystemInsertPermissionObject,State=SYSTEM_STATE_USER_REGISTER_Object,Active=1)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%(ctype.name,"object",created)
			self.SecurityLogger.debug('[%s] %s'%('_RegisterUserFromSiteSystem',msg))
			msglist.append(msg)
			
			
			Obj,created = SecurityGroupContent.objects.get_or_create(Group=Group_SYSTEM_DAEMON_CREATE_USER_GROUP_Obj.id,ContentType=ctype,Permission=SYSTEM_PERMISSION_EMAIL_AUObject,State=SYSTEM_STATE_USER_EMAIL_AUObject,Active=1)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%(ctype.name,"object",created)
			self.SecurityLogger.debug('[%s] %s'%('_RegisterUserFromSiteSystem',msg))
			msglist.append(msg)
			
			Obj,created = User.objects.get_or_create(UserEmail=SYSTEM_DAEMON_CREATE_USER,UserPassword=enc_dec.encrypt(SYSTEM_DAEMON_CREATE_USER),UserBirthDate=datetime.date.today(),UserFirstName='UserFirstName',UserMiddleName='UserMiddleName',UserLastName='UserLastName',UserEntity=EntityObj,State=StateActiveObj,UserGender='S',Group=Group_CREATEUSERDAEMON_Obj)
			msg = 'OBJECT = %s, RESULT = %s\t%s'%(Obj.UserEmail,"object",created)
			self.SecurityLogger.debug('[%s] %s'%('_RegisterUserFromSiteSystem',msg))
			msglist.append(msg)
			
			return (1,str(msglist))
		except:
			msg = "== EXCEPTION =="
			self.SecurityLogger.exception('[%s] %s'%('_RegisterUserFromSiteSystem',msg))
			return (-1,'Error occured in RegisterUserFromSiteSystem')
