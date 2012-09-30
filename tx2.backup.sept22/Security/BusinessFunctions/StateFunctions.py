from tx2.Security.models import SecurityStates
from tx2.CONFIG import LoggerSecurity
from tx2.Security.SecurityConfig import InitPermission, PermissionInsert
from tx2.Security.DBFunctions.DatabaseFunctions import DBInsertState
from tx2.Security.DBFunctions.DBMessages import decode
from tx2.conf.LocalProjectConfig import *
import logging

class StateFnx():
    
        def __init__(self):
            self.SecurityLogger = logging.getLogger(LoggerSecurity)
            
        #CRUD FUNCTIONS
        
        def CreateState(self,StateName,StateDesc,by,ip,Operation=SYSTEM_PERMISSION_INSERT):
            try:
                self.SecurityLogger.debug('inside CreateState')
                details = {
                           'ip':ip,
                           'by':by,
                           'Operation':Operation,
                           'name':StateName,
                           'desc':StateDesc,
                           }
                result = DBInsertState(details)
                self.SecurityLogger.debug('[%s] %s,%s'%('CreateState',str(details),str(result)))
                return (result,decode(int(result['result']), result['rescode']))
            except:
                exception_log = ('[%s] StateName = %s, StateDesc = %s, OperationFlag = %s, entity = %s, by = %s, ip = %s')%('CreateState',StateName,StateDesc,OperationFlag,entity,by,ip)
                self.SecurityLogger.exception(exception_log)
                return (-1,'Exception Occoured at Business Functions while creating state')


        # SELECTION AND QUERY FUNCTIONS
            
        def ListAllStates(self):
            try:
                SecurityStatesList =  SecurityStates.objects.all()
                self.SecurityLogger.debug('[%s] %s'%('ListAllStates',str(len(SecurityStatesList))))                
                return (1,SecurityStatesList)
            except:
                exception_log = ('[%s]')%('ListAllStates')
                self.SecurityLogger.exception(exception_log)
                return (-1,[])
