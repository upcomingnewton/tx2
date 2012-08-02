'''
Created on 01-Aug-2012

@author: jivjot
'''

from tx2.DataBaseHelper import DBhelper
from tx2.CONFIG import LOGGER_COMMUNICATION, LoggerQuery
from tx2.CONFIG import LOGGER_USER_PROFILE

import logging

CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
QueryLogger = logging.getLogger(LoggerQuery)
UserProfileLogger=logging.getLogger(LOGGER_USER_PROFILE)

def DBExtraAcademicInfoTypeInsert(details):
    query = "SELECT * FROM ExtraAcademicInfoTypeInsert('%s','%s','%s','%s');"%(details["ExtraAcademicInfoTypeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertExtraAcademicInfoType',query))
        QueryLogger.debug('[%s] %s'%('DBInsertExtraAcademicInfoType',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertExtraAcademicInfoType',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBInsertExtraAcademicInfoType',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}                                                                
def DBFunctionalAreaTypeInsert(details):
    query = "SELECT * FROM FunctionalAreaTypeInsert('%s','%s','%s','%s');"%(details["FunctionalAreaTypeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertFunctionalAreaType',query))
        QueryLogger.debug('[%s] %s'%('DBInsertFunctionalAreaType',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertFunctionalAreaType',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBInsertFunctionalAreaType',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}                                                                
def DBExtraAcademicInfoDetailsInsert(details):
    query = "SELECT * FROM ExtraAcademicInfoDetailsInsert(%s,'%s','%s','%s','%s','%s','%s',%s,'%s',%s,'%s','%s','%s',%s,'%s');"%(details["User_id"],details["Title"],details["Start"],details["End"],details["Organisation"],details["Designation"],details["Details"],details["PlaceOfWork_id"],details["FunctionalArea"],details["ExtraAcadmicInfoType_id"],details["References"],details["Summary"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsInsert',query))
        QueryLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsInsert',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsInsert',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBExtraAcademicInfoDetailsInsert',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}                                                                
def DBFunctionalAreaListInsert(details):
    query = "SELECT * FROM FunctionalAreaListInsert(%s,'%s','%s',%s,'%s');"%(details["FunctionalAreaType_id"],details["FunctionalArea"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBFunctionalAreaListInsert',query))
        QueryLogger.debug('[%s] %s'%('DBFunctionalAreaListInsert',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBFunctionalAreaListInsert',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBFunctionalAreaListInsert',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}                                                                
