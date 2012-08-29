
from tx2.DataBaseHelper import DBhelper
from datetime import datetime
from tx2.CONFIG import LOGGER_COMMUNICATION, LoggerQuery
from tx2.CONFIG import LOGGER_USER_PROFILE
import logging
import inspect
CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
QueryLogger = logging.getLogger(LoggerQuery)
UserProfileLogger=logging.getLogger(LOGGER_USER_PROFILE)
# USER SYSTEM
### ========================================================================================================  ### 


def DBBoardInsert(details):
    query = "SELECT * FROM BoardInsert('%s','%s','%s','%s');"%(details["BoardName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertBoard',query))
        QueryLogger.debug('[%s] %s'%('DBInsertBoard',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertBoard',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
def DBDegreeTypeInsert(details):
    query = "SELECT * FROM DegreeTypeInsert('%s','%s','%s','%s');"%(details["DegreeTypeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertDegreeType',query))
        QueryLogger.debug('[%s] %s'%('DBInsertDegreeType',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertDegreeType',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
def DBDegreeInsert(details):
    query = "SELECT * FROM DegreeInsert('%s','%s','%s','%s');"%(details["DegreeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertDegree',query))
        QueryLogger.debug('[%s] %s'%('DBInsertDegree',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertDegree',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
def DBSessionTypeInsert(details):
    query = "SELECT * FROM SessionTypeInsert('%s','%s','%s','%s');"%(details["SessionTypeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertSessionType',query))
        QueryLogger.debug('[%s] %s'%('DBInsertSessionType',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertSessionType',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
def DBMarksInsert(details):
    query = "SELECT * FROM MarksInsert('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s',%s,'%s');"%(details["SessionStart"],details["SessionEnd"],details["SessionNumber"],details["SessionType"],details["TotalMarks"],details["SecuredMarks"],details["TotalReappears"],details["ReappearsRemaining"],details["DegreeType"],details["Board"],details["Degree"],details["UserId"],details["RequestedOperation"],details["by_user"],details["ip"]);
        
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertMarks',query))
        QueryLogger.debug('[%s] %s'%('DBInsertMarks',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertMarks',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}

def DBBranchInsert(details):
    query = "SELECT * FROM BranchInsert('%s','%s',%s,'%s');"%(details["BranchName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertBranch',query))
        QueryLogger.debug('[%s] %s'%('DBInsertBranch',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertBoard',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}

def DBBranchUpdate(details):
    query = "SELECT * FROM BranchUpdate(%s,'%s','%s','%s',%s,'%s');"%(details['Id'],details["BranchName"],details['prev'],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBBranchUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBBranchUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBBranchUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}

def DBCategoryInsert(details):
    query = "SELECT * FROM CategoryInsert('%s','%s',%s,'%s');"%(details["CategoryName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertCategory',query))
        QueryLogger.debug('[%s] %s'%('DBInsertCategory',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertCategory',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}                                                           

def DBCategoryUpdate(details):
    query = "SELECT * FROM CategoryUpdate(%s,'%s','%s','%s',%s,'%s');"%(details['Id'],details["CategoryName"],details['prev'],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBCategoryUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBCategoryUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBCategoryUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}                                                       

def DBStudentDetailsInsert(details):
    try:
        query = "SELECT * FROM StudentDetailsInsert(%s,'%s',%s,%s,%s,%s,'%s','%s','%s',%s,'%s');"%(details["UserId"],details["RollNo"],details["BranchMajor"],details["BranchMinor"],details["Degree"],details["CategoryId"],details["ComputerProficiency"],details['aieee'],details["RequestedOperation"],details["by_user"],details["ip"]);
        UserProfileLogger.debug('[%s] %s'%('DBInsertStudentDetails',query))
        QueryLogger.debug('[%s] %s'%('DBInsertStudentDetails',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertStudentDetails',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}                                                           

def DBStudentDetailsUpdate(details):
    try:
        query = "SELECT * FROM StudentDetailsUpdate(%s,%s,'%s',%s,%s,%s,%s,'%s','%s','%s',%s,'%s');"%(details['Id'],details["UserId"],details["RollNo"],details["BranchMajor"],details["BranchMinor"],details["Degree"],details["CategoryId"],details["ComputerProficiency"],details['prev'],details["RequestedOperation"],details["by_user"],details["ip"]);
        UserProfileLogger.debug('[%s] %s'%('DBStudentDetailsUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBStudentDetailsUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBStudentDetailsUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}                                                                

def DBBoardDelete(details):
    query = "SELECT * FROM BoardDelete(%d,'%s','%s','%s');"%(details["BoardId"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertDelete',query))
        QueryLogger.debug('[%s] %s'%('DBInsertDelete',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBDeleteBoard',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
    
def DBBoardUpdate(details):
    query = "SELECT * FROM BoardUpdate(%d,'%s','%s','%s','%s');"%(details["BoardId"],details["BoardName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBUpdateBoard',query))
        QueryLogger.debug('[%s] %s'%('DBUpdateBoard',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBUpdateBoard',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
    
def DBDegreeTypeUpdate(details):
    query = "SELECT * FROM DegreeTypeUpdate(%s,'%s','%s',%s,'%s');"%(details["DegreeTypeId"],details["DegreeTypeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBDegreeTypeUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBDegreeTypeUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBDegreeTypeUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}

def DBDegreeUpdate(details):
    query = "SELECT * FROM DegreeUpdate(%s,'%s','%s',%s,'%s');"%(details["DegreeId"],details["DegreeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBDegreeUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBDegreeUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBDegreeUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
    
def DBSessionTypeUpdate(details):
    query = "SELECT * FROM SessionTypeUpdate(%s,'%s','%s',%s,'%s');"%(details["SessionTypeId"],details["SessionTypeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBSessionTypeUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBSessionTypeUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBSessionTypeUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}

def DBMarksUpdate(details):
    query = "SELECT * FROM MarksUpdate(%s,'%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s','%s',%s,'%s');"%(details["Id"],details["SessionStart"],details["SessionEnd"],details["SessionNumber"],details["SessionType"],details["TotalMarks"],details["SecuredMarks"],details["TotalReappears"],details["ReappearsRemaining"],details["DegreeType"],details["Board"],details["Degree"],details["UserId"],details['prev'],details["RequestedOperation"],details["by_user"],details["ip"]);
        
    try:
        UserProfileLogger.debug('[%s] %s'%('DBMarksUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBMarksUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBMarksUpdate',result))
        return result[0]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}


if __name__=='__main__':
    details = {
                    'BoardName':'a',
                    'RequestedOperation':'SYS_PER_INSERT',
                    'by_user':1,
                    'ip':'12',
                }
    print DBBoardInsert(details); 