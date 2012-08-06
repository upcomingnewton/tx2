from tx2.UserReg.models import RegisterUser
from tx2.UserReg.DBFunctions import DBRegUserUpdate,DBRegUserInsert
from tx2.CONFIG import LOGGER_UserReg
import logging

class UserRegFnx():
	def __init__(self):
		self.Logger = logging.getlogger(LOGGER_UserReg)
		
	def Create(self):
		try:
			details = {
					'MetaInfo':MetaInfo,
					'Desc':Desc,
					'Users':Users,
					'Record':Record,
					'ContentType':ContentType,
					'Operation':Operation,
					'by':by,
					'ip':ip
				}
		except:
			self.Logger.exception('[%s] == Exception =='%('Create'))
			return (-1,'Error at business level functions while creating group')
