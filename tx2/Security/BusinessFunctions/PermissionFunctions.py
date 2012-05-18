from tx2.Security.models import SecurityPermissions
from tx2.CONFIG import LoggerSecurity
from tx2.Security.SecurityConfig import InitPermission, PermissionInsert
from tx2.Security.DBFunctions.DatabaseFunctions import DBInsertPermission
from tx2.Security.DBFunctions.DBMessages import decode
import logging

class PermissionFnx():
    
        def __init__(self):
            self.SecurityLogger = logging.getLogger(LoggerSecurity)
            
        #CRUD FUNCTIONS
        
        def CreatePermission(self,PermName,PermDesc,OperationFlag,entity,by,ip):
            try:
                self.SecurityLogger.debug('inside CreatePermission')
                if OperationFlag == 1:
                    Operation = InitPermission
                else:
                    Operation = PermissionInsert
                details = {
                           'ip':ip,
                           'by':by,
                           'Operation':Operation,
                           'name':PermName,
                           'desc':PermDesc,
                           }
                result = DBInsertPermission(details)
                self.SecurityLogger.debug('[%s] %s,%s'%('CreatePermission',str(details),str(result)))
                return (result,decode(int(result['result']), result['rescode']))
            except:
                exception_log = ('[%s] PermName = %s, PermDesc = %s, OperationFlag = %s, entity = %s, by = %s, ip = %s')%('CreateState',PermName,PermDesc,OperationFlag,entity,by,ip)
                self.SecurityLogger.exception(exception_log)
                return (-1,'Exception Occoured at Business Functions while creating permission')


        # SELECTION AND QUERY FUNCTIONS
            
        def ListAllPermissions(self):
            try:
                SecurityPermissionsList =  SecurityPermissions.objects.all()
                self.SecurityLogger.debug('[%s] %s'%('ListAllPermissions',str(len(SecurityPermissionsList))))                
                return (1,SecurityPermissionsList)
            except:
                exception_log = ('[%s]')%('ListAllPermissions')
                self.SecurityLogger.exception(exception_log)
                return (-1,[])