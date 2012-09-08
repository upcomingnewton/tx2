'''
Created on 08-Sep-2012

@author: jivjot
'''
from tx2.CONFIG import LoggerJob
import logging
import inspect
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT
from tx2.jobs.DBFunctions.DBMessages import decode
from tx2.jobs.DBFunctions.DBCompanyInfo import DBInsertCompanyInfo
class CompanyInfoFunctions():
  def __init__(self): 
    self.JobLogger = logging.getLogger(LoggerJob)
  def Add(self,CompanyName,CompanyAdress,CompanyWebsite,CompanyAbout,CompanyOtherDetails1,CompanyOtherDetails2,User,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
      details = {
          'CompanyName':CompanyName,
          'CompanyAdress':CompanyAdress,
          'CompanyWebsite':CompanyWebsite,
          'CompanyAbout':CompanyAbout,
          'CompanyOtherDetails1':CompanyOtherDetails1,
          'CompanyOtherDetails2':CompanyOtherDetails2,
          'User':User,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBInsertCompanyInfo(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))


