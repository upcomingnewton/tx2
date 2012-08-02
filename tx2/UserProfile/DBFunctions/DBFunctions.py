
from tx2.DataBaseHelper import DBhelper
from datetime import datetime
from tx2.CONFIG import LOGGER_COMMUNICATION, LoggerQuery
from tx2.CONFIG import LOGGER_USER_PROFILE
import logging

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
    except:
        exception_log = "[%s] %s"%('DBInsertBoard',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
def DBDegreeTypeInsert(details):
    query = "SELECT * FROM DegreeTypeInsert('%s','%s','%s','%s');"%(details["DegreeTypeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertDegreeType',query))
        QueryLogger.debug('[%s] %s'%('DBInsertDegreeType',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertDegreeType',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertDegreeType',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
def DBDegreeInsert(details):
    query = "SELECT * FROM DegreeInsert('%s','%s','%s','%s');"%(details["DegreeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertDegree',query))
        QueryLogger.debug('[%s] %s'%('DBInsertDegree',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertDegree',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertDegree',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
def DBSessionTypeInsert(details):
    query = "SELECT * FROM SessionTypeInsert('%s','%s','%s','%s');"%(details["SessionTypeName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertSessionType',query))
        QueryLogger.debug('[%s] %s'%('DBInsertSessionType',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertSessionType',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertSessionType',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
def DBMarksInsert(details):
    query = "SELECT * FROM MarksInsert('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s',%s,'%s');"%(details["SessionStart"],details["SessionEnd"],details["SessionNumber"],details["SessionType"],details["TotalMarks"],details["SecuredMarks"],details["TotalReappears"],details["ReappearsRemaining"],details["DegreeType"],details["Board"],details["UserId"],details["UserId"],details["RequestedOperation"],details["by_user"],details["ip"]);
        
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertMarks',query))
        QueryLogger.debug('[%s] %s'%('DBInsertMarks',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertMarks',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBInsertMarks',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}

def DBBranchInsert(details):
    query = "SELECT * FROM BranchInsert('%s','%s','%s','%s');"%(details["BranchName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertBranch',query))
        QueryLogger.debug('[%s] %s'%('DBInsertBranch',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertBoard',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBInsertBranch',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}

def DBCategoryInsert(details):
    query = "SELECT * FROM CategoryInsert('%s','%s','%s','%s');"%(details["CategoryName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertCategory',query))
        QueryLogger.debug('[%s] %s'%('DBInsertCategory',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertCategory',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBInsertCategory',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}                                                                


def DBStudentDetailsInsert(details):
    try:
        query = "SELECT * FROM StudentDetailsInsert(%s,'%s',%s,%s,%s,%s,'%s','%s',%s,'%s');"%(details["UserId"],details["RollNo"],details["BranchMajor"],details["BranchMinor"],details["Degree"],details["CategoryId"],details["ComputerProficiency"],details["RequestedOperation"],details["by_user"],details["ip"]);
        UserProfileLogger.debug('[%s] %s'%('DBInsertStudentDetails',query))
        QueryLogger.debug('[%s] %s'%('DBInsertStudentDetails',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBInsertStudentDetails',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBInsertStudentDetails',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}                                                                

def DBBoardDelete(details):
    query = "SELECT * FROM BoardDelete(%d,'%s','%s','%s');"%(details["BoardId"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBInsertDelete',query))
        QueryLogger.debug('[%s] %s'%('DBInsertDelete',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBDeleteBoard',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBDeleteBoard',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}
    
def DBBoardUpdate(details):
    query = "SELECT * FROM BoardUpdate(%d,'%s','%s','%s','%s');"%(details["BoardId"],details["BoardName"],details["RequestedOperation"],details["by_user"],details["ip"]);
    try:
        UserProfileLogger.debug('[%s] %s'%('DBUpdateBoard',query))
        QueryLogger.debug('[%s] %s'%('DBUpdateBoard',query))
        result =  DBhelper.CallFunction(query)
        UserProfileLogger.debug('[%s] %s'%('DBUpdateBoard',result))
        return result[0]
    except Exception as inst:
        exception_log = "[%s] %s"%('DBUpdateBoard',query)
        UserProfileLogger.exception(exception_log)
        return {'result':-1,'rescode':-1,'exception':inst}


if __name__=='__main__':
    details = {
                    'BoardName':'a',
                    'RequestedOperation':'SYS_PER_INSERT',
                    'by_user':1,
                    'ip':'12',
                }
    print DBBoardInsert(details); 