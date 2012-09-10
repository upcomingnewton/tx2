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
from tx2.jobs.models import BranchJob
from tx2.jobs.DBFunctions.DBBranchJob import DBInsertBranchJob,\
  DBUpdateBranchJob
class BranchJobFunctions():
  def __init__(self): 
    self.JobLogger = logging.getLogger(LoggerJob)
  def Add(self,Branch,Job,JobType,Comments1,Comments2,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
        
      details = {
          'Branch':Branch,
          'Job':Job,
          'JobType':JobType,
          'Comments1':Comments1,
          'Comments2':Comments2,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBInsertBranchJob(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  def Update(self,_Id,Branch,Job,JobType,Comments1,Comments2,by,ip,req_op=SYSTEM_PERMISSION_UPDATE):
    try:
      _Id=int(_Id)
      obj=BranchJob.objects.get(id=_Id);
      prev=pickle.dumps(obj)
      prev=prev.replace("'", ">");
      prev=prev.replace("\n", "<");
      prev=prev.replace("\\", "+");
        
      details = {
          'Id':_Id,
          'Branch':Branch,
          'Job':Job,
          'JobType':JobType,
          'Comments1':Comments1,
          'Comments2':Comments2,
          'prev':prev,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBUpdateBranchJob(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  
  def getObjectsbyBranch(self,Branchid):
      try:
        BranchJobList =  BranchJob.objects.filter(Branch=Branchid) 
        return (1,BranchJobList)
      except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))

  def getObjectsbyJob(self,Jobid):
      try:
        BranchJobList =  BranchJob.objects.filter(Job=Jobid) 
        return (1,BranchJobList)
      except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
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
        BranchJobList =  BranchJob.objects.filter(JobType=JobTypeid) 
        return (1,BranchJobList)
      except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
  def getObjectsbyState(self,Stateid):
      try:
        BranchJobList =  BranchJob.objects.filter(State=Stateid) 
        return (1,BranchJobList)
      except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
  def getObjectsbyBranchandJob(self,branchid,Jobid):
      try:
        BranchJobList =  BranchJob.objects.filter(Branch=branchid,Job=Jobid) 
        return (1,BranchJobList)
      except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
  def getObjectsbyBranchandJobType(self,branchid,Jobtypeid):
      try:
        BranchJobList =  BranchJob.objects.filter(Branch=branchid,JobType=Jobtypeid) 
        return (1,BranchJobList)
      except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
  def getObjectsbyJobandJobType(self,Jobid,Jobtypeid):
      try:
        BranchJobList =  BranchJob.objects.filter(Job=Jobid,JobType=Jobtypeid) 
        return (1,BranchJobList)
      except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
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
        BranchJobList =  BranchJob.objects.all() 
        return (1,BranchJobList)
      except ObjectDoesNotExist:
        return (-1,'No BranchJob Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))


