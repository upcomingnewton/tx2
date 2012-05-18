from django.db import models
from ThoughtXplore.txUser.models import User,Group,SecGroup_Comm
from ThoughtXplore.txMisc.Encryption.enc_dec import Encrypt
from ThoughtXplore.txUser.DBFunctions.DBMessages import decode
from ThoughtXplore.txUser.DBFunctions.DatabaseFunctions import DBCreateGroup,DBCreateSecGroupForCommunications
from ThoughtXplore.CONFIG import LOGGER_USER
import logging

class GroupFnx(models.Model):
    
        def __init__(self):
            self.encrypt = Encrypt()
            self.UserLogger = logging.getLogger(LOGGER_USER)
            
        #CRUD FUNCTIONS
        
        def CreateGroup(self,gname,gdesc,gtype,entity,by,ip):
            try:
                self.UserLogger.debug('inside CreateGroup')
                details = {
                           'ip':ip,
                           'by':by,
                           'request':'INSERT',
                           'entity':entity,
                           'group_type_id':gtype,
                           'groupname':gname,
                           'groupdesc':gdesc,
                           }
                result = DBCreateGroup(details)
                self.UserLogger.debug('[%s] %s,%s'%('CreateGroup',str(details),str(result)))
                return (result,decode(int(result['result']), result['rescode']))
            except:
                exception_log = ('[%s] %s,%s,%s,%s,%s,%s')%('CreateGroup',gname,gdesc,gtype,entity,by,ip)
                self.UserLogger.exception(exception_log)
                return (-1,'Exception Occoured at Business Functions while creating group')


        # SELECTION AND QUERY FUNCTIONS
            
        def ListAllGroups(self):
            try:
                grouplist =  Group.objects.all()
                self.UserLogger.debug('[%s] %s'%('getParentMenus',str(grouplist)))
                return (1,grouplist)
            except:
                exception_log = ('[%s]')%('getParentMenus')
                self.UserLogger.exception(exception_log)
                return (-1,[])
                    
        
    
        def CreateSecGroupForComm(self,groupid,params,logsdec,by,ip):
            details = {
                        'groupid':groupid,
                        'permission':'INSERT',
                        'params':params,
                        'logdesc':logsdec,
                        'by':by,
                        'ip':ip
                       }
            result = DBCreateSecGroupForCommunications(details)
            return (result[0],decode(int(result[0]), result[1],'CreateSecGroupForComm'))