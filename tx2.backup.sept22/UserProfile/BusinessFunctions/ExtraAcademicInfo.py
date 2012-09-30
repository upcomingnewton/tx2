'''
Created on 01-Aug-2012

@author: jivjot
'''
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.DBFunctions import DBExtraAcademicInfo
from tx2.UserProfile.models import ExtraAcademicInfoType
from tx2.UserProfile.models import FunctionalAreaType
from tx2.UserProfile.models import FunctionalAreaList
from tx2.UserProfile.models import ExtraAcademicInfoDetails

import pickle
import logging
import inspect
class ExtraAcademicInfo:
  def __init__(self):
        '''
        Constructor
        '''
        self.UserProfileLogger=logging.getLogger(LOGGER_USER_PROFILE)
        def MakeExceptionMessage(self,msg):
          return 'Exception Generated : ' + str(msg) + ' Administrators have been alerted to rectify the error. We will send you a notification in this regard soon.'
  
  def InsertExtraAcademicInfoType(self,ExtraAcademicInfoTypeName,by_user,ip):
        try:
            details={'ExtraAcademicInfoTypeName':ExtraAcademicInfoTypeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBExtraAcademicInfoTypeInsert(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
  def UpdateExtraAcademicInfoType(self,_Id,ExtraAcademicInfoTypeName,by_user,ip):
        try:
            _Id=int(_Id)
            obj=ExtraAcademicInfoType.objects.get(id=_Id);
            
            
            prev=pickle.dumps(obj)
            prev=prev.replace("'", ">");
            prev=prev.replace("\n", "<");
            prev=prev.replace("\\", "+");
            
            details={'Id':_Id,
                     'ExtraAcademicInfoTypeName':ExtraAcademicInfoTypeName,
                     'prev':prev,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBExtraAcademicInfoTypeUpdate(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
  def InsertFunctionalAreaType(self,FunctionalAreaTypeName,by_user,ip):
        try:
            details={'FunctionalAreaTypeName':FunctionalAreaTypeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBFunctionalAreaTypeInsert(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
  def UpdateFunctionalAreaType(self,_Id,FunctionalAreaTypeName,by_user,ip):
        try:
          _Id=int(_Id)
          obj=FunctionalAreaType.objects.get(id=_Id);
          prev=pickle.dumps(obj)
          prev=prev.replace("'", ">");
          prev=prev.replace("\n", "<");
          prev=prev.replace("\\", "+");
          details={'Id':_Id,
                     'FunctionalAreaTypeName':FunctionalAreaTypeName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'prev':prev,
                     'by_user':by_user,
                     'ip':ip,};
          result=DBExtraAcademicInfo.DBFunctionalAreaTypeUpdate(details);
          return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
          
  
  def InsertExtraAcademicInfoDetails(self,User_id,Title,Start,End,Organisation,Designation,Details,PlaceOfWork,FunctionalArea,ExtraAcadmicInfoType_id,References,Summary,by_user,ip):
        try:
            details={'User_id':User_id,
                     'Title':Title,
                     'Start':Start,
                     'End':End,
                     'Organisation':Organisation,
                     'Designation':Designation,
                     'Details':Details,
                     'PlaceOfWork':PlaceOfWork,
                     'FunctionalArea':FunctionalArea,
                     'References':References,
                     'Summary':Summary,
                     'ExtraAcadmicInfoType_id':ExtraAcadmicInfoType_id,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBExtraAcademicInfoDetailsInsert(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
  
  def UpdateExtraAcademicInfoDetails(self,_Id,User_id,Title,Start,End,Organisation,Designation,Details,PlaceOfWork,FunctionalArea,ExtraAcadmicInfoType_id,References,Summary,by_user,ip):
        try:
            _Id=int(_Id)
            obj=ExtraAcademicInfoDetails.objects.get(id=_Id);
            prev=pickle.dumps(obj)
            prev=prev.replace("'", ">");
            prev=prev.replace("\n", "<");
            prev=prev.replace("\\", "+");
          
            details={'Id':_Id,
                     'User_id':User_id,
                     'Title':Title,
                     'Start':Start,
                     'End':End,
                     'Organisation':Organisation,
                     'Designation':Designation,
                     'Details':Details,
                     'PlaceOfWork':PlaceOfWork,
                     'FunctionalArea':FunctionalArea,
                     'References':References,
                     'Summary':Summary,
                     'ExtraAcadmicInfoType_id':ExtraAcadmicInfoType_id,
                     'prev':prev,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBExtraAcademicInfoDetailsUpdate(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
  def DeleteExtraAcademicInfoDetails(self,_Id,UserId,by_user,ip):
        try:
            _Id=int(_Id)
            
            details={'Id':_Id,
                     'User_id':UserId,
                     'RequestedOperation':'SYS_PER_DELETE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBExtraAcademicInfoDetailsDelete(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
        
  def InsertFunctionalAreaList(self,FunctionalAreaType_id,FunctionalArea,by_user,ip):
        try:
            details={'FunctionalAreaType_id':FunctionalAreaType_id,
                     'FunctionalArea':FunctionalArea,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBFunctionalAreaListInsert(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
  def UpdateFunctionalAreaList(self,_Id,FunctionalAreaType_id,FunctionalArea,by_user,ip):
        try:
          _Id=int(_Id)
          obj=FunctionalAreaList.objects.get(id=_Id);
          prev=pickle.dumps(obj)
          prev=prev.replace("'", ">");
          prev=prev.replace("\n", "<");
          prev=prev.replace("\\", "+");
          details={'Id':_Id,
           'FunctionalAreaType_id':FunctionalAreaType_id,
           'FunctionalArea':FunctionalArea,
           'RequestedOperation':'SYS_PER_UPDATE',
           'by_user':by_user,
           'prev':prev,
           'ip':ip,};
          result=DBExtraAcademicInfo.DBFunctionalAreaListUpdate(details);
          return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        