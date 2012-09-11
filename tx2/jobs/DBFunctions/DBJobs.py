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

def DBInsertJob(details):
  try:
    query = "SELECT * FROM Jobs_Job_Insert(%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s');"%(details['Company'],details['Profile'],details['Designation'],details['Package'],details['DateOfVisit'],details['JobDetails1'],details['JobDetails2'],details['RecruitmentRounds'],details['ContactPersonName'],details['ContactPersonMobile'],details['ContactPersonEmail'],details['ContactPersonDetails'],details['RegistrationsUpto'],details['op'],details['by'],details['ip'])
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
def DBUpdateJob(details):
  try:
    query = "SELECT * FROM Jobs_Job_Update(%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s');"%(details['Id'],details['Company'],details['Profile'],details['Designation'],details['Package'],details['DateOfVisit'],details['JobDetails1'],details['JobDetails2'],details['RecruitmentRounds'],details['ContactPersonName'],details['ContactPersonMobile'],details['ContactPersonEmail'],details['ContactPersonDetails'],details['RegistrationsUpto'],details['prev'],details['op'],details['by'],details['ip'])
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
