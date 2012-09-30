from tx2.UserReg.BusinessFunctions import UserRegFunctions
from tx2.Communication.models import *
from tx2.Communication.DBFunctions.DBFunctions import DBInsertCommunication,DBUpdateCommunication, DBInsertAttachment,DBUpdateAttachment
from tx2.Communication.BusinessFunctions.CommunicationTypeFunctions import CommunicationTypeFnx
from tx2.Communication.BusinessFunctions.CommunicationTemplateFunctions import CommunicationTemplateFnx
from tx2.Misc.CacheManagement import deleteCacheKey, setCache,getCache,getContentTypesByAppNameAndModel,getStateIDbyStateName
from tx2.CONFIG import LOGGER_COMMUNICATION
from tx2.conf.LocalProjectConfig import *
import logging
import datetime
from cPickle import dumps
from django.core.paginator import Paginator


class GetCommunicationFnx():
	def __init__(self):
		self.CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
	
	
	def getCommunicationByType(self,CommType):
		try:
			commtypeID=CommunicationTypeFnx().getCommunicationTypeIDbyName(CommType)
			Comm= Messages.objects.filter(CommunicationType=commtypeID)
			
			return Comm
		except:
			return -1
	
		
		
	
	def getNCommunicationsbyPageIndex(self,commType,n=0, index=0):
			try:	
				Pages=getCache(commType+"Cache")
				if(Pages is None):
					print "Cache Not Found"
					PostCommunicationFnx().setCommunicationCache(commType)
					Pages=getCache(commType+"Cache")
				Page=Pages.page(1)
				M=Page.object_list
				if(index!=0):
					if(index in Pages.page_range):
						Page=Pages.page(index)
						M=Page.object_list
					else:
						error_msg = 'Error @ getNCommunicationsbyPageIndex in Business Functions:Page Index does not exist'
						self.CommunicationLogger.exception('[%s] == Exception =='%('getNCommunicationsbyPageIndex'))
						return (-1,error_msg)
				if(n!=0):
					M=M[:n]
				return [M,Page.has_next(),Page.has_previous(), Pages.page_range]
			except:
				error_msg = 'Error @ getNCommunicationsbyPageIndex in Business Functions'
				self.CommunicationLogger.exception('[%s] == Exception =='%('getNCommunicationsbyPageIndex'))
				return (-5,error_msg)
	
		
	
class PostCommunicationFnx():
	def __init__(self):
		self.CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
			
	def InsertCommunication(self,Title,Content,CommunicationTypeName, CommunicationTemplateName, Timestamp,CTID,Record,by,ip,RequestedOperation='SYS_PER_INSERT'):
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
			##print "here111"
			Title= dumps(Title).encode("zip").encode("base64").strip()
			Content= dumps(Content).encode("zip").encode("base64").strip()
			#print "up here"
			details = {
					'Title':Title,
					'Content':Content,
					'CommunicationType':CommunicationTypeID,
					'CommunicationTemplate':CommunicationTemplateID,
					'Timestamp':Timestamp,
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
			
				
	def setCommunicationCache(self,commType):
		
		try:
			M= GetCommunicationFnx().getCommunicationByType(commType).order_by("Timestamp")
			M=M.reverse()
			P=Paginator(M,10)
			cache_name=commType+"Cache"
			print cache_name
			deleteCacheKey(cache_name)
			setCache(cache_name, P)
		except:
			
			error_msg = 'Error @ setCommunicationCache in Business Functions| Error fetching data from database'
			self.CommunicationLogger.exception('[%s] == Exception =='%('setCommunicationCache'))
			return (-5,error_msg)
		#print "done cache"
		return 1
			
	def UpdateMessage(self,MID,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_UPDATE,_AppLabel='communication',_Model='messages',Record=-1,UsersReg=1):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			return self.UpdateMessage(MID,Title,Content,UsersReg,Comment,tstamp,KEY_MESSAGES_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation,'updating')
		except:
			error_msg = 'Error @ UpdateMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateMessage'))
			return (-5,error_msg)
	#####		
	def PostMessage(self,Title,Content, UserList,GroupList, ReferenceToRegisterUser,Desc, by,ip, RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel='Communication', _Model='messages', Record=-1,UserReg=0):
		try:
			ctid=getContentTypesByAppNameAndModel(_AppLabel, _Model)
			if(ctid!=-1):
				res=self.InsertCommunication(Title, Content, KEY_MESSAGES_COMMUNICATION_TYPE, 'Default', datetime.datetime.now(), ctid, Record, by, ip, RequestedOperation)
				return UserRegFunctions.UserRegFnx().Create(str(datetime.datetime.now()), Desc, UserList, GroupList, ReferenceToRegisterUser, res["rescode"], ctid, RequestedOperation, by, ip)
			else:
				return -1
		except:
			error_msg = 'Error @ PostMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('PostMessage'))
			return (-5,error_msg)
			
	

	def PostNotice(self,Title,Content,Timestamp,Users,Desc,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel='Communication',_Model='messages',Record=-1,UsersReg=0):
		try:
			deleteCacheKey("NOTICESCache")
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			if(ctid!=-1):
				return self.InsertCommunication(Title, Content, KEY_NOTICES_COMMUNICATION_TYPE, 'Default',datetime.datetime.now(), -1, -1, by, ip)
			else:
				return -1
		except:
			error_msg = 'Error @ PostNotice in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('PostNotice'))
			return (-5,error_msg)


	def UpdateNotice(self,MID,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=0):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			if(ctid!=-1):
				return self.UpdateMessage(MID,Title,Content,UsersReg,Comment,tstamp,KEY_NOTICES_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation,'updating')
			else:
				return -1
		except:
			error_msg = 'Error @ UpdateNotice in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateNotice'))
			return (-5,error_msg)
	
	def UpdateNews(self,MID,Title,Content,Comment,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel=-1,_Model=-1,Record=-1,UsersReg=0):
		try:
			tstamp = datetime.datetime.now()
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			if(ctid!=-1):
				return self.UpdateMessage(MID,Title,Content,UsersReg,Comment,tstamp, KEY_NEWS_COMMUNICATION_TYPE,ctid,Record,by,ip,RequestedOperation,'updating')
			else:
				return -1
		except:
			error_msg = 'Error @ UpdateNews in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateNews'))
			return (-5,error_msg)
	
	
	def PostNews(self,Title,Content,tstamp,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel='Communication',_Model='messages',Record=-1,UsersReg=0):
		try:
			deleteCacheKey("NEWSCache")
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			if(ctid!=-1):
				return self.InsertCommunication(Title, Content, KEY_NEWS_COMMUNICATION_TYPE, 'Default',tstamp, -1, -1, by, ip)
			else:
				return -1
		except:
			error_msg = 'Error @ PostNews in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('PostNews'))
			return (-5,error_msg)
			
			
			
