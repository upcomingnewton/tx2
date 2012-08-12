from tx2.UserReg.models import RegisterUser
from tx2.UserReg.BusinessFunctions import UserRegFunctions
from tx2.Communication.models import *
from tx2.Communication.DBFunctions.DBFunctions import DBInsertCommunication,DBUpdateCommunication, DBInsertAttachment,DBUpdateAttachment
from tx2.Communication.BusinessFunctions.CommunicationTypeFunctions import CommunicationTypeFnx
from tx2.Communication.BusinessFunctions.CommunicationTemplateFunctions import CommunicationTemplateFnx
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypes,getContentTypesByAppNameAndModel,getStateIDbyStateName
from tx2.CONFIG import LOGGER_COMMUNICATION
from tx2.conf.LocalProjectConfig import *
import logging
import datetime
from cPickle import dumps, loads



class MessageFnx():
	def __init__(self):
		self.CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
		
		
		
	def InsertCommunication(self,Title,Content,CommunicationTypeName, CommunicationTemplateName,CTID,Record,by,ip,RequestedOperation='SYS_PER_INSERT'):
		try:
			CommunicationTypeObj = CommunicationTypeFnx()
			CommunicationTypeID = CommunicationTypeObj.getCommunicationTypeIDbyName(CommunicationTypeName)
			if CommunicationTypeID == -1:
				error_msg = 'Invalid CommunicationTypeName %s ' % (CommunicationTypeName)
				self.CommunicationLogger.error('[%s] == Error == \n %s'%('InsertCommunication',error_msg))
				return (-1,error_msg)
			CommunicationTemplateObj = CommunicationTemplateFnx()
			CommunicationTemplateID = CommunicationTemplateObj.getCommunicationTemplateIDbyName(CommunicationTemplateName)
			if CommunicationTemplateID == -1:
				error_msg = 'Invalid CommunicationTemplateName %s ' % (CommunicationTemplateName)
				self.CommunicationLogger.error('[%s] == Error == \n %s'%('InsertCommunication',error_msg))
				return (-1,error_msg)
			
			Title= dumps(Title).encode("zip").encode("base64").strip()
			Content= dumps(Content).encode("zip").encode("base64").strip()
			
			details = {
					'Title':Title,
					'Content':Content,
					#'UsersReg':UsersReg,
					#'Comment':Comment,
					
					'CommunicationType':CommunicationTypeID,
					'CommunicationTemplate':CommunicationTemplateID,
					'RefContentType':CTID,
					'Record':Record,
					'op':RequestedOperation,
					'by':by,
					'ip':ip,
				}
			res = DBInsertCommunication(details)
			return res
		except:
			error_msg = 'Error @ InsertCommunication in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('InsertCommunication'))
			return (-5,error_msg)
			
	def UpdateCommunication(self,MessageID,Title,Content,UsersReg,Comment,CommunicationTypeName, CommunicationTemplateName,CTID,Record,by,ip,RequestedOperation,LogsDesc):
		try:
			CommunicationTypeObj = CommunicationTypeFnx()
			CommunicationTypeID = CommunicationTypeObj.getCommunicationTypeIDbyName(CommunicationTypeName)
			if CommunicationTypeID == -1:
				error_msg = 'Invalid CommunicationTypeName %s ' % (CommunicationTypeName)
				self.CommunicationLogger.error('[%s] == Error == \n %s'%('UpdateCommunication',error_msg))
				return (-1,error_msg)
			CommunicationTemplateObj = CommunicationTemplateFnx()
			CommunicationTemplateID = CommunicationTemplateObj.getCommunicationTemplateIDbyName(CommunicationTemplateName)
			
			
			
			if CommunicationTemplateID == -1:
				error_msg = 'Invalid CommunicationTemplateName %s ' % (CommunicationTemplateName)
				self.CommunicationLogger.error('[%s] == Error == \n %s'%('UpdateCommunication',error_msg))
				return (-1,error_msg)
				
			
			Title= dumps(Title).encode("zip").encode("base64").strip()
			Content= dumps(Content).encode("zip").encode("base64").strip()
			details = {
					'MessageID':MessageID,
					'Title':Title,
					'Content':Content,
					#'UsersReg':UsersReg,
					#'Comment':Comment,
					'CommunicationType':CommunicationTypeID,
					'CommunicationTemplate':CommunicationTemplateID,
					'RefContentType':CTID,
					'Record':Record,
					'op':RequestedOperation,
					'by':by,
					'ip':ip,
					'LogsDesc':LogsDesc,
				}
			res = DBUpdateCommunication(details)
			return res
		except:
			error_msg = 'Error @ UpdateMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateCommunication'))
			return (-5,error_msg)
			
			
			#loads(Comm.Title.decode("base64").decode("zip"))
			
	def getCommunicationByType(self,CommType):
		try:
			Comm= Messages.objects.filter(CommunicationType=CommType)
			
			return Comm
		except:
			return -1
		
	
	
	
	def PostMessage(self,Title,Content,Users,Desc,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=1):
		try:
			res=self.InsertCommunication(Title, Content, KEY_MESSAGES_COMMUNICATION_TYPE, 'Default', -1, -1, by, ip)
			ctid_ = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			ctid= ctid_
			print ctid_
			
			UserRegFunctions.UserRegFnx().AdduserData1(ctid,res['rescode'],Desc, Users, by, ip)
			
		except:
			error_msg = 'Error @ PostMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('PostMessage'))
			return (-5,error_msg)
	
	#####
			
	def UpdateMessage(self,MID,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_UPDATE,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=1):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			return self.UpdateMessage(MID,Title,Content,UsersReg,Comment,tstamp,KEY_MESSAGES_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation,'updating')
		except:
			error_msg = 'Error @ UpdateMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateMessage'))
			return (-5,error_msg)
	#####		
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
	
	def UpdateNews(self,MID,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=0):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			return self.UpdateMessage(MID,Title,Content,UsersReg,Comment,tstamp, KEY_NEWS_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation,'updating')
		except:
			error_msg = 'Error @ UpdateNews in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateNews'))
			return (-5,error_msg)
	
	
	def PostNews(self,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=0):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			return self.InsertMessage(Title,Content,UsersReg,Comment,tstamp,KEY_NEWS_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation)
		except:
			error_msg = 'Error @ PostNews in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('PostNews'))
			return (-5,error_msg)
			
			
			
