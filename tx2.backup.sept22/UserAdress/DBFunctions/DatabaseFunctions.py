'''
Created on Mar 3, 2012

@author: nitin
'''
from tx2.DataBaseHelper import DBhelper
from datetime import datetime
from tx2.CONFIG import LoggerAdress, LoggerQuery
import logging
import inspect

AdressLogger = logging.getLogger(LoggerAdress)
QueryLogger = logging.getLogger(LoggerQuery)

### ========================================================================================================  ### 

# SELECT * FROM UserAdress_City_Insert('Chandigarh','SYS_PER_INSERT',1,'test');
def DBInsertCity(details):
  try:
        query = "SELECT * FROM UserAdress_City_Insert('" + details['name'] + "','" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        QueryLogger.debug('%s' % (query))
        result =  DBhelper.CallFunction(query)
        AdressLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
### ========================================================================================================  ### 

# SELECT * FROM UserAdress_State_Insert('Chandigarh','SYS_PER_INSERT',1,'test');
def DBInsertState(details):
  try:
        query = "SELECT * FROM UserAdress_State_Insert('" + details['name'] + "','" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        QueryLogger.debug('%s' % (query))
        result =  DBhelper.CallFunction(query)
        AdressLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
### ========================================================================================================  ### 

# SELECT * FROM UserAdress_Country_Insert('Chandigarh','SYS_PER_INSERT',1,'test');
def DBInsertCountry(details):
  try:
        query = "SELECT * FROM UserAdress_Country_Insert('" + details['name'] + "','" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        QueryLogger.debug('%s' % (query))
        result =  DBhelper.CallFunction(query)
        AdressLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
### ========================================================================================================  ### 
### ========================================================================================================  ### 

def DBInsertUserContactInfo(details):
  try:
        query = "SELECT * FROM UserAdress_UserContactInfo_Insert(" + str(details['UserID']) +",'" + details['MobileNo'] + "','" + details['AltEmail'] + "','" + details['FatherName'] + "','" + details['FatherContactNo'] + "','" + details['MotherName'] + "','" + details['MotherContactNo'] + "'," + str(details['ParmanentAdress']) + "," + str(details['PresentAdress']) + ",'" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        QueryLogger.debug('%s' % (query))
        result =  DBhelper.CallFunction(query)
        AdressLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
### ========================================================================================================  ### 

def DBUpdateUserContactInfo(details):
  try:
        query = "SELECT * FROM UserAdress_UserContactInfo_Update(" + str(details['UserID']) +",'" + details['MobileNo'] + "','" + details['AltEmail'] + "','" + details['FatherName'] + "','" + details['FatherContactNo'] + "','" + details['MotherName'] + "','" + details['MotherContactNo'] + "'," + str(details['ParmanentAdress']) + "," + str(details['PresentAdress']) + ",'" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        QueryLogger.debug('%s' % (query))
        result =  DBhelper.CallFunction(query)
        AdressLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
### ========================================================================================================  ### 

def DBInsertAdress(details):
  try:
        query = "SELECT * FROM UserAdress_adress_Insert('" + details['AdressNo'] + "','" + details['StreetAdress1'] + "','" + details['StreetAdress2'] + "'," + str(details['City']) + "," + str(details['State']) + "," + str(details['Country']) + ",'" + (details['PinCode']) + "','" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        QueryLogger.debug('%s' % (query))
        result =  DBhelper.CallFunction(query)
        AdressLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
### ========================================================================================================  ### 

def DBUpdateAdress(details):
  try:
        query = "SELECT * FROM UserAdress_adress_Update(" + str(details['AdressID']) +",'" + details['AdressNo'] + "','" + details['StreetAdress1'] + "','" + details['StreetAdress2'] + "'," + str(details['City']) + "," + str(details['State']) + "," + str(details['Country']) + ",'" + (details['PinCode']) + "','" + details['op'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        QueryLogger.debug('%s' % (query))
        result =  DBhelper.CallFunction(query)
        AdressLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      AdressLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}

### ========================================================================================================  ### 
