'''
Created on 26-Jul-2012

@author: jivjot
'''
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.DBFunctions import DBFunctions
from tx2.UserProfile.models import Marks as mymarks
from StringIO import StringIO
import pickle
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
    def InsertSessionType(self,SessionTypeName,by_user,ip):
        try:
            details={'SessionTypeName':SessionTypeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBSessionTypeInsert(details);
            return result
        except Exception as inst:
            error_msg = 'Error @ InsertSessionTypeName in Business Functions %s'%(inst)
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    def InsertMarks(self,SessionStart,SessionEnd,SessionNumber,SessionType,TotalMarks,SecuredMarks,TotalReappears,ReappearsRemaining,DegreeType,Board,Degree,UserId,by_user,ip):
        try:
            details={'SessionStart':SessionStart,
                     'SessionEnd':SessionEnd,
                     'SessionNumber':SessionNumber,
                     'SessionType':SessionType,
                     'TotalMarks':TotalMarks,
                     'SecuredMarks':SecuredMarks,
                     'TotalReappears':TotalReappears,
                     'ReappearsRemaining':ReappearsRemaining,
                     'DegreeType':DegreeType,
                     'Board':Board,
                     'Degree':Degree,
                     'UserId':UserId,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBMarksInsert(details);
            return result
        except Exception as inst:
            error_msg = 'Error @ InsertMarks in Business Functions %s'%(inst)
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    def UpdateMarks(self,_Id,SessionStart,SessionEnd,SessionNumber,SessionType,TotalMarks,SecuredMarks,TotalReappears,ReappearsRemaining,DegreeType,Board,Degree,UserId,by_user,ip):
        try:
            _Id=int(_Id)
            obj=mymarks.objects.get(id=_Id);
            
            
            prev=pickle.dumps(obj)
            prev=prev.replace("'", ">");
            prev=prev.replace("\n", "<");
            prev=prev.replace("\\", "+");
            
            #prev=''
            details={'Id':_Id,
                     'SessionStart':SessionStart,
                     'SessionEnd':SessionEnd,
                     'SessionNumber':SessionNumber,
                     'SessionType':SessionType,
                     'TotalMarks':TotalMarks,
                     'SecuredMarks':SecuredMarks,
                     'TotalReappears':TotalReappears,
                     'ReappearsRemaining':ReappearsRemaining,
                     'DegreeType':DegreeType,
                     'Board':Board,
                     'Degree':Degree,
                     'prev':prev,
                     'UserId':UserId,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBMarksUpdate(details);
            return result
        except Exception as inst:
            error_msg = 'Error @ InsertMarks in Business Functions %s'%(inst)
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
    def UpdateDegreeType(self,DegreeTypeId,DegreeTypeName,by_user,ip):
        try:
            details={'DegreeTypeId':DegreeTypeId,
                     'DegreeTypeName':DegreeTypeName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBDegreeTypeUpdate(details);
            return result
        except:
            error_msg = 'Error @ UpdateDegreeType in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    
    def UpdateDegree(self,DegreeId,DegreeName,by_user,ip):
        try:
            details={'DegreeId':DegreeId,
                     'DegreeName':DegreeName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBDegreeUpdate(details);
            return result
        except:
            error_msg = 'Error @ UpdateDegree in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    
    def UpdateSessionType(self,SessionTypeId,SessionTypeName,by_user,ip):
        try:
            details={'SessionTypeId':SessionTypeId,
                     'SessionTypeName':SessionTypeName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBSessionTypeUpdate(details);
            return result
        except:
            error_msg = 'Error @ UpdateSessionType in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}