'''
Created on 26-Jul-2012

@author: jivjot
'''
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.DBFunctions import DBFunctions
from tx2.UserProfile.models import Marks as mymarks
import pickle
import logging
import inspect

class Marks(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.UserProfileLogger=logging.getLogger(LOGGER_USER_PROFILE)
    def MakeExceptionMessage(self,msg):
          return 'Exception Generated : ' + str(msg) + ' Administrators have been alerted to rectify the error. We will send you a notification in this regard soon.'
  
    def InsertBoard(self,BoardName,by_user,ip):
        try:
            details={'BoardName':BoardName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBBoardInsert(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
    def InsertDegreeType(self,DegreeTypeName,by_user,ip):
        try:
            details={'DegreeTypeName':DegreeTypeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBDegreeTypeInsert(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
    def InsertDegree(self,DegreeName,by_user,ip):
        try:
            details={'DegreeName':DegreeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBDegreeInsert(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
    def InsertSessionType(self,SessionTypeName,by_user,ip):
        try:
            details={'SessionTypeName':SessionTypeName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBSessionTypeInsert(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
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
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
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
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBMarksUpdate(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
    def DeleteBoard(self,BoardId,by_user,ip):
        try:
            details={'BoardId':int(BoardId),
                     'RequestedOperation':'SYS_PER_DELETE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBBoardDelete(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
    def UpdateBoard(self,BoardId,BoardName,by_user,ip):
        try:
            details={'BoardId':int(BoardId),
                     'BoardName':BoardName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBBoardUpdate(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
    def UpdateDegreeType(self,DegreeTypeId,DegreeTypeName,by_user,ip):
        try:
            details={'DegreeTypeId':DegreeTypeId,
                     'DegreeTypeName':DegreeTypeName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBDegreeTypeUpdate(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
    def UpdateDegree(self,DegreeId,DegreeName,by_user,ip):
        try:
            details={'DegreeId':DegreeId,
                     'DegreeName':DegreeName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBDegreeUpdate(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        
    def UpdateSessionType(self,SessionTypeId,SessionTypeName,by_user,ip):
        try:
            details={'SessionTypeId':SessionTypeId,
                     'SessionTypeName':SessionTypeName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBSessionTypeUpdate(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        