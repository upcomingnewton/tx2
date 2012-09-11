'''
Created on 09-Sep-2012

@author: jivjot
'''
from tx2.CONFIG import LoggerJob
import logging
import inspect
import pickle
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_UPDATE
from tx2.jobs.DBFunctions.DBMessages import decode
from django.core.exceptions import ObjectDoesNotExist
from tx2.jobs.models import StudentJob
from tx2.jobs.DBFunctions.DBStudentJobs import DBInsertStudentJob,\
  DBUpdateStudentJob
class StudentJobFunctions():
  def __init__(self): 
    self.JobLogger = logging.getLogger(LoggerJob)
  def Add(self,Userid,JobBranch,Status,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
        
      details = {
          'User':Userid,
          'Status':Status,
          'JobBranch':JobBranch,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBInsertStudentJob(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No StudentJob Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  def Update(self,_Id,Userid,JobBranch,Status,by,ip,req_op=SYSTEM_PERMISSION_UPDATE):
    try:
        
      _Id=int(_Id)
      obj=StudentJob.objects.get(id=_Id);
      prev=pickle.dumps(obj)
      prev=prev.replace("'", ">");
      prev=prev.replace("\n", "<");
      prev=prev.replace("\\", "+");
      
      details = {
          'Id':_Id,
          'User':Userid,
          'Status':Status,
          'JobBranch':JobBranch,
          'prev':prev,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBUpdateStudentJob(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No StudentJob Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  

  def getObjectsbyUser(self,Userid):
      try:
        StudentJobList =  StudentJob.objects.filter(User=Userid) 
        return (1,StudentJobList)
      except ObjectDoesNotExist:
        return (-1,'No StudentJob Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))




