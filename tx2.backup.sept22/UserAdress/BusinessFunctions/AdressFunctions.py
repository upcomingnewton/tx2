from tx2.UserAdress.DBFunctions.DatabaseFunctions import DBInsertAdress,DBUpdateAdress
from tx2.UserAdress.DBFunctions.DBMessages import decode
from tx2.UserAdress.models import Adress
from tx2.CONFIG import LoggerAdress
from django.core.exceptions import ObjectDoesNotExist
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_UPDATE
import logging
import inspect

class AdressFnx():
    
  def __init__(self): 
    self.AdressLogger = logging.getLogger(LoggerAdress)
        #CRUD FUNCTIONS

  def Add(self,AdressNo,StreetAdress1,StreetAdress2,City,State,Country,PinCode,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
      details = {
          'AdressNo':AdressNo,
          'StreetAdress1':StreetAdress1,
          'StreetAdress2':StreetAdress2,
          'City':City,
          'State':State,
          'Country':Country,
          'PinCode':PinCode,
          'op':req_op,
          'by':by,
          'ip':ip,
        }
      result = DBInsertAdress(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
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


  def Update(self,AdressID,AdressNo,StreetAdress1,StreetAdress2,City,State,Country,PinCode,by,ip,req_op=SYSTEM_PERMISSION_UPDATE):
    try:
      details = {
          'AdressID':AdressID,
          'AdressNo':AdressNo,
          'StreetAdress1':StreetAdress1,
          'StreetAdress2':StreetAdress2,
          'City':City,
          'State':State,
          'Country':Country,
          'PinCode':PinCode,
          'op':req_op,
          'by':by,
          'ip':ip,
        }
      result = DBUpdateAdress(details)
      if (result['result'] == 1):
        return (1,result['rescode'] ) 
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

      
  def getAdressObjById(self,_id):
    try:
      AdressObj =  Adress.objects.get(id=_id)  
      return (1,AdressObj)
    except ObjectDoesNotExist:
      return (-1,'No Adress Object exists in database with this name')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))


