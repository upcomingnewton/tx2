'''
Created on 06-Aug-2012

@author: jivjot
'''
from tx2.CONFIG import LOGGER_USER_PROFILE
from tx2.UserProfile.DBFunctions import DBUserProfileMisc
import logging
import inspect
import pickle
from tx2.UserProfile.models import MedicalInfo
class UserProfileMisc:
  def __init__(self):
        '''
        Constructor
        '''
        self.UserProfileLogger=logging.getLogger(LOGGER_USER_PROFILE)
  def InsertMedicalInfo(self,User_id,Height,Weight,LeftEye,RightEye,DisabilityInfo,by_user,ip):
        try:
            details={'User_id':User_id,
                     'Height':Height,
                     'Weight':Weight,
                     'LeftEye':LeftEye,
                     'RightEye':RightEye,
                     'DisabilityInfo':DisabilityInfo,
                     'RequestedOperation':'SYS_PER_INSERT',
                     'by_user':by_user,
                     'ip':ip,};
            result=DBUserProfileMisc.DBMedicalInfoInsert(details);
            return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
  def UpdateMedicalInfo(self,Id,User_id,Height,Weight,LeftEye,RightEye,DisabilityInfo,by_user,ip):
        try:
          _Id=int(Id)
          obj=MedicalInfo.objects.get(id=Id);
          prev=pickle.dumps(obj)
          prev=prev.replace("'", ">");
          prev=prev.replace("\n", "<");
          prev=prev.replace("\\", "+");
          details={'Id':Id,
                     'User_id':User_id,
                     'Height':Height,
                     'Weight':Weight,
                     'LeftEye':LeftEye,
                     'RightEye':RightEye,
                     'DisabilityInfo':DisabilityInfo,
                     'prev':prev,
                     'RequestedOperation':'SYS_PER_UPDATE',
                     'by_user':by_user,
                     'ip':ip,};
          result=DBUserProfileMisc.DBMedicalInfoUpdate(details);
          return result
        except Exception, ex:
          frame = inspect.currentframe()
          args, _, _, values = inspect.getargvalues(frame)
          msg = ''
          for i in args:
            msg += "[%s : %s]" % (i,values[i])
          self.UserProfileLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
          return (-2,self.MakeExceptionMessage(str(ex)))
        