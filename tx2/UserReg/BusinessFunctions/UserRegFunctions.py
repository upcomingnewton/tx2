from tx2.UserReg.models import RegisterUser
from tx2.UserReg.DBFunctions.DBFunctions import DBRegUserUpdate,DBRegUserInsert
from tx2.UserReg.models import RegisterUser
from tx2.Users.models import User
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypes
from tx2.CONFIG import LOGGER_UserReg
import logging
import datetime
from tx2.conf.LocalProjectConfig import *
from django.core.exceptions import ObjectDoesNotExist, DoesNotExist

class UserRegFnx():
	def __init__(self):
		self.UserRegLogger = logging.getLogger(LOGGER_UserReg)
		self.UserSep = "$"
		self.GroupSep = "!"
		
	#Internal function
	def ConvertStrListToInt(self,UsersList):
		try:
			res = [ int(i) for i in UsersList]
			return res
		except:
			return []
	
	def getUniqueIntList(self,UsersList):
		try:
			res = []
			num = len(UsersList)
			for x in range(0,num):
				if UsersList[x] not in UsersList[x+1:]:
					res.append(UsersList[x])
			return res
		except:
			return []
	
	def ConvertUsersListToString(self,UsersList,userstr):
		try:
			for user in UsersList:
				userstr = userstr + str(user) + userstr
			self.UserRegLogger.debug('[%s] == %s =='%('ConvertUsersListToString',userstr))
			return userstr
		except:
			return None
	
	#Internal function
	def ConvertStringToUsersList(self,UsersList,sep):
		try:
			_str = UsersList.split(sep)
			_str = _str[1:-1]
			res = [int(i) for i in _str]
			return res
		except:
			return None
		
	def Create(self,MetaInfo,Desc,Users,Groups,ReferenceToRegisterUser,Record,ContentType,Operation,by,ip):
		try:
			details = {
					'MetaInfo':MetaInfo,
					'Desc':Desc,
					'Users':Users,
					'Groups':Groups,
					'ReferenceToRegisterUser':ReferenceToRegisterUser,
					'Record':Record,#int
					'ContentType':ContentType,#int
					'Operation':Operation,
					'by':by,#int
					'ip':ip,
				}
			result = DBRegUserInsert(details)
			return (1,result)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('Create'))
			return (-1,'Error at business level Create function in UserReg')
			
	def Update(self,MetaInfo,Desc,Users,Groups,ReferenceToRegisterUser,Record,ContentType,Operation,by,ip,LogsDesc):
		try:
			details = {
					'MetaInfo':MetaInfo,
					'Desc':Desc,
					'Users':Users,
					'Groups':Groups,
					'ReferenceToRegisterUser':ReferenceToRegisterUser,
					'Record':Record,#int
					'ContentType':ContentType,#int
					'Operation':Operation,
					'LogsDesc':LogsDesc,
					'by':by,#int
					'ip':ip,
				}
			result = DBRegUserUpdate(details)
			return (1,result)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('Update'))
			return (-1,'Error at business level Update function in UserReg')
		

	def AdduserData(self,AppLabel,Model,rid,Desc,Users,by,ip,op_insert=SYSTEM_PERMISSION_INSERT,op_update=SYSTEM_PERMISSION_UPDATE,Groups=-1,ReferenceToRegisterUser=1-,):
		try:
			# get the object, if present
			ctid = -1
			ctlist = getContentTypes()
			for ctobj in ctlist:
				if ctobj.app_label == AppLabel and ctobj.model == Model:
					ctid = ctobj.id
			if ctid == -1:
				#error here
				error_msg = 'Invalid Applabel %s or Model %s' % (AppLabel, Model)
				self.UserRegLogger.error('[%s] == Error == \n %s'%('AdduserData',error_msg))
				return (-1,error_msg)
			print ctid
			
			try:
				#change code 4 this for Notice i'll b calling this funx with Users=-1 or Users=
			
				UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
				objlist = self.ConvertStringToUsersList(UserRegObj.Users,self.UserSep)
				user_list = self.ConvertStrListToInt(Users)
				UsersList = objlist + user_list
				UsersList = self.getUniqueIntList(UsersList)
				UsersList = self.ConvertUsersListToString(UsersList,self.UserSep)
				
				grplist = self.ConvertStringToUsersList(UserRegObj.Groups,self.GroupSep)
				grp_list = self.ConvertStrListToInt(Groups)
				GroupsList = grplist + grp_list
				GroupsList = self.getUniqueIntList(GroupsList)
				GroupsList = self.ConvertUsersListToString(GroupsList,self.GroupSep)
				
				return self.Update(str(datetime.datetime.now()),Desc,UsersList,GroupsList,"-1",rid,ctid,op_update,by,ip,'added ' + str(user_list))
			except  ObjectDoesNotExist , DoesNotExist:
				UsersList = self.ConvertUsersListToString(Users,self.UserSep)
				GroupsList = self.ConvertUsersListToString(Groups,self.GroupSep)
				if UsersList is None or GroupsList is None:
					error_msg = 'Error formatting users/groups list'
					self.UserRegLogger.error('[%s] == Error == \n %s'%('AdduserData',error_msg))
					return (-1,error_msg)
				print UsersList
				return self.Create(str(datetime.datetime.now()),Desc,UsersList,GroupsList,"-1",rid,ctid,op_insert,by,ip)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('AdduserData'))
			return (-1,'Error at business level AdduserData function in UserReg')
			
	def DeleteUsers(self,AppLabel,Model,rid,Users,Groups,by,ip,op_delete=SYSTEM_PERMISSION_DELETE):
		try:
			ctid = -1
			ctlist = getContentTypes()
			for ctobj in ctlist:
				if ctobj.app_label == AppLabel and ctobj.model == Model:
					ctid = ctobj.id
			if ctid == -1:
				#error here
				error_msg = 'Invalid Applabel %s or Model %s' % (AppLabel, Model)
				self.UserRegLogger.error('[%s] == Error == \n %s'%('DeleteUsers',error_msg))
				return (-1,error_msg)
			try:
				UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
				objlist = self.ConvertStringToUsersList(UserRegObj.Users,self.UserSep)
				user_list = self.ConvertStrListToInt(Users)
				new_list = []
				for x in objlist:
					if x not in user_list:
						new_list.append(x)
				UsersList = self.ConvertUsersListToString(new_list,self.UserSep)
				
				grplist = self.ConvertStringToUsersList(UserRegObj.Groups,self.GroupSep)
				group_list = self.ConvertStrListToInt(Groups)
				newgrp_list = []
				for x in grplist:
					if x not in group_list:
						newgrp_list.append(x)
				GroupsList = self.ConvertUsersListToString(newgrp_list,self.GroupSep)
				
				return self.Update(str(datetime.datetime.now()),UserRegObj.Desc,UsersList,GroupsList,"-1",rid,ctid,op_delete,by,ip,'deleted ' + str(user_list))
			except  ObjectDoesNotExist , DoesNotExist:
				error_msg = 'Error Record Does not exist'
				self.UserRegLogger.error('[%s] == Error == \n %s'%('DeleteUsers',error_msg))
				return (-1,error_msg)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('DeleteUsers'))
			return (-1,'Error at business level DeleteUsers function in UserReg')
			
			
			
	# SELECT FUNCTIONS
	
	def getUserIDListForARecord(self,AppLabel,Model,rid):
		try:
			ctid = -1
			ctlist = getContentTypes()
			for ctobj in ctlist:
				if ctobj.app_label == AppLabel and ctobj.model == Model:
					ctid = ctobj.id
			if ctid == -1:
				#error here
				error_msg = 'Invalid Applabel %s or Model %s' % (AppLabel, Model)
				self.UserRegLogger.error('[%s] == Error == \n %s'%('getUserIDListForARecord',error_msg))
				return (-1,error_msg)
			try:
				UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
				UserList = self.ConvertStringToUsersList(UserRegObj.Users,self.UserSep)
				GroupList = self.ConvertStringToUsersList(UserRegObj.Groups,self.GroupSep)
				#TODO get the users in this group , and then return the complete list
				CompleteUserList = UserList
				return (1,CompleteUserList)
			except  ObjectDoesNotExist , DoesNotExist:
				error_msg = 'Error Record Does not exist'
				self.UserRegLogger.error('[%s] == Error == \n %s'%('getUserIDListForARecord',error_msg))
				return (-1,error_msg)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('getUserIDListForARecord'))
			return (-1,'Error at business level getUserIDListForARecord function in UserReg')
			
	def getUserObjectListForARecord(self,AppLabel,Model,rid):
		try:
			ctid = -1
			ctlist = getContentTypes()
			for ctobj in ctlist:
				if ctobj.app_label == AppLabel and ctobj.model == Model:
					ctid = ctobj.id
			if ctid == -1:
				#error here
				error_msg = 'Invalid Applabel %s or Model %s' % (AppLabel, Model)
				self.UserRegLogger.error('[%s] == Error == \n %s'%('getUserObjectListForARecord',error_msg))
				return (-1,error_msg)
			try:
				UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
				user_id_list_str = str(self.getUserIDListForARecord(AppLabel,Model,rid)) # TODO check if it works
				query = "id IN (" +  user_id_list_str[1:-1] + ")" 
				UserObjList = User.objects.extra(where=[query])
				return (1,UserObjList)
			except  ObjectDoesNotExist , DoesNotExist:
				error_msg = 'Error Record Does not exist'
				self.UserRegLogger.error('[%s] == Error == \n %s'%('getUserObjectListForARecord',error_msg))
				return (-1,error_msg)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('getUserObjectListForARecord'))
			return (-1,'Error at business level getUserObjectListForARecord function in UserReg')
			
	def getContentTypeAndRecordByUserID(self,userid):
		try:
			query = self.UserSep + str(userid) + self.UserSep
			UserRegObjList = RegisterUser.objects.filter(Users__contains=query)
			return (1,UserRegObjList)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('getContentTypeAndRecordByUserID'))
			return (-1,'Error at business level getContentTypeAndRecordByUserID function in UserReg')
			
	def getContentTypeAndRecordByGroupID(self,gid):
		try:
			query = self.GroupSep + str(gid) + self.GroupSep
			GroupRegObjList = RegisterUser.objects.filter(Groups__contains=query)
			return (1,GroupRegObjList)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('getContentTypeAndRecordByGroupID'))
			return (-1,'Error at business level getContentTypeAndRecordByGroupID function in UserReg')
			
	def geRecordIDListByUserIDAndContentType(self,Applabel,Model,userid):
		try:
			ctid = -1
			ctlist = getContentTypes()
			for ctobj in ctlist:
				if ctobj.app_label == Applabel and ctobj.model == Model:
					ctid = ctobj.id
			if ctid == -1:
				#error here
				error_msg = 'Invalid Applabel %s or Model %s' % (AppLabel, Model)
				self.UserRegLogger.error('[%s] == Error == \n %s'%('geRecordIDListByUserIDAndContentType',error_msg))
				return (-1,error_msg)
			try:
				query = "$" + str(userid) + "$"
				UserRegObjList = RegisterUser.objects.filter(Users__contains=query,ContentType__id=ctid)
				return (1,UserRegObjList)
			except  ObjectDoesNotExist , DoesNotExist:
				error_msg = 'Error Record Does not exist'
				self.UserRegLogger.error('[%s] == Error == \n %s'%('geRecordIDListByUserIDAndContentType',error_msg))
				return (-1,error_msg)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('geRecordIDListByUserIDAndContentType'))
			return (-1,'Error at business level geRecordIDListByUserIDAndContentType function in UserReg')
			
			
	def geRecordIDListByGroupIDAndContentType(self,Applabel,Model,groupid):
		try:
			ctid = -1
			ctlist = getContentTypes()
			for ctobj in ctlist:
				if ctobj.app_label == Applabel and ctobj.model == Model:
					ctid = ctobj.id
			if ctid == -1:
				#error here
				error_msg = 'Invalid Applabel %s or Model %s' % (AppLabel, Model)
				self.UserRegLogger.error('[%s] == Error == \n %s'%('geRecordIDListByUserIDAndContentType',error_msg))
				return (-1,error_msg)
			try:
				query2 = self.GroupSep + str(groupid) + self.GroupSep
				GroupRegObjList = RegisterUser.objects.filter(Groups__contains=query2,ContentType__id=ctid)
				return (1,GroupRegObjList)
			except  ObjectDoesNotExist , DoesNotExist:
				error_msg = 'Error Record Does not exist'
				self.UserRegLogger.error('[%s] == Error == \n %s'%('geRecordIDListByUserIDAndContentType',error_msg))
				return (-1,error_msg)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('geRecordIDListByUserIDAndContentType'))
			return (-1,'Error at business level geRecordIDListByUserIDAndContentType function in UserReg')
