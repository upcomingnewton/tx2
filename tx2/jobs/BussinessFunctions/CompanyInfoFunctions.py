'''
Created on 08-Sep-2012

@author: jivjot
'''
from tx2.CONFIG import LoggerJob
import logging
import inspect
import pickle
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,\
  SYSTEM_PERMISSION_UPDATE
from tx2.jobs.DBFunctions.DBMessages import decode
from tx2.jobs.DBFunctions.DBCompanyInfo import DBInsertCompanyInfo, DBUpdateCompanyInfo
from django.core.exceptions import ObjectDoesNotExist
from tx2.jobs.models import CompanyInfo
from tx2.Users.models import User
class CompanyInfoFunctions():
  def __init__(self): 
    self.JobLogger = logging.getLogger(LoggerJob)
  def Add(self,CompanyName,CompanyAdress,CompanyWebsite,CompanyAbout,CompanyOtherDetails1,CompanyOtherDetails2,Userid,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
      if by==-1:
        by=User.objects.get(UserEmail='SystemInit1@init.com').id
      if Userid==-1:
        Userid=User.objects.get(UserEmail='SystemInit1@init.com').id
        
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
    except ObjectDoesNotExist:
        return (-1,'No User Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
  def Update(self,_Id,CompanyName,CompanyAdress,CompanyWebsite,CompanyAbout,CompanyOtherDetails1,CompanyOtherDetails2,User,by,ip,req_op=SYSTEM_PERMISSION_UPDATE):
    try:
      Id=int(_Id)
      obj=CompanyInfo.objects.get(id=_Id);
      prev=pickle.dumps(obj)
      prev=prev.replace("'", ">");
      prev=prev.replace("\n", "<");
      prev=prev.replace("\\", "+");
          
      details = {
                 'Id':Id,
                 'CompanyName':CompanyName,
                 'CompanyAdress':CompanyAdress,
                 'CompanyWebsite':CompanyWebsite,
                 'CompanyAbout':CompanyAbout,
                 'CompanyOtherDetails1':CompanyOtherDetails1,
                 'CompanyOtherDetails2':CompanyOtherDetails2,
                 'User':User,
                 'prev':prev,
                 'by':by,
                 'op':req_op,
                 'ip':ip,
                 }
      result = DBUpdateCompanyInfo(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
      else:
        return (-1,decode(result))
    except ObjectDoesNotExist:
      return (-1,'No CompanyInfo Object exists in database with this name')
      
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
        self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
    
    def getObjectById(_id):
      try:
        AdressObj =  CompanyInfo.objects.get(id=_id)  
        return (1,AdressObj)
      except ObjectDoesNotExist:
        return (-1,'No CompanyInfo Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))

  def getObjectByName(self,_Name):
      try:
        CompanyInfoObj =  CompanyInfo.objects.get(CompanyName=_Name)  
        return (1,CompanyInfoObj)
      except ObjectDoesNotExist:
        return (-1,'No ComapnyInfo Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
      
  def getObjectByUserId(self,_User):
      try:
        CompanyInfoObjList =  CompanyInfo.objects.filter(User=_User)  
        return (1,CompanyInfoObjList)
      except ObjectDoesNotExist:
        return (-1,'No CompanyInfo Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))
  def getObjectsAll(self):
      try:
        CompanyInfoObjList =  CompanyInfo.objects.all() 
        return (1,CompanyInfoObjList)
      except ObjectDoesNotExist:
        return (-1,'No CompanyInfo Object exists in database with this name')
      except Exception, ex:
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        msg = ''
        for i in args:
          msg += "[%s : %s]" % (i,values[i])
          self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
        return (-2,str(ex))


