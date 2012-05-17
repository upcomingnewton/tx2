'''
Created on Mar 3, 2012

@author: nitin
'''
from tx2.DataBaseHelper import DBhelper
from tx2.CONFIG import LoggerSecurity, LoggerQuery
import logging

SecurityLogger = logging.getLogger(LoggerSecurity)
QueryLogger = logging.getLogger(LoggerQuery)

# USER SYSTEM
### ========================================================================================================  ### 


def DBInsertState(details):
    try:
        #query = "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['state'] + "','" + userdetails['group'] + "','" + userdetails['logsdesc'] + "','" + str(userdetails['by_email']) + "','" + userdetails['ip'] +"'); "
        query = "SELECT * FROM securitystateinsert('" + details['name'] + "','" + details['desc'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
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
        #query = "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['state'] + "','" + userdetails['group'] + "','" + userdetails['logsdesc'] + "','" + str(userdetails['by_email']) + "','" + userdetails['ip'] +"'); "
        query = "SELECT * FROM securitypermissioninsert('" + details['name'] + "','" + details['desc'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        SecurityLogger.debug('[%s] %s'%('DBInsertPermission',query))
        QueryLogger.debug('[%s] %s'%('DBInsertPermission',query))
        result =  DBhelper.CallFunction(query)
        SecurityLogger.debug('[%s] %s'%('DBInsertPermission',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertPermission',query)
        SecurityLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}