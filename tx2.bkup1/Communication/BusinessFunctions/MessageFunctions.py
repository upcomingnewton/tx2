from tx2.UserReg.models import RegisterUser
from tx2.Communication.models import *
from tx2.Communication.DBFunctions.DBFunctions import DBInsertMessage, DBUpdateMessage
from tx2.Communication.BusinessFunctions.CommunicationTypeFunctions import CommunicationTypeFnx
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypes,getContentTypesByAppNameAndModel,getStateIDbyStateName
from tx2.CONFIG import LOGGER_COMMUNICATION
from tx2.conf.LocalProjectConfig import *
import logging
import datetime

class MessageFnx():
	def __init__(self):
		self.CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
		
	def InsertMessage(self,Title,Content,UsersReg,Comment,Timestamp,CommunicationTypeName,CTID,Record,by,ip,RequestedOperation):
		try:
			CommunicationTypeObj = CommunicationTypeFnx()
			CommunicationTypeID = CommunicationTypeObj.getCommunicationTypeIDbyName(CommunicationTypeName)
			if CommunicationTypeID == -1:
				error_msg = 'Invalid CommunicationTypeName %s ' % (CommunicationTypeName)
				self.CommunicationLogger.error('[%s] == Error == \n %s'%('InsertMessage',error_msg))
				return (-1,error_msg)
			details = {
					'Title':Title,
					'Content':Content,
					'UsersReg':UsersReg,
					'Comment':Comment,
					'Timestamp':Timestamp,
					'CommunicationType':CommunicationTypeID,
					'RefContentType':CTID,
					'Record':Record,
					'op':RequestedOperation,
					'by':by,
					'ip':ip,
				}
			res = DBInsertMessage(details)
			return res
		except:
			error_msg = 'Error @ InsertMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('InsertMessage'))
			return (-5,error_msg)
			
	def UpdateMessage(self,MessageID,Title,Content,UsersReg,Comment,Timestamp,CommunicationTypeName,CTID,Record,by,ip,RequestedOperation,LogsDesc):
		try:
			CommunicationTypeObj = CommunicationTypeFnx()
			CommunicationTypeID = CommunicationTypeObj.getCommunicationTypeIDbyName(CommunicationTypeName)
			if CommunicationTypeID == -1:
				error_msg = 'Invalid CommunicationTypeName %s ' % (CommunicationTypeName)
				self.CommunicationLogger.error('[%s] == Error == \n %s'%('UpdateMessage',error_msg))
				return (-1,error_msg)
			details = {
					'MessageID':MessageID,
					'Title':Title,
					'Content':Content,
					'UsersReg':UsersReg,
					'Comment':Comment,
					'Timestamp':Timestamp,
					'CommunicationType':CommunicationTypeID,
					'RefContentType':CTID,
					'Record':Record,
					'op':RequestedOperation,
					'by':by,
					'ip':ip,
					'LogsDesc':LogsDesc,
				}
			res = DBUpdateMessage(details)
			return res
		except:
			error_msg = 'Error @ UpdateMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateMessage'))
			return (-5,error_msg)
			
	def PostMessage(self,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=1):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			return self.InsertMessage(Title,Content,UsersReg,Comment,tstamp,KEY_MESSAGES_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation)
		except:
			error_msg = 'Error @ PostMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('PostMessage'))
			return (-5,error_msg)
			
	def UpdateMessage(self,MID,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_UPDATE,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=1):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			return self.UpdateMessage(MID,Title,Content,UsersReg,Comment,tstamp,KEY_MESSAGES_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation,'updating')
		except:
			error_msg = 'Error @ UpdateMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateMessage'))
			return (-5,error_msg)
			
	def PostNotice(self,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=0):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			return self.InsertMessage(Title,Content,UsersReg,Comment,tstamp,KEY_NOTICES_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation)
		except:
			error_msg = 'Error @ PostNotice in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('PostNotice'))
			return (-5,error_msg)


	def UpdateNotice(self,MID,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=0):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			return self.UpdateMessage(MID,Title,Content,UsersReg,Comment,tstamp,KEY_NOTICES_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation,'updating')
		except:
			error_msg = 'Error @ UpdateNotice in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateNotice'))
			return (-5,error_msg)

