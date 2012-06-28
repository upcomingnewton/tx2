from tx2.UserReg.models import RegisterUser
from tx2.UserReg.DBFunctions.DBFunctions import DBRegUserUpdate,DBRegUserInsert
from tx2.UserReg.models import RegisterUser
from tx2.Users.models import User
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypes
from tx2.CONFIG import LOGGER_UserReg
import logging
import datetime
from tx2.conf.LocalProjectConfig import *
from django.core.exceptions import ObjectDoesNotExist

class UserRegFnx():
	def __init__(self):
		self.UserRegLogger = logging.getLogger(LOGGER_UserReg)
		
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
	
	def ConvertUsersListToString(self,UsersList):
		try:
			userstr = '$'
			for user in UsersList:
				userstr = userstr + str(user) + '$'
			self.UserRegLogger.debug('[%s] == %s =='%('ConvertUsersListToString',userstr))
			return userstr
		except:
			return None
	
	#Internal function
	def ConvertStringToUsersList(self,UsersList):
		try:
			_str = UsersList.split('$')
			_str = _str[1:-1]
			res = [int(i) for i in _str]
			return res
		except:
			return None
		
	def Create(self,MetaInfo,Desc,Users,Record,ContentType,Operation,by,ip):
		try:
			details = {
					'MetaInfo':MetaInfo,
					'Desc':Desc,
					'Users':Users,
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
			
	def Update(self,MetaInfo,Desc,Users,Record,ContentType,Operation,by,ip,LogsDesc):
		try:
			details = {
					'MetaInfo':MetaInfo,
					'Desc':Desc,
					'Users':Users,
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
			
	def AdduserData(self,AppLabel,Model,rid,Desc,Users,by,ip,op_insert=SYSTEM_PERMISSION_INSERT,op_update=SYSTEM_PERMISSION_UPDATE):
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
			try:
				UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
				objlist = self.ConvertStringToUsersList(UserRegObj.Users)
				user_list = self.ConvertStrListToInt(Users)
				UsersList = objlist + user_list
				UsersList = self.getUniqueIntList(UsersList)
				UsersList = self.ConvertUsersListToString(UsersList)
				return self.Update(str(datetime.datetime.now()),Desc,UsersList,rid,ctid,op_update,by,ip,'added ' + str(user_list))
			except  ObjectDoesNotExist , DoesNotExist:
				UsersList = self.ConvertUsersListToString(Users)
				if UsersList is None:
					error_msg = 'Error formatting users list'
					self.UserRegLogger.error('[%s] == Error == \n %s'%('AdduserData',error_msg))
					return (-1,error_msg)
				return self.Create(str(datetime.datetime.now()),Desc,UsersList,rid,ctid,op_insert,by,ip)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('AdduserData'))
			return (-1,'Error at business level AdduserData function in UserReg')
			
	def DeleteUsers(self,AppLabel,Model,rid,Users,by,ip,op_delete=SYSTEM_PERMISSION_DELETE):
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
				objlist = self.ConvertStringToUsersList(UserRegObj.Users)
				user_list = self.ConvertStrListToInt(Users)
				new_list = []
				for x in objlist:
					if x not in user_list:
						new_list.append(x)
				UsersList = self.ConvertUsersListToString(new_list)
				return self.Update(str(datetime.datetime.now()),UserRegObj.Desc,UsersList,rid,ctid,op_delete,by,ip,'deleted ' + str(user_list))
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
				return (1,self.ConvertStringToUsersList(UserRegObj.Users))
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
				user_id_list_str = str(self.ConvertStringToUsersList(UserRegObj.Users))
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
			query = "$" + str(userid) + "$"
			UserRegObjList = RegisterUser.objects.filter(Users__contains=query)
			return (1,UserRegObjList)
		except:
			self.UserRegLogger.exception('[%s] == Exception =='%('getContentTypeAndRecordByUserID'))
			return (-1,'Error at business level getContentTypeAndRecordByUserID function in UserReg')
			
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
