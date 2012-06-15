from django.db import models
from tx2.Users.models import Group
from tx2.Users.DBFunctions.DatabaseFunctions import DBGroupInsert
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_ENTITY,CACHE_KEY_SYSTEM_ENTITY
from tx2.Misc.CacheManagement import setCache,getCache
from tx2.Security.models import Entity
import logging

class GroupFnx(models.Model):
    
        def __init__(self):
            #self.encrypt = Encrypt()
            self.UserLogger = logging.getLogger(LoggerUser)
            
        #CRUD FUNCTIONS
        
        def CreateGroup(self,gname,gdesc,gtype,entity,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
            eid = entity
            if entity == -1:
            	e_obj = Entity.objects.get(EntityName=SYSTEM_ENTITY)
            	setCache(CACHE_KEY_SYSTEM_ENTITY,e_obj.id)
            	eid = e_obj.id
            try:
                self.UserLogger.debug('inside CreateGroup')
                details = {
                           'ip':ip,
                           'by':by,
                           'RequestedOperation':req_op,
                           'GroupEntity':eid,
                           'GroupType':gtype,
                           'GroupName':gname,
                           'GroupDescription':gdesc,
                           }
                result = DBGroupInsert(details)
                self.UserLogger.debug('[%s] %s,%s'%('CreateGroup',str(details),str(result)))
                return (result)
            except:
                exception_log = ('[%s] %s,%s,%s,%s,%s,%s')%('CreateGroup',gname,gdesc,gtype,entity,by,ip)
                self.UserLogger.exception(exception_log)
                return (-1,'Exception Occoured at Business Functions while creating group')


        # SELECTION AND QUERY FUNCTIONS
            
        def ListAllGroups(self):
            try:
                grouplist =  Group.objects.all()
                self.UserLogger.debug('[%s] %s'%('ListAllGroups',str(len(grouplist))))
                return (1,grouplist)
            except:
                exception_log = ('[%s]')%('ListAllGroups')
                self.UserLogger.exception(exception_log)
                return (-1,[])
                    
        
    
#        def CreateSecGroupForComm(self,groupid,params,logsdec,by,ip):
#            details = {
#                        'groupid':groupid,
#                        'permission':'INSERT',
#                        'params':params,
#                        'logdesc':logsdec,
#                        'by':by,
#                        'ip':ip
#                       }
#            result = DBCreateSecGroupForCommunications(details)
#            return (result[0],decode(int(result[0]), result[1],'CreateSecGroupForComm'))
