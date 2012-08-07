'''
Created on 06-Aug-2012

@author: jivjot
'''
from tx2.DataBaseHelper import DBhelper
from tx2.CONFIG import LOGGER_COMMUNICATION, LoggerQuery
from tx2.CONFIG import LOGGER_USER_PROFILE

import logging

CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
QueryLogger = logging.getLogger(LoggerQuery)
UserProfileLogger=logging.getLogger(LOGGER_USER_PROFILE)

def DBMedicalInfoInsert(details):
    query = "SELECT * FROM MedicalInfoInsert(%s,'%s','%s','%s','%s','%s','%s',%s,'%s');"%(details["User_id"],details["Height"],details["Weight"],details["LeftEye"],details["RightEye"],details['DisabilityInfo'],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBMedicalInfoInsert',query))
        QueryLogger.debug('[%s] %s'%('DBMedicalInfoInsert',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBMedicalInfoInsert',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBMedicalInfoInsert',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}