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
from tx2.jobs.models import   JobType
from tx2.jobs.DBFunctions.DBJobType import DBInsertJobType, DBUpdateJobType
class JobTypeFunctions():
  def __init__(self): 
    self.JobLogger = logging.getLogger(LoggerJob)
  def Add(self,Name,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
      details = {
          'Name':Name,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBInsertJobType(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No JobType Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  def Update(self,_Id,Name,by,ip,req_op=SYSTEM_PERMISSION_UPDATE):
    try:
      _Id=int(_Id)
      obj=JobType.objects.get(id=_Id);
      prev=pickle.dumps(obj)
      prev=prev.replace("'", ">");
      prev=prev.replace("\n", "<");
      prev=prev.replace("\\", "+");
        
      details = {
          'Id':_Id,
          'Name':Name,
          'prev':prev,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBUpdateJobType(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No JobType Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  
  def getObjectbyName(self,_Name):
      try:
        JobTypeObjList =  JobType.objects.get(Name=_Name) 
        return (1,JobTypeObjList)
      except ObjectDoesNotExist:
        return (-1,'No JobType Object exists in database with this name')
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
        JobObjList =  JobType.objects.all() 
        return (1,JobObjList)
      except ObjectDoesNotExist:
        return (-1,'No JobType Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))


