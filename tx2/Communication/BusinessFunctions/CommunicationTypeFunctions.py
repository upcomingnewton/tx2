from tx2.UserReg.models import RegisterUser
from tx2.Communication.models import *
from tx2.Communication.DBFunctions.DBFunctions import DBInsertCommunicationType 
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypes,getContentTypesByAppNameAndModel,getStateIDbyStateName, deleteCacheKey
from tx2.CONFIG import LOGGER_COMMUNICATION
from tx2.conf.LocalProjectConfig import *
import logging
import datetime

class CommunicationTypeFnx():
	def __init__(self):
		self.CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
		
	def InsertCommunicationType(self,CommTypeName,CommTypeDesc,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT):
		CACHE_COMMUNICATION_TYPES = 'CACHE_COMMUNICATION_TYPES'
		try:
			details = {
					'CommTypeName':CommTypeName,
					'CommTypeDesc':CommTypeDesc,
					'op':RequestedOperation,
					'by':by,
					'ip':ip,
				}
			res = DBInsertCommunicationType(details)
			deleteCacheKey(CACHE_COMMUNICATION_TYPES)
			return res
		except:
			error_msg = 'Error @ InsertCommunicationType in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('InsertCommunicationType'))
			return (-5,error_msg)
			
	def getCommunicationTypes(self):
		CACHE_COMMUNICATION_TYPES = 'CACHE_COMMUNICATION_TYPES'
		CommTypeList = getCache(CACHE_COMMUNICATION_TYPES)
		if CommTypeList is None:
			CommTypeList = CommunicationType.objects.all()
			setCache(CACHE_COMMUNICATION_TYPES,CommTypeList)
		return CommTypeList
	
	def getCommunicationTypeIDbyName(self,_CommunicationTypeName):
		CommunicationTypeID = -1
		CommTypeList = self.getCommunicationTypes()
		if  CommTypeList is None:
			return  CommunicationTypeID
		for CommTypeObj in CommTypeList:
			print CommTypeObj.CommName
			if CommTypeObj.CommName == _CommunicationTypeName:
				CommunicationTypeID = CommTypeObj.id
		print CommunicationTypeID
		return CommunicationTypeID
