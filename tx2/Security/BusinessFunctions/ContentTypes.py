from django.db import models
from django.contrib.contenttypes.models import ContentType
from tx2.Security.models import SecurityGroupContent
from tx2.Security.DBFunctions.DatabaseFunctions import DBGroupContentSecurityInsert
from tx2.conf.LocalProjectConfig import *
from tx2.Users.models import Group
from tx2.CONFIG import LoggerSecurity
import logging


class ContentTypeFnx():
    
        def __init__(self):
            self.SecurityLogger = logging.getLogger(LoggerSecurity)
            
        def CreateGroupContentSecurity(self,groupid,stateid,permissionid,ctid,userid,ip,Operation=SYSTEM_PERMISSION_INSERT):
        	try:
			if groupid == -1 or stateid == -1 or permissionid == -1 or ctid == -1:
				self.SecurityLogger.debug('invalid values passed, groupid = %d,stateid = %d,permissionid = %d,ctid = %d,userid = %d,ip = %s,Operation = %s'%(groupid,stateid,permissionid,ctid,userid,ip,Operation))
				
				return (-1,'Invalid values. Values Passed are not proper')
			details = {
				'groupid':groupid,
				'ctid':ctid,
				'permissionid':permissionid,
				'stateid':stateid,
				'userid':userid,
				'ip':ip,
				'op':Operation,
			}
			result = DBGroupContentSecurityInsert(details)
			return result
		except:
			self.SecurityLogger.exception('== Exception == , groupid = %d,stateid = %d,permissionid = %d,ctid = %d,userid = %d,ip = %s,Operation = %s'%(groupid,stateid,permissionid,ctid,userid,ip,Operation))
			return {'result':-11,'rescode':-1}
			
	def DeleteGroupContentSecurity(self,ctid,userid,ip,Operation=SYSTEM_PERMISSION_DELETE):
        	try:
			if groupid == -1 or stateid == -1 or permissionid == -1 or ctid == -1:\
				self.SecurityLogger.debug('Invalid Values ctid = %d,userid = %d,ip = %s,op = %s'%(ctid,userid,ip,Operation))
				return (-1,'Invalid values. Values Passed are not proper')
			details = {
				'ctid':ctid,
				'userid':userid,
				'ip':ip,
				'op':Operation,
			}
			result = DBGroupContentSecurityInsert(details)
			return result
		except:
			self.SecurityLogger.exception('== EXCEPTION == ctid = %d,userid = %d,ip = %s,op = %s'%(ctid,userid,ip,Operation))
			return {'result':-11,'rescode':-1}
            
        # SELECTION QUERIES
        
        def getDjangoContentTypes(self):
            try:
        	ctlist = ContentType.objects.all()
        	self.SecurityLogger.debug('[%s] %s'%('getDjangoContentTypes',str(len(ctlist))))
                return (1,ctlist)
            except:
                exception_log = ('[%s]')%(' == getDjangoContentTypes ==')
                self.SecurityLogger.exception(exception_log)
                return (-1,[])
        
        def getGroupSecuritybyContentTypes(self,ctid):
            try:
        	ctlist = SecurityGroupContent.objects.filter(ContentType=ctid)
        	self.SecurityLogger.debug('[%s] %s'%('getGroupSecuritybyContentTypes',str(len(ctlist))))
                return (1,ctlist)
            except:
                exception_log = ('[%s]')%(' == getGroupSecuritybyContentTypes ==')
                self.SecurityLogger.exception(exception_log)
                return (-1,[])
