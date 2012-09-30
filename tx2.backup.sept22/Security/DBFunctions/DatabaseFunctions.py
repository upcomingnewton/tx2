'''
Created on Mar 3, 2012

@author: nitin
'''
from tx2.DataBaseHelper import DBhelper
from tx2.CONFIG import LoggerSecurity, LoggerQuery
import logging

SecurityLogger = logging.getLogger(LoggerSecurity)
QueryLogger = logging.getLogger(LoggerQuery)

#
### ========================================================================================================  ### 


def DBInsertState(details):
    try:
        #SELECT * FROM SecurityStateInsert('testfromdb','testfromdb','SYS_PER_INSERT',1,'testfromdb');
        query = "SELECT * FROM SecurityStateInsert('" + details['name'] + "','" + details['desc'] + "','" + details['Operation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        SecurityLogger.debug('[%s] %s'%('DBInsertState',query))
        QueryLogger.debug('[%s] %s'%('DBInsertState',query))
        result =  DBhelper.CallFunction(query)
        SecurityLogger.debug('[%s] %s'%('DBInsertState',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertState',query)
        SecurityLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
def DBInsertPermission(details):
    try:
        #SELECT * FROM SecurityPermissionInsert('testfromdb','testfromdb','SYS_PER_INSERT',1,'testfromdb');
        query = "SELECT * FROM securitypermissioninsert('" + details['name'] + "','" + details['desc'] + "','" + details['Operation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        SecurityLogger.debug('[%s] %s'%('DBInsertPermission',query))
        QueryLogger.debug('[%s] %s'%('DBInsertPermission',query))
        result =  DBhelper.CallFunction(query)
        SecurityLogger.debug('[%s] %s'%('DBInsertPermission',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertPermission',query)
        SecurityLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
        
def DBGroupContentSecurityInsert(details):
    try:
    	#SELECT * FROM SecurityGroupContent_Insert(  2, 9, 1,  1,  'SYS_PER_INSERT',1,'testfromdb');
        query = "SELECT * FROM SecurityGroupContent_Insert(" + str(details['groupid']) + "," + str(details['ctid']) + "," + str(details['permissionid']) + "," + str(details['stateid']) + ",'"+ details['op'] +"'," + str(details['userid']) + ",'" + details['ip'] + "');"
        SecurityLogger.debug('[%s] %s'%('DBGroupContentSecurityInsert',query))
        QueryLogger.debug('[%s] %s'%('DBGroupContentSecurityInsert',query))
        result =  DBhelper.CallFunction(query)
        SecurityLogger.debug('[%s] %s'%('DBGroupContentSecurityInsert',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBGroupContentSecurityInsert',query)
        SecurityLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
def DBGroupContentSecurityDelete(details):
    try:
    	#SELECT * FROM  SecurityGroupContent_Delete(16,'SYS_PER_DELETE',1,'testfromdb');
        query = "SELECT * FROM SecurityGroupContent_Delete(" + str(details['ctid']) + ",'" + details['op'] + "'," + str(details['userid']) + ",'" + details['ip'] + "');"
        SecurityLogger.debug('[%s] %s'%('DBGroupContentSecurityDelete',query))
        QueryLogger.debug('[%s] %s'%('DBGroupContentSecurityDelete',query))
        result =  DBhelper.CallFunction(query)
        SecurityLogger.debug('[%s] %s'%('DBGroupContentSecurityDelete',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBGroupContentSecurityDelete',query)
        SecurityLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}


