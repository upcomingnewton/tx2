from django.db import models
from django.contrib.contenttypes.models import ContentType
from tx2.Security.models import SecurityGroupContent
from tx2.Security.DBFunctions.DatabaseFunctions import DBGroupContentSecurityInsert
from tx2.Users.models import Group
from tx2.CONFIG import LoggerSecurity
import logging


class ContentTypeFnx():
    
        def __init__(self):
            self.SecurityLogger = logging.getLogger(LoggerSecurity)
            
        def CreateGroupContentSecurity(self,groupid,stateid,permissionid,ctid,userid,ip):
        	try:
			if groupid == -1 or stateid == -1 or permissionid == -1 or ctid == -1:
				return (-1,'Invalid values. Values Passed are not proper')
			details = {
				'groupid':groupid,
				'ctid':ctid,
				'permissionid':permissionid,
				'stateid':stateid,
				'userid':userid,
				'ip':ip,
			}
			result = DBGroupContentSecurityInsert(details)
			return result
		except:
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
