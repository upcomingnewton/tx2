'''
Created on 08-Sep-2012

@author: jivjot
'''
from tx2.DataBaseHelper import DBhelper
from tx2.CONFIG import LoggerJob, LoggerQuery
import logging
import inspect

JobLogger = logging.getLogger(LoggerJob)
QueryLogger = logging.getLogger(LoggerQuery)

### ========================================================================================================  ### 

def DBInsertBranchJob(details):
  try:
    query = "SELECT * FROM Jobs_BranchJob_Insert(%s,%s,%s,'%s','%s','%s',%s,'%s');"%(details['Branch'],details['Job'],details['JobType'],details['Comments1'],details['Comments2'],details['op'],details['by'],details['ip'])
    QueryLogger.debug('%s' % (query))
    result =  DBhelper.CallFunction(query)
    JobLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
    return result[0]
  except Exception, ex:
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    msg = ''
    for i in args:
      msg += "[%s : %s]" % (i,values[i])
      JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
    return {'result':-5,'rescode':str(ex)}
def DBUpdateBranchJob(details):
  try:
    query = "SELECT * FROM Jobs_BranchJob_Update(%s,%s,%s,%s,'%s','%s','%s','%s',%s,'%s');"%(details['Id'],details['Branch'],details['Job'],details['JobType'],details['Comments1'],details['Comments2'],details['prev'],details['op'],details['by'],details['ip'])
    QueryLogger.debug('%s' % (query))
    result =  DBhelper.CallFunction(query)
    JobLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
    return result[0]
  except Exception, ex:
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    msg = ''
    for i in args:
      msg += "[%s : %s]" % (i,values[i])
      JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
    return {'result':-5,'rescode':str(ex)}
