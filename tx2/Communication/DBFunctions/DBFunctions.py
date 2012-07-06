'''
Created on Mar 3, 2012

@author: nitin
'''
from tx2.DataBaseHelper import DBhelper
from datetime import datetime
from tx2.CONFIG import LOGGER_COMMUNICATION, LoggerQuery
import logging

CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
QueryLogger = logging.getLogger(LoggerQuery)
# USER SYSTEM
### ========================================================================================================  ### 


def DBInsertCommunicationType(details):
    
    	#SELECT * FROM  CommunicationTypeInsert ( 'TEST-FROM-DB','TEST-FROM-DB','SYS_PER_INSERT',13,'TEST-FROM-DB');
    query = "SELECT * FROM CommunicationTypeInsert('" + details['CommTypeName'] + "','" + details['CommTypeDesc'] + "','" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] +"'); "
    try:
        CommunicationLogger.debug('[%s] %s'%('DBInsertCommunicationType',query))
        QueryLogger.debug('[%s] %s'%('DBInsertCommunicationType',query))
        result =  DBhelper.CallFunction(query)
        CommunicationLogger.debug('[%s] %s'%('DBInsertCommunicationType',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertCommunicationType',query)
        CommunicationLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        


def DBInsertMessage(details):
    query = "SELECT * FROM MessgaeInsert('" + details['Title'] + "','" + details['Content'] + "',"+str(details['UsersReg'])+","+str(details['Comment'])+",'"+str(details['Timestamp'])+"',"+str(details['CommunicationType'])+","+str(details['RefContentType'])+","+str(details['Record'])+",'" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] +"'); "
    try:
        CommunicationLogger.debug('[%s] %s'%('DBInsertMessage',query))
        QueryLogger.debug('[%s] %s'%('DBInsertMessage',query))
        result =  DBhelper.CallFunction(query)
        CommunicationLogger.debug('[%s] %s'%('DBInsertMessage',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertMessage',query)
        CommunicationLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
       
def DBUpdateMessage(details):
    query = "SELECT * FROM MessgaeUpdate(" + str(details['MessageID'])  +",'" + details['Title'] + "','" + details['Content'] + "'," + str(details['UsersReg']) + "," + str(details['Comment']) + ",'" + str(details['Timestamp']) + "'," + str(details['CommunicationType']) + "," + str(details['RefContentType']) + "," + str(details['Record']) + ",'" + details['op'] + "','" + details['LogsDesc'] + "'," + str(details['by']) + ",'" + details['ip'] +"'); "
    try:
        CommunicationLogger.debug('[%s] %s'%('DBUpdateMessage',query))
        QueryLogger.debug('[%s] %s'%('DBUpdateMessage',query))
        result =  DBhelper.CallFunction(query)
        CommunicationLogger.debug('[%s] %s'%('DBUpdateMessage',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBUpdateMessage',query)
        CommunicationLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        

def DBInsertComment(details):
    query = "SELECT * FROM CommentInsert(" + str(details['ContentType'])  +"," + str(details['RecordID']) + "," + str(details['UserID'])+ ",'" + details['CommentText'] +"','" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] +"'); "
    try:
        CommunicationLogger.debug('[%s] %s'%('DBInsertComment',query))
        QueryLogger.debug('[%s] %s'%('DBInsertComment',query))
        result =  DBhelper.CallFunction(query)
        CommunicationLogger.debug('[%s] %s'%('DBInsertComment',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertComment',query)
        CommunicationLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        

def DBStateChangeComment(details):
    query = "SELECT * FROM CommentStateChange(" + str(details['CommentID'])  + ",'" + details['LogsDesc'] + "','" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] +"'); "
    try:
        CommunicationLogger.debug('[%s] %s'%('DBStateChangeComment',query))
        QueryLogger.debug('[%s] %s'%('DBStateChangeComment',query))
        result =  DBhelper.CallFunction(query)
        CommunicationLogger.debug('[%s] %s'%('DBStateChangeComment',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBStateChangeComment',query)
        CommunicationLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
