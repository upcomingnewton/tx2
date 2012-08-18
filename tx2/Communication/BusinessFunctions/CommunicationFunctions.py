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
from tx2.Misc.CacheManagement import *
from tx2.Users.models import User as _User
from django.core.paginator import Paginator
import re

class MessageFnx():
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
					#'UsersReg':UsersReg,
					#'Comment':Comment,
					
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
			
			
			#loads(Comm.Title.decode("base64").decode("zip"))
			
	def getCommunicationByType(self,CommType):
		try:
			Comm= Messages.objects.filter(CommunicationType=CommType)
			
			return Comm
		except:
			return -1
		
		
	
	
	
	
	def PostMessage(self,Title,Content,Users,Desc,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel='communication',_Model='messages',Record=-1,UsersReg=1):
		try:
			res=self.InsertCommunication(Title, Content, KEY_MESSAGES_COMMUNICATION_TYPE, 'Default', -1, -1, by, ip)
			
			
			return UserRegFunctions.UserRegFnx().AdduserData(_AppLabel,_Model,res['rescode'],Desc, Users, by, ip)
			
		except:
			error_msg = 'Error @ PostMessage in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('PostMessage'))
			return (-5,error_msg)
	
	#####
		
	
		
	def updateHappeningsCache(self):
		
		#print "herre"
		commtypeID=CommunicationTypeFnx().getCommunicationTypeIDbyName("NEWS")
		M=Messages.objects.filter(CommunicationType=commtypeID).order_by("Timestamp")
		P=Paginator(M,10)
		deleteCacheKey("HappeningsCache")
		setCache("HappeningsCache", P)
		#print "done cache"
		return 1
	def getNHappenings(self,n=3):
			try:	
				Pages=getCache("HappeningsCache")
				if(Pages is None):
					commtypeID=CommunicationTypeFnx().getCommunicationTypeIDbyName("NEWS")
					M=Messages.objects.filter(CommunicationType=commtypeID).order_by("Timestamp")
					M=M.reverse()
					P=Paginator(M,10)
					deleteCacheKey("HappeningsCache")
					setCache("HappeningsCache", P)
					Pages=getCache("HappeningsCache")
				M=Pages.page(1)
				M=M.object_list
				M=M[:n]
				return M
			except:
				error_msg = 'Error @ getNHappenings in Business Functions'
				self.CommunicationLogger.exception('[%s] == Exception =='%('getNHappenings'))
				return (-5,error_msg)
	
	def getHappenings(self, index):
		try:
			Pages=getCache("HappeningsCache")
			if(Pages is None):
				print "cache not found"
				commtypeID=CommunicationTypeFnx().getCommunicationTypeIDbyName("NEWS")
				M=Messages.objects.filter(CommunicationType=commtypeID).order_by("Timestamp")
				M=M.reverse()
				for i in M:
					i.User=_User.objects.get(id=i.User)
				P=Paginator(M,10)
				deleteCacheKey("HappeningsCache")
				setCache("HappeningsCache", P)
				Pages=getCache("HappeningsCache")
				
				
				
			#print "here"
			#print Pages.page_range
			
			
			if(index in Pages.page_range):
				#print "here"
				page=Pages.page(index)
				Page=page.object_list
				
				
				return [Page,page.has_next(),page.has_previous(), Pages.page_range]
			
			else:
				return -1
		
		except:
			error_msg = 'Error @ getHappenings in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('getHappenings'))
			return (-5,error_msg)
		
		
	
	
	def replaceUrls(self,content):

	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
	    
	    for i in urls:
	         k= "<a href='"+i+"' target='new' >"+i+"</a>"
	         content=content.replace(i,k)
	    return content		
			
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
	def PostNotice(self,Title,Content,Timestamp,Users,Desc,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel='Communication',_Model='messages',Record=-1,UsersReg=0):
		try:
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)

			res=self.InsertCommunication(Title, Content, KEY_NOTICES_COMMUNICATION_TYPE, 'Default',Timestamp, -1, -1, by, ip)
			return UserRegFunctions.UserRegFnx().Create(str(datetime.datetime.now()),Desc,Users,res["rescode"],ctid,SYSTEM_PERMISSION_INSERT,by,ip)
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
	
	
	def PostNews(self,Title,Content,tstamp,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT,_AppLabel='Communication',_Model='messages',Record=-1,UsersReg=0):
		try:
			#tstamp = datetime.datetime.now()
			deleteCacheKey("HappeningsCache")
			#print "Sarv"
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			return self.InsertCommunication(Title, Content, KEY_NEWS_COMMUNICATION_TYPE, 'Default',tstamp, -1, -1, by, ip)
		except:
			error_msg = 'Error @ PostNews in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('PostNews'))
			return (-5,error_msg)
			
			
			
