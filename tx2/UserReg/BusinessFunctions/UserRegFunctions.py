from tx2.UserReg.models import RegisterUser
from tx2.UserReg.DBFunctions.DBFunctions import DBRegUserUpdate,DBRegUserInsert
from tx2.UserReg.models import RegisterUser
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
	def ConvertUsersListToString(self,UsersList):
		try:
			userstr = '$'
			for user in UsersList:
				userstr = userstr + user + '$'
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
			print 'int res' , res
			print 'str res' , _str
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
				UsersList = UserRegObj.Users[:-1] + self.ConvertUsersListToString(Users)
				return self.Update(str(datetime.datetime.now()),Desc,UsersList,rid,ctid,op_update,by,ip,'added ' + Users):
				return (1,'update')
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
