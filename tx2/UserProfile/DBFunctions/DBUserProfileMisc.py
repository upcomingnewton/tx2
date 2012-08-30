'''
Created on 06-Aug-2012

@author: jivjot
'''
from tx2.DataBaseHelper import DBhelper
from tx2.CONFIG import LOGGER_COMMUNICATION, LoggerQuery
from tx2.CONFIG import LOGGER_USER_PROFILE

import logging
import inspect

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
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
    