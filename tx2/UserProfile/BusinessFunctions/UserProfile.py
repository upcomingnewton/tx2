'''
Created on 26-Jul-2012

@author: jivjot
'''
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.DBFunctions import DBFunctions
from tx2.Users.BusinessFunctions.GroupTypeFunctions import GroupTypeFnx
from tx2.Users.BusinessFunctions.GroupFunctions import GroupFnx
from tx2.conf.LocalProjectConfig import  SYSTEM_USERDEFINED_GROUPTYPE
from tx2.Users.BusinessFunctions.UserFunctions import UserFnx
from tx2.UserProfile.models import Branch
from tx2.UserProfile.models import Category
from tx2.UserProfile.models import StudentDetails
import logging
import pickle
import inspect

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
            if( result['result'] == 1 ):
              GroupTypeObj = GroupTypeFnx()
              GroupType = GroupTypeObj.getGroupTypeByName(SYSTEM_USERDEFINED_GROUPTYPE)
              if( GroupType[0] != -1 ):
                self.UserProfileLogger.exception('[%s]== %s,%d'%("GroupTypeObj",GroupType[1].GroupTypeName,GroupType[1].id))
                GroupFnxObj = GroupFnx()
                res = GroupFnxObj.CreateGroup("GROUP_"  + BranchName ,"GROUP_"  + BranchName,GroupType[1].id,-1,by_user,ip)
                self.UserProfileLogger.exception('[%s] == %s'%("GroupFnxObj",str(res)))
                res = GroupFnxObj.CreateGroup("GROUP_"  + BranchName + "_UN-AUTHENTICATED" ,"GROUP_"  + BranchName + "_UN-AUTHENTICATED",GroupType[1].id,-1,by_user,ip)
                self.UserProfileLogger.exception('[%s == %s'%("GroupFnxObj",str(res)))
            return result
        except Exception, ex:
            frame = inspect.currentframe()
            args, _, _, values = inspect.getargvalues(frame)
            msg = ''
            for i in args:
              msg += "[%s : %s]" % (i,values[i])
            LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
            messages.error(HttpRequest,'ERROR: ' + str(ex))
            return HttpResponseRedirect('/message/')
        
    def UpdateBranch(self,_Id,BranchName,by_user,ip):
        try:
          _Id=int(_Id)
          obj=Branch.objects.get(id=_Id);
          prev=pickle.dumps(obj)
          prev=prev.replace("'", ">");
          prev=prev.replace("\n", "<");
          prev=prev.replace("\\", "+");
          details={'Id':_Id,
                     'BranchName':BranchName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'prev':prev,
                     'by_user':by_user,
                     'ip':ip,};
          result=DBFunctions.DBBranchUpdate(details);
          if( result['result'] == 1 ):
              GroupTypeObj = GroupTypeFnx()
              GroupType = GroupTypeObj.getGroupTypeByName(SYSTEM_USERDEFINED_GROUPTYPE)
              if( GroupType[0] != -1 ):
                self.UserProfileLogger.exception('[%s]== %s,%d'%("GroupTypeObj",GroupType[1].GroupTypeName,GroupType[1].id))
                GroupFnxObj = GroupFnx()
                res = GroupFnxObj.CreateGroup("GROUP_"  + BranchName ,"GROUP_"  + BranchName,GroupType[1].id,-1,by_user,ip)
                self.UserProfileLogger.exception('[%s] == %s'%("GroupFnxObj",str(res)))
                res = GroupFnxObj.CreateGroup("GROUP_"  + BranchName + "_UN-AUTHENTICATED" ,"GROUP_"  + BranchName + "_UN-AUTHENTICATED",GroupType[1].id,-1,by_user,ip)
                self.UserProfileLogger.exception('[%s == %s'%("GroupFnxObj",str(res)))
          return result
        except Exception, ex:
            frame = inspect.currentframe()
            args, _, _, values = inspect.getargvalues(frame)
            msg = ''
            for i in args:
              msg += "[%s : %s]" % (i,values[i])
            LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
            messages.error(HttpRequest,'ERROR: ' + str(ex))
            return HttpResponseRedirect('/message/')
        
    def InsertCategory(self,CategoryName,by_user,ip):
        try:
            details={'CategoryName':CategoryName,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBFunctions.DBCategoryInsert(details);
            return result
        except Exception, ex:
            frame = inspect.currentframe()
            args, _, _, values = inspect.getargvalues(frame)
            msg = ''
            for i in args:
              msg += "[%s : %s]" % (i,values[i])
            LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
            messages.error(HttpRequest,'ERROR: ' + str(ex))
            return HttpResponseRedirect('/message/')
        
    def UpdateCategory(self,_Id,CategoryName,by_user,ip):
        try:
          _Id=int(_Id)
          obj=Category.objects.get(id=_Id);
          prev=pickle.dumps(obj)
          prev=prev.replace("'", ">");
          prev=prev.replace("\n", "<");
          prev=prev.replace("\\", "+");
          details={'Id':_Id,
                     'CategoryName':CategoryName,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'prev':prev,
                     'by_user':by_user,
                     'ip':ip,};
          result=DBFunctions.DBCategoryUpdate(details);
          return result
        except Exception, ex:
            frame = inspect.currentframe()
            args, _, _, values = inspect.getargvalues(frame)
            msg = ''
            for i in args:
              msg += "[%s : %s]" % (i,values[i])
            LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
            messages.error(HttpRequest,'ERROR: ' + str(ex))
            return HttpResponseRedirect('/message/')
        
    def InsertStudentDetails(self,UserId,RollNo,BranchMajor,BranchMinor,Degree,CategoryId,ComputerProficiency,aieee,by_user,ip, Group):
        try:
          details={'UserId':UserId,
                     'RollNo':RollNo,
                     'BranchMajor':BranchMajor,
                     'BranchMinor':BranchMinor,
                     'Degree':Degree,
                     'CategoryId':CategoryId,
                     'ComputerProficiency':ComputerProficiency,
                     'aieee':aieee,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
          result=DBFunctions.DBStudentDetailsInsert(details);
          if( result['result'] == 1 ):
              UserFnxObj = UserFnx()
              res = UserFnxObj.ChangeUserGroup(UserId,Group,by_user,ip)
              self.UserProfileLogger.debug('[%s][%d] == %s =='%("ChangeUserGroup",UserId,str(res)))
              return (result,"Your basic profile necessary for authentication has been sucessfully updated. We will update through email as soon as it is activated by your respective branch admin")
          elif result['result'] == 2:
              UserFnxObj = UserFnx()
              res = UserFnxObj.ChangeUserGroup(UserId,Group,by_user,ip)
              self.UserProfileLogger.exception('[%s][%d] == %s =='%("ChangeUserGroup",UserId,str(res)))
              return (result,"Your basic profile necessary has already been created.")
          else:
                self.UserProfileLogger.debug('[%s] == Exception %s, %d=='%("InsertStudentDetails",str(result),UserId))
                return (-1,"Some error has occured. Please try again")
        except Exception, ex:
            frame = inspect.currentframe()
            args, _, _, values = inspect.getargvalues(frame)
            msg = ''
            for i in args:
              msg += "[%s : %s]" % (i,values[i])
            LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
            messages.error(HttpRequest,'ERROR: ' + str(ex))
            return HttpResponseRedirect('/message/')
        
    def UpdateStudentDetails(self,_Id,UserId,RollNo,BranchMajor,BranchMinor,Degree,CategoryId,ComputerProficiency,aieee,by_user,ip,Group):
        try:
          _Id=int(_Id)
          obj=StudentDetails.objects.get(id=_Id);
          prev=pickle.dumps(obj)
          prev=prev.replace("'", ">");
          prev=prev.replace("\n", "<");
          prev=prev.replace("\\", "+");
          details={'Id':_Id,
                     'UserId':UserId,
                     'RollNo':RollNo,
                     'BranchMajor':BranchMajor,
                     'BranchMinor':BranchMinor,
                     'Degree':Degree,
                     'CategoryId':CategoryId,
                     'ComputerProficiency':ComputerProficiency,
                     'aieee':aieee,
                     'prev':prev,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
          result=DBFunctions.DBStudentDetailsUpdate(details);
          if( result['result'] == 1 ):
              UserFnxObj = UserFnx()
              res = UserFnxObj.ChangeUserGroup(UserId,Group,by_user,ip)
              self.UserProfileLogger.debug('[%s][%d] == %s =='%("ChangeUserGroup",UserId,str(res)))
              return (result,"Your basic profile necessary has been sucessfully updated. ")
          else:
                self.UserProfileLogger.debug('[%s] == Exception %s, %d=='%("InsertStudentDetails",str(result),UserId))
                return (-1,"Some error has occured. Please try again")
        except Exception, ex:
            frame = inspect.currentframe()
            args, _, _, values = inspect.getargvalues(frame)
            msg = ''
            for i in args:
              msg += "[%s : %s]" % (i,values[i])
            LogUser.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
            messages.error(HttpRequest,'ERROR: ' + str(ex))
            return HttpResponseRedirect('/message/')
        
