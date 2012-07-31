'''
Created on 26-Jul-2012

@author: jivjot
'''
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.DBFunctions import DBFunctions
import logging


class Marks(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.UserProfileLogger=logging.getLogger(LOGGER_USER_PROFILE)
    def InsertBoard(self,BoardName,by_user,ip):
        try:
            details={'BoardName':BoardName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBBoardInsert(details);
            return result
        except:
            error_msg = 'Error @ InsertBoard in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    def InsertDegreeType(self,DegreeTypeName,by_user,ip):
        try:
            details={'DegreeTypeName':DegreeTypeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBDegreeTypeInsert(details);
            return result
        except Exception as inst:
            error_msg = 'Error @ InsertDegreeTypeName in Business Functions %s'%(inst)
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    def InsertDegree(self,DegreeName,by_user,ip):
        try:
            details={'DegreeName':DegreeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBDegreeInsert(details);
            return result
        except Exception as inst:
            error_msg = 'Error @ InsertDegreeName in Business Functions %s'%(inst)
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    
    def DeleteBoard(self,BoardId,by_user,ip):
        try:
            details={'BoardId':int(BoardId),
                     'RequestedOperation':'SYS_PER_DELETE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBBoardDelete(details);
            return result
        except:
            error_msg = 'Error @ DeleteBoard in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    def UpdateBoard(self,BoardId,BoardName,by_user,ip):
        try:
            details={'BoardId':int(BoardId),
                     'BoardName':BoardName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBBoardUpdate(details);
            return result
        except:
            error_msg = 'Error @ InsertBoard in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}