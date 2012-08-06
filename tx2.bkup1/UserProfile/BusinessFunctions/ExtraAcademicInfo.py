'''
Created on 01-Aug-2012

@author: jivjot
'''
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.DBFunctions import DBExtraAcademicInfo
import logging

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
  def InsertFunctionalAreaListInsert(self,FunctionalAreaType_id,FunctionalArea,by_user,ip):
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
  