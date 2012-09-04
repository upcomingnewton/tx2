from tx2.UserAdress.DBFunctions.DatabaseFunctions import DBInsertUserContactInfo,DBUpdateUserContactInfo
from tx2.UserAdress.DBFunctions.DBMessages import decode
from tx2.UserAdress.models import UserContactInfo
from tx2.CONFIG import LoggerAdress
from django.core.exceptions import ObjectDoesNotExist
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT, SYSTEM_PERMISSION_UPDATE
import logging
import inspect

class UserContactInfoFnx():
    
  def __init__(self): 
    self.AdressLogger = logging.getLogger(LoggerAdress)
        #CRUD FUNCTIONS

  def Add(self,UserID,MobileNo,AltEmail,FatherName,FatherContactNo,MotherName,MotherContactNo,ParmanentAdress,PresentAdress,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
      details = {
          'UserID':UserID,
          'MobileNo':MobileNo,
          'AltEmail':AltEmail,
          'FatherName':FatherName,
          'FatherContactNo':FatherContactNo,
          'MotherName':MotherName,
          'MotherContactNo':MotherContactNo,
          'ParmanentAdress':ParmanentAdress,
          'PresentAdress':PresentAdress,
          'op':req_op,
          'by':by,
          'ip':ip,
        }
      result = DBInsertUserContactInfo(details)
      if (result['result'] == 1):
        return (1,'SUCESS. Contact information has been sucessfully added to database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))

  def Update(self,UserID,MobileNo,AltEmail,FatherName,FatherContactNo,MotherName,MotherContactNo,ParmanentAdress,PresentAdress,by,ip,req_op=SYSTEM_PERMISSION_UPDATE):
    try:
      details = {
          'UserID':UserID,
          'MobileNo':MobileNo,
          'AltEmail':AltEmail,
          'FatherName':FatherName,
          'FatherContactNo':FatherContactNo,
          'MotherName':MotherName,
          'MotherContactNo':MotherContactNo,
          'ParmanentAdress':ParmanentAdress,
          'PresentAdress':PresentAdress,
          'op':req_op,
          'by':by,
          'ip':ip,
        }
      result = DBUpdateUserContactInfo(details)
      if (result['result'] == 1):
        return (1,'SUCESS. Contact information has been sucessfully updated in database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))


  def Initialise(self,UserID,ParmanentAdress,PresentAdress,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
      details = {
          'UserID':UserID,
          'MobileNo':'NULL',
          'AltEmail':'NULL',
          'FatherName':'NULL',
          'FatherContactNo':'NULL',
          'MotherName':'NULL',
          'MotherContactNo':'NULL',
          'ParmanentAdress':ParmanentAdress,
          'PresentAdress':PresentAdress,
          'op':req_op,
          'by':by,
          'ip':ip,
        }
      result = DBInsertUserContactInfo(details)
      if (result['result'] == 1):
        return (1,'SUCESS. Contact information has been sucessfully updated in database.') 
      else:
        return (-1,decode(result))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))

        # SELECTION AND QUERY FUNCTIONS

      
  def getUserContactInfoByUserId(self,_id):
    try:
      UserContactInfoObj =  UserContactInfo.objects.get(User=_id)  
      return (1,UserContactInfoObj)
    except ObjectDoesNotExist:
      return (-1,'No Communication Info Object exists in database for this user.')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))


