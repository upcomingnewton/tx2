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
from tx2.jobs.models import  Job
from tx2.Users.models import User
from tx2.jobs.DBFunctions.DBJobs import DBInsertJob, DBUpdateJob
class JobFunctions():
  def __init__(self): 
    self.JobLogger = logging.getLogger(LoggerJob)
  def Add(self,CompanyId,Profile,Designation,Package,DateOfVisit,JobDetails1,JobDetails2,RecruitmentRounds,ContactPersonName,ContactPersonMobile,ContactPersonEmail,ContactPersonDetails,RegistrationsUpto,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
      if by==-1:
        by=User.objects.get(UserEmail='SystemInit1@init.com').id
        
      details = {
          'Company':CompanyId,
          'Profile':Profile,
          'Designation':Designation,
          'Package':Package,
          'DateOfVisit':DateOfVisit,
          'JobDetails1':JobDetails1,
          'JobDetails2':JobDetails2,
          'RecruitmentRounds':RecruitmentRounds,
          'ContactPersonName':ContactPersonName,
          'ContactPersonMobile':ContactPersonMobile,
          'ContactPersonEmail':ContactPersonEmail,
          'ContactPersonDetails':ContactPersonDetails,
          'RegistrationsUpto':RegistrationsUpto,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBInsertJob(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No User Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  def Update(self,_Id,CompanyId,Profile,Designation,Package,DateOfVisit,JobDetails1,JobDetails2,RecruitmentRounds,ContactPersonName,ContactPersonMobile,ContactPersonEmail,ContactPersonDetails,RegistrationsUpto,by,ip,req_op=SYSTEM_PERMISSION_UPDATE):
    try:
      
        
      _Id=int(_Id)
      obj=Job.objects.get(id=_Id);
      prev=pickle.dumps(obj)
      prev=prev.replace("'", ">");
      prev=prev.replace("\n", "<");
      prev=prev.replace("\\", "+");
      
      details = {
          'Id':_Id,
          'Company':CompanyId,
          'Profile':Profile,
          'Designation':Designation,
          'Package':Package,
          'DateOfVisit':DateOfVisit,
          'JobDetails1':JobDetails1,
          'JobDetails2':JobDetails2,
          'RecruitmentRounds':RecruitmentRounds,
          'ContactPersonName':ContactPersonName,
          'ContactPersonMobile':ContactPersonMobile,
          'ContactPersonEmail':ContactPersonEmail,
          'ContactPersonDetails':ContactPersonDetails,
          'RegistrationsUpto':RegistrationsUpto,
          'prev':prev,
          'by':by,
          'op':req_op,
          'ip':ip,
        }
      result = DBUpdateJob(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
        return (-1,'No User Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  
  def getObjectByStateid(self,_State):
      try:
        JobObj =  Job.objects.filter(State=_State)  
        return (1,JobObj)
      except ObjectDoesNotExist:
        return (-1,'No Job Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
  def getObjectByDateofVisit(self,_DateofVisit):
      try:
        JobObj =  Job.objects.filter(DateOfVisit=_DateofVisit)  
        return (1,JobObj)
      except ObjectDoesNotExist:
        return (-1,'No Job Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
  def getObjectByRegistraionUpto(self,_RegistrationsUpto):
      try:
        JobObj =  Job.objects.filter(RegistrationsUpto=_RegistrationsUpto)  
        return (1,JobObj)
      except ObjectDoesNotExist:
        return (-1,'No Job Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
        
  def getObjectByID(self,_id):
      try:
        JobObj =  Job.objects.get(id=_id)  
        return (1,JobObj)
      except ObjectDoesNotExist:
        return (-1,'No Job Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
      
  def getObjectByCompanyId(self,_Id):
      try:
        JobObjList =  Job.objects.filter(Company=_Id)  
        return (1,JobObjList)
      except ObjectDoesNotExist:
        return (-1,'No Job Object exists in database with this name')
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
        JobObjList =  Job.objects.all() 
        return (1,JobObjList)
      except ObjectDoesNotExist:
        return (-1,'No Job Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.JobLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))


