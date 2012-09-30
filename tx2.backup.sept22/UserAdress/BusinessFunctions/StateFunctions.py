from tx2.UserAdress.DBFunctions.DatabaseFunctions import DBInsertState
from tx2.UserAdress.DBFunctions.DBMessages import decode
from tx2.UserAdress.models import State
from tx2.CONFIG import LoggerAdress
from django.core.exceptions import ObjectDoesNotExist
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT
import logging
import inspect

class StateFnx():
    
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
      result = DBInsertState(details)
      if (result['result'] == 1):
        return (1,'SUCESS. State has been sucessfully added to database.') 
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

            
  def getAllStates(self):
    try:
      StateList =  State.objects.all()  
      return (1,StateList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      
  def getStateObjByName(self,name):
    try:
      StateObj =  State.objects.filter(StateName=name)  
      return (1,StateObj)
    except ObjectDoesNotExist:
      return (-1,'No State exists in database with this name')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))


