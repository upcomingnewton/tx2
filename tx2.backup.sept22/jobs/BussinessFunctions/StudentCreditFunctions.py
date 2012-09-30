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
from tx2.jobs.models import StudentsCredit
from tx2.jobs.DBFunctions.DBStudentCredit import DBInsertStudentCredit,\
  DBUpdateStudentCredit
class StudentCreditFunctions():
  def __init__(self): 
    self.JobLogger = logging.getLogger(LoggerJob)
  def Add(self,Userid,JobType,Credit,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
        
      details = {
          'User':Userid,
          'Credit':Credit,
          'JobType':JobType,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBInsertStudentCredit(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No StudentCredit Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  def Update(self,_Id,Userid,JobType,Credit,by,ip,req_op=SYSTEM_PERMISSION_UPDATE):
    try:
        
      _Id=int(_Id)
      obj=StudentsCredit.objects.get(id=_Id);
      prev=pickle.dumps(obj)
      prev=prev.replace("'", ">");
      prev=prev.replace("\n", "<");
      prev=prev.replace("\\", "+");
      
      details = {
          'Id':_Id,
          'User':Userid,
          'Credit':Credit,
          'JobType':JobType,
          'prev':prev,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBUpdateStudentCredit(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No StudentCredit Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  
  
  def getObjectsbyJobType(self,JobTypeid):
      try:
        StudentCreditList =  StudentsCredit.objects.filter(JobType=JobTypeid) 
        return (1,StudentCreditList)
      except ObjectDoesNotExist:
        return (-1,'No StudentCredit Object exists in database with this name')
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
        StudentCreditList =  StudentsCredit.objects.filter(User=Userid) 
        return (1,StudentCreditList)
      except ObjectDoesNotExist:
        return (-1,'No StudentCredit Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
  def getObjectsbyCredit(self,_Credit):
      try:
        StudentCreditList =  StudentsCredit.objects.filter(Credit=_Credit) 
        return (1,StudentCreditList)
      except ObjectDoesNotExist:
        return (-1,'No StudentCredit Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
      
  def getObjectsAll(self):
      try:
        StudentCreditList =  StudentsCredit.objects.all() 
        return (1,StudentCreditList)
      except ObjectDoesNotExist:
        return (-1,'No StudentCredit Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))


