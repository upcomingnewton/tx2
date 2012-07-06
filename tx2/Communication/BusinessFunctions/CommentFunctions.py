from tx2.UserReg.models import RegisterUser
from tx2.Communication.models import *
from tx2.Communication.DBFunctions.DBFunctions import DBStateChangeComment , DBInsertComment
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypes,getContentTypesByAppNameAndModel,getStateIDbyStateName
from tx2.CONFIG import LOGGER_COMMUNICATION
from tx2.conf.LocalProjectConfig import *
import logging
import datetime

class CommentFnx():
	def __init__(self):
		self.CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
		
	def AddComment(self,_AppLabel,_Model,RecordID,UserID,CommentText,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT):
		try:
			ctid = getContentTypesByAppNameAndModel(_AppLabel,_Model)
			if ctid == -1:
				error_msg = 'Invalid Applabel %s or Model %s' % (_AppLabel, _Model)
				self.CommunicationLogger.error('[%s] == Error == \n %s'%('AddComment',error_msg))
				return (-1,error_msg)
			StateID = getStateIDbyStateName(StateName)
			if StateID == -1:
				error_msg = 'Invalid StateName %s ' % (StateName)
				self.CommunicationLogger.error('[%s] == Error == \n %s'%('AddComment',error_msg))
				return (-1,error_msg)
			details = {
					'ContentType':ctid,
					'RecordID':RecordID,
					'UserID':UserID,
					'CommentText':CommentText,
					'op':RequestedOperation,
					'by':by,
					'ip':ip,
				}
			res = DBInsertComment(details)
			return res
		except:
			error_msg = 'Error @ AddComment in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('AddComment'))
			return (-5,error_msg)
			
	def CommentStateChange(self,CommentID,by,ip,RequestedOperation=SYSTEM_PERMISSION_UPDATE,PreviousState=-1):
		try:
			if PreviousState == -1:
				CommentObj = Comment.objects.get(id=CommentID)
				if CommentObj is None:
					error_msg = 'Invalid CommentID'
					self.CommunicationLogger.error('[%s] == Error == \n %s'%('CommentStateChange',error_msg))
					return (-1,error_msg)
				PreviousState =  CommentObj.State
			StateID = getStateIDbyStateName(StateName)
			if StateID == -1:
				error_msg = 'Invalid StateName %s ' % (StateName)
				self.CommunicationLogger.error('[%s] == Error == \n %s'%('CommentStateChange',error_msg))
				return (-1,error_msg)
			details = {
					'CommentID':CommentID,
					'LogsDesc': 'PrState ' + str(PreviousState),
					'op':RequestedOperation,
					'by':by,
					'ip':ip,
				}
			res = DBStateChangeComment(details)
			return res
		except:
			error_message = 'Error @ CommentStateChange in Business Functions'
			self.CommunicationLogger.exception('[%s] == Exception =='%('AddComment'))
			return (-5,error_msg)

