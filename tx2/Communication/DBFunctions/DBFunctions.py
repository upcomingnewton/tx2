
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

def DBInsertCommunicationTemplate(details):
    
        #SELECT * FROM  CommunicationTypeInsert ( 'TEST-FROM-DB','TEST-FROM-DB','SYS_PER_INSERT',13,'TEST-FROM-DB');
    print "in DBFunction"
    print details

    query = "SELECT * FROM CommunicationTemplateInsert(" + str(details['CommunicationType']) + ",'" + details['TemplateName'] + "','" + details['TemplateDisc']+ "','" + details['TemplateFormat']+ "','" + details['paramList'] + "','" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] +"'); "
    print "good"
    
    print query
    try:    
        CommunicationLogger.debug('[%s] %s'%('DBInsertCommunicationTemplates',query))
        QueryLogger.debug('[%s] %s'%('DBInsertCommunicationTemplates',query))
        result =  DBhelper.CallFunction(query)
        print "done"
        CommunicationLogger.debug('[%s] %s'%('DBInsertCommunicationTemplate',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertCommunicationTemplate',query)
        CommunicationLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        


def DBInsertAttachment(details):
    query = "SELECT * FROM AttachmentInsert('" + details['ContentType'] + "','" + details['Record'] + "',"+str(details['AttachmentType'])+","+str(details['AttachmentDesc'])+",'"+str(details['AttachmentName'])+"',"+str(details['AttachmentRef'])+details['op'] + "'," + str(details['by']) + ",'" + details['ip']+"'); "
    try:
        CommunicationLogger.debug('[%s] %s'%('DBInsertAttachment',query))
        QueryLogger.debug('[%s] %s'%('DBInsertAttachment',query))
        result =  DBhelper.CallFunction(query)
        CommunicationLogger.debug('[%s] %s'%('DBInsertMessage',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertAttachment',query)
        CommunicationLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}


def DBInsertCommunication(details):
    print details
    query = "SELECT * FROM MessgaeInsert('" + details['Title'] + "','" + details['Content'] + "',"+str(details['CommunicationType'])+","+str(details['CommunicationTemplate'])+","+str(details['RefContentType'])+","+str(details['Record'])+",'" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] +"'); "
    print query
    
    try:
        CommunicationLogger.debug('[%s] %s'%('DBInsertCommunication',query))
        QueryLogger.debug('[%s] %s'%('DBInsertMessage',query))
        result =  DBhelper.CallFunction(query)
        CommunicationLogger.debug('[%s] %s'%('DBInsertCommunication',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertCommunication',query)
        CommunicationLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
       
def DBUpdateCommunication(details):
    query = "SELECT * FROM MessgaeUpdate(" + str(details['MessageID'])  +",'" + details['Title'] + "','" + details['Content'] + "'," + "'," + str(details['CommunicationType'])+"',"+str(details['CommunicationTemplate'])+","+ "," + str(details['RefContentType']) + "," + str(details['Record']) + ",'" + details['op'] + "','" + details['LogsDesc'] + "'," + str(details['by']) + ",'" + details['ip'] +"'); "
    try:
        CommunicationLogger.debug('[%s] %s'%('DBUpdateCommunication',query))
        QueryLogger.debug('[%s] %s'%('DBUpdateCommunication',query))
        result =  DBhelper.CallFunction(query)
        CommunicationLogger.debug('[%s] %s'%('DBUpdateCommunication',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBUpdateCommunication',query)
        CommunicationLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
    
def DBUpdateAttachment(details):
    query = "SELECT * FROM AttachmentUpdate('" + details['Content'] + "','" + details['Record'] + "',"+str(details['AttachmentType'])+","+str(details['AttachmentDesc'])+",'"+str(details['AttachmentName'])+"',"+str(details['AttachmentRef'])+details['op'] + "','" + details['LogsDesc'] + "'," + "'," + str(details['by']) + ",'" + details['ip']+"'); "
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