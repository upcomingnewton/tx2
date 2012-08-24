'''
Created on Mar 3, 2012

@author: nitin
'''
from tx2.DataBaseHelper import DBhelper
from tx2.CONFIG import LOGGER_UserReg, LoggerQuery
import logging
import inspect

RegLogger = logging.getLogger(LOGGER_UserReg)
QueryLogger = logging.getLogger(LoggerQuery)

#
### ========================================================================================================  ### 


def DBRegUserInsert(details):
  try:
	#SELECT * FROM  UserRegInsert('MetaInfo','_Desc','Users','Groups','ReferenceToRegisterUser',1,1,'SYS_PER_INSERT',1,'ip');
        query = "SELECT * FROM UserRegInsert('" + details['MetaInfo'] + "','" + details['Desc'] + "','" + details['Users'] +"',"+ str(details['Record']) + ",'" + details['Groups'] + "','" + details['ReferenceToRegisterUser'] + "',"+ str(details['ContentType']) +",'" + details['Operation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        QueryLogger.debug(query)
        result =  DBhelper.CallFunction(query)
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      RegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
def DBRegUserUpdate(details):
  try:
	#SELECT * FROM  UserRegUpdate('MetaInfo-updated','_Desc-updated','Users-updated',1,1,'SYS_PER_UPDATE','update test from db',1,'testfromdb');
        query = "SELECT * FROM UserRegUpdate('" + details['MetaInfo'] + "','" + details['Desc'] + "','" + details['Users'] +"','" + details['Groups'] + "','" + details['ReferenceToRegisterUser'] + "',"+ str(details['Record']) + ","+ str(details['ContentType']) +",'" + details['Operation'] + "','" + details['LogsDesc'] +"'," + str(details['by']) + ",'" + details['ip'] + "');"
        QueryLogger.debug(query)
        result =  DBhelper.CallFunction(query)
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      RegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}



