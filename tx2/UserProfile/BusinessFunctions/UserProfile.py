'''
Created on 26-Jul-2012

@author: jivjot
'''
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.DBFunctions import DBFunctions
import logging


class UserProfile(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.UserProfileLogger=logging.getLogger(LOGGER_USER_PROFILE)
    def InsertBranch(self,BranchName,by_user,ip):
        try:
            details={'BranchName':BranchName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBBranchInsert(details);
            return result
        except:
            error_msg = 'Error @ InsertBoard in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    def InsertCategory(self,CategoryName,by_user,ip):
        try:
            details={'CategoryName':CategoryName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBCategoryInsert(details);
            return result
        except:
            error_msg = 'Error @ InsertCategory in Business Functions'
            self.UserProfileLogger.exception('[%s] == Exception =='%('AddComment'))
            return {'result':-5,'error_msg':error_msg}
    def InsertStudentDetails(self,UserId,RollNo,BranchMajor,BranchMinor,Degree,CategoryId,ComputerProficiency,by_user,ip):
        try:
            details={'UserId':UserId,
                     'RollNo':RollNo,
                     'BranchMajor':BranchMajor,
                     'BranchMinor':BranchMinor,
                     'Degree':Degree,
                     'CategoryId':CategoryId,
                     'ComputerProficiency':ComputerProficiency,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBStudentDetailsInsert(details);
            if( result['result'] == 1 ):
                return (result,"Your basic profile necessary for authentication has been sucessfully updated. We will update through email as soon as it is activated by your respective branch admin")
            else:
                return (-1,"Some error has occured. Please try again")
        except Exception as inst:
            error_msg = 'Error @ InsertStudentDetails in Business Functions %s'%(inst)
            self.UserProfileLogger.exception('[%s] == Exception =='%(inst))
            return {'result':-5,'error_msg':error_msg}
    
