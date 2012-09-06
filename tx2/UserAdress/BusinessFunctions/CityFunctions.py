from tx2.UserAdress.DBFunctions.DatabaseFunctions import DBInsertCity
from tx2.UserAdress.DBFunctions.DBMessages import decode
from tx2.UserAdress.models import City
from tx2.CONFIG import LoggerAdress
from django.core.exceptions import ObjectDoesNotExist
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT
import logging
import inspect

class CityFnx():
    
  def __init__(self): 
    self.AdressLogger = logging.getLogger(LoggerAdress)
        #CRUD FUNCTIONS

  def Add(self,name,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
    try:
      details = {
        'ip':ip,
        'by':by,
        'name':name,
        'op':req_op,
        }
      result = DBInsertCity(details)
      if (result['result'] == 1):
        return (1,'SUCESS. City has been sucessfully added to database.') 
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

            
  def getAllCities(self):
    try:
      CityList =  City.objects.all()  
      return (1,CityList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      
  def getCityObjByName(self,name):
    try:
      CityObj =  City.objects.filter(CityName=name)  
      return (1,CityObj)
    except ObjectDoesNotExist:
      return (-1,'No City exists in database with this name')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))


