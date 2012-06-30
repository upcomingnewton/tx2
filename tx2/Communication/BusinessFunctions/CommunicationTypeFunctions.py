from tx2.UserReg.models import RegisterUser
from tx2.Communication.models import *
from tx2.Communication.DBFunctions.DBFunctions import DBInsertCommunicationType 
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypes,getContentTypesByAppNameAndModel,getStateIDbyStateName
from tx2.CONFIG import LOGGER_COMMUNICATION
from tx2.conf.LocalProjectConfig import *
import logging
import datetime

class CommunicationTypeFnx():
	def __init__(self):
		self.CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
		
	def InsertCommunicationType(self,CommTypeName,CommTypeDesc,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT):
		try:
			details = {
					'CommTypeName':CommTypeName,
					'CommTypeDesc':CommTypeDesc,
					'op':RequestedOperation,
					'by':by,
					'ip':ip,
				}
			res = DBInsertCommunicationType(details)
			return res
		except:
			error_msg = 'Error @ InsertCommunicationType in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('InsertCommunicationType'))
			return (-5,error_msg)
