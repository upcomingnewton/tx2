from tx2.UserAdress.DBFunctions.DatabaseFunctions import DBInsertCountry
from tx2.UserAdress.DBFunctions.DBMessages import decode
from tx2.UserAdress.models import Country
from tx2.CONFIG import LoggerAdress
from django.core.exceptions import ObjectDoesNotExist
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT
import logging
import inspect

class CountryFnx():
    
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
      result = DBInsertCountry(details)
      if (result['result'] == 1):
        return (1,'SUCESS. Country has been sucessfully added to database.') 
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

            
  def getAllCountries(self):
    try:
      CountryList =  Country.objects.all()  
      return (1,CountryList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      
  def getCountryObjByName(self,name):
    try:
      CountryObj =  Country.objects.filter(CountryName=name)  
      return (1,CountryObj)
    except ObjectDoesNotExist:
      return (-1,'No Country exists in database with this name')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))


