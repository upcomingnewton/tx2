'''
Created on Mar 3, 2012

@author: nitin
'''
from tx2.DataBaseHelper import DBhelper
from tx2.CONFIG import LOGGER_UserReg, LoggerQuery
import logging

RegLogger = logging.getLogger(LOGGER_UserReg)
QueryLogger = logging.getLogger(LoggerQuery)

#
### ========================================================================================================  ### 


def DBRegUserInsert(details):
    try:
	#SELECT * FROM  UserRegInsert('MetaInfo','_Desc','Users','Groups','ReferenceToRegisterUser',1,1,'SYS_PER_INSERT',1,'ip');
        query = "SELECT * FROM UserRegInsert('" + details['MetaInfo'] + "','" + details['Desc'] + "','" + details['Users'] +"','" + details['Groups'] + "','" + details['ReferenceToRegisterUser'] + "',"+ str(details['Record']) + ","+ str(details['ContentType']) +",'" + details['Operation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        RegLogger.debug('[%s] %s'%('DBRegUserInsert',query))
        QueryLogger.debug('[%s] %s'%('DBRegUserInsert',query))
        result =  DBhelper.CallFunction(query)
        RegLogger.debug('[%s] %s'%('DBRegUserInsert',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBRegUserInsert',query)
        RegLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
def DBRegUserUpdate(details):
    try:
	#SELECT * FROM  UserRegUpdate('MetaInfo-updated','_Desc-updated','Users-updated',1,1,'SYS_PER_UPDATE','update test from db',1,'testfromdb');
        query = "SELECT * FROM UserRegUpdate('" + details['MetaInfo'] + "','" + details['Desc'] + "','" + details['Users'] +",'" + details['Groups'] + "','" + details['ReferenceToRegisterUser'] + "',"+ str(details['Record']) + ","+ str(details['ContentType']) +",'" + details['Operation'] + "','" + details['LogsDesc'] +"'," + str(details['by']) + ",'" + details['ip'] + "');"
        RegLogger.debug('[%s] %s'%('DBRegUserUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBRegUserUpdate',query))
        result =  DBhelper.CallFunction(query)
        RegLogger.debug('[%s] %s'%('DBRegUserUpdate',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBRegUserUpdate',query)
        RegLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}

def DBInsertPriority(details):
    try:
        
        if(details['Group'] is None):
            details['Group']=0        
        query= "SELECT * FROM UserGroupAppPriorityInsert('"+details['ContentType']+"','"+details['Record']+"','"+details['Group']+"','"+details['Priority']+"','"+details['Desc']+"','"+details['RequestedOperation']+"','"+details['ByUser']+"','"+details['ip']+"');"
        RegLogger.debug('[%s] %s'%('DBInsertPriority',query))
        QueryLogger.debug('[%s] %s'%('DBInsertPriority',query))
        result =  DBhelper.CallFunction(query)
        RegLogger.debug('[%s] %s'%('DBInsertPriority',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertPriority',query)
        RegLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}


def DBUpdatePriority(details):
    try:
        
        if(details['Group'] is None):
            details['Group']=0        
        query= "SELECT * FROM UserGroupAppPriorityUpdate('"+details['ContentType']+"','"+details['Record']+"','"+details['Group']+"','"+details['Priority']+"','"+details['Desc']+"','"+details['RequestedOperation']+"','"+details['LogsDesc']+"','"+details['ByUser']+"','"+details['ip']+"');"
        RegLogger.debug('[%s] %s'%('DBUpdatePriority',query))
        QueryLogger.debug('[%s] %s'%('DBUpdatePriority',query))
        result =  DBhelper.CallFunction(query)
        RegLogger.debug('[%s] %s'%('DBUpdatePriority',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBUpdatePriority',query)
        RegLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
