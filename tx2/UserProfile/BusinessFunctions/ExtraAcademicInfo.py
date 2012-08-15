'''
Created on 01-Aug-2012

@author: jivjot
'''
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.DBFunctions import DBExtraAcademicInfo
from tx2.UserProfile.models import ExtraAcademicInfoType
from tx2.UserProfile.models import FunctionalAreaType
from tx2.UserProfile.models import FunctionalAreaList
import pickle
import logging
import inspect
class ExtraAcademicInfo:
  def __init__(self):
        '''
        Constructor
        '''
        self.UserProfileLogger=logging.getLogger(LOGGER_USER_PROFILE)
  def InsertExtraAcademicInfoType(self,ExtraAcademicInfoTypeName,by_user,ip):
        try:
            details={'ExtraAcademicInfoTypeName':ExtraAcademicInfoTypeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBExtraAcademicInfoTypeInsert(details);
            return result
        except:
            error_msg = 'Error @ InsertExtraAcademicInfoType in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
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
        except:
            error_msg = 'Error @ InsertExtraAcademicInfoType in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
  
  def InsertFunctionalAreaType(self,FunctionalAreaTypeName,by_user,ip):
        try:
            details={'FunctionalAreaTypeName':FunctionalAreaTypeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBFunctionalAreaTypeInsert(details);
            return result
        except:
            error_msg = 'Error @ InsertFunctionalAreaType in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
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
          self.UserProfileLogger.exception('UpdateFunctionalAreaType : %s' % (msg))
          return (-2,self.MakeExceptionMessage(str(ex)))  
  def InsertExtraAcademicInfoDetails(self,User_id,Title,Start,End,Organisation,Designation,Details,PlaceOfWork_id,FunctionalArea,ExtraAcadmicInfoType_id,References,Summary,by_user,ip):
        try:
            details={'User_id':User_id,
                     'Title':Title,
                     'Start':Start,
                     'End':End,
                     'Organisation':Organisation,
                     'Designation':Designation,
                     'Details':Details,
                     'PlaceOfWork_id':PlaceOfWork_id,
                     'FunctionalArea':FunctionalArea,
                     'References':References,
                     'Summary':Summary,
                     'ExtraAcadmicInfoType_id':ExtraAcadmicInfoType_id,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBExtraAcademicInfoDetailsInsert(details);
            return result
        except:
            error_msg = 'Error @ InsertExtraAcademicInfoDetails in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
  def InsertFunctionalAreaList(self,FunctionalAreaType_id,FunctionalArea,by_user,ip):
        try:
            details={'FunctionalAreaType_id':FunctionalAreaType_id,
                     'FunctionalArea':FunctionalArea,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBExtraAcademicInfo.DBFunctionalAreaListInsert(details);
            return result
        except:
            error_msg = 'Error @ InsertExtraAcademicInfoDetails in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
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
          self.UserProfileLogger.exception('UpdateFunctionalAreaList : %s' % (msg))
          return (-2,self.MakeExceptionMessage(str(ex)))