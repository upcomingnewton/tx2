'''
Created on 01-Aug-2012

@author: jivjot
'''

from tx2.DataBaseHelper import DBhelper
from tx2.CONFIG import LOGGER_COMMUNICATION, LoggerQuery
from tx2.CONFIG import LOGGER_USER_PROFILE
import inspect
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
    
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)} 
                                                                   
def DBExtraAcademicInfoTypeUpdate(details):
    query = "SELECT * FROM ExtraAcademicInfoTypeUpdate(%s,'%s','%s','%s','%s','%s');"%(details["Id"],details["ExtraAcademicInfoTypeName"],details['prev'],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoTypeUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBExtraAcademicInfoTypeUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoTypeUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
    
def DBFunctionalAreaTypeInsert(details):
    query = "SELECT * FROM FunctionalAreaTypeInsert('%s','%s',%s,'%s');"%(details["FunctionalAreaTypeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertFunctionalAreaType',query))
        QueryLogger.debug('[%s] %s'%('DBInsertFunctionalAreaType',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertFunctionalAreaType',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}

def DBFunctionalAreaTypeUpdate(details):
    query = "SELECT * FROM FunctionalAreaTypeUpdate(%s,'%s','%s','%s',%s,'%s');"%(details["Id"],details["FunctionalAreaTypeName"],details["prev"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBFunctionalAreaTypeUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBFunctionalAreaTypeUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBFunctionalAreaTypeUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}

def DBExtraAcademicInfoDetailsInsert(details):
    query = "SELECT * FROM ExtraAcademicInfoDetailsInsert(%s,'%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s','%s','%s',%s,'%s');"%(details["User_id"],details["Title"],details["Start"],details["End"],details["Organisation"],details["Designation"],details["Details"],details["PlaceOfWork"],details["FunctionalArea"],details["ExtraAcadmicInfoType_id"],details["References"],details["Summary"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsInsert',query))
        QueryLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsInsert',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsInsert',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}                                                                
def DBExtraAcademicInfoDetailsUpdate(details):
    query = "SELECT * FROM ExtraAcademicInfoDetailsUpdate(%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s','%s','%s','%s',%s,'%s');"%(details["Id"],details["User_id"],details["Title"],details["Start"],details["End"],details["Organisation"],details["Designation"],details["Details"],details["PlaceOfWork"],details["FunctionalArea"],details["ExtraAcadmicInfoType_id"],details["References"],details["Summary"],details["prev"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
def DBExtraAcademicInfoDetailsDelete(details):
    query = "SELECT * FROM ExtraAcademicInfoDetailsDelete(%s,%s,'%s',%s,'%s');"%(details["Id"],details["User_id"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsDelete',query))
        QueryLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsDelete',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBExtraAcademicInfoDetailsDelete',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}

def DBFunctionalAreaListInsert(details):
    query = "SELECT * FROM FunctionalAreaListInsert(%s,'%s','%s',%s,'%s');"%(details["FunctionalAreaType_id"],details["FunctionalArea"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBFunctionalAreaListInsert',query))
        QueryLogger.debug('[%s] %s'%('DBFunctionalAreaListInsert',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBFunctionalAreaListInsert',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
def DBFunctionalAreaListUpdate(details):
    query = "SELECT * FROM FunctionalAreaListUpdate(%s,%s,'%s','%s','%s',%s,'%s');"%(details["Id"],details["FunctionalAreaType_id"],details["FunctionalArea"],details["prev"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBFunctionalAreaListUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBFunctionalAreaListUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBFunctionalAreaListUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}