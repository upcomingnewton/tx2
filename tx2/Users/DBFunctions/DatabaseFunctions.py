'''
Created on Mar 3, 2012

@author: nitin
'''
from tx2.DataBaseHelper import DBhelper
from datetime import datetime
from tx2.CONFIG import LoggerUser, LoggerQuery
import logging
import inspect

UserLogger = logging.getLogger(LoggerUser)
QueryLogger = logging.getLogger(LoggerQuery)
# USER SYSTEM
### ========================================================================================================  ### 


def DBInsertUser(userdetails):
  try:
        query = "SELECT * FROM UserInsert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['bday'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "'," + str(userdetails['entity']) + ",'" + userdetails['gender'] + "'," + str(userdetails['group']) + ",'" + userdetails['op'] + "'," + str(userdetails['by']) + ",'" + userdetails['ip'] +"'); "
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
def DBUpdateUser(userdetails):
  try:
        query = "SELECT * FROM UserUpdate('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['bday'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "'," + str(userdetails['entity']) + ",'" + userdetails['gender'] + "','" + userdetails['LogsDesc'] + "','" + userdetails['PreviousState']  + "'," + str(userdetails['group']) + ",'" + userdetails['op'] + "'," + str(userdetails['by']) + ",'" + userdetails['ip'] +"'); "
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
def DBLoginUser(logindetails):
  try:
        query = "SELECT * FROM UserLogin('" + logindetails['email'] + "','" + logindetails['pass'] + "'," + str(logindetails['login_type']) + ",'" + logindetails['ip'] + "','" + str(datetime.now()) + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
    
def DBLogoutUser(details):
  try:
        query = "SELECT * FROM userlogout(" + str(details['loginid']) + "," +  str(details['logout_from']) + ",'" + str(datetime.now()) + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
    
### ========================================================================================================  ###  

def DBGroupTypeInsert(details):
  try:
        query = "SELECT * FROM GroupTypeInsert('"+ details['name'] +"','"+ details['desc'] +"','"+ details['req_op'] +"',"+ str(details['by']) +",'"+ details['ip'] +"');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
    
def DBGroupInsert(details):
  try:
        query = "SELECT * FROM GroupInsert('" + details['GroupName'] + "','" + details['GroupDescription'] + "'," + str(details['GroupType']) + "," + str(details['GroupEntity']) + ",'" + details['RequestedOperation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
      
# MENU SYSTEM
### ========================================================================================================  ### 

def DBMenuInsert(details):
  try:
	#SELECT * FROM  MenuInsert('MenuName','MenuDesc','MenuUrl','MenuPid','MenuIcon','RequestedOperation','by_user','_ip');
        query = "SELECT * FROM MenuInsert('" + details['MenuName'] + "','" + details['MenuDesc'] + "','" + details['MenuUrl'] + "'," + str(details['MenuPid']) + ",'" + details['MenuIcon'] + "','" + details['RequestedOperation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
def DBMenuUpdate(details):
  try:
	#SELECT * FROM  MenuUpdate(MenuId,MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,RequestedOperation,LogDesc,LogPreviousState,'by_user','_ip');
        query = "SELECT * FROM MenuUpdate(" + str(details['MenuId']) + ",'" + details['MenuName'] + "','" + details['MenuDesc'] + "','" + details['MenuUrl'] + "'," + str(details['MenuPid']) + ",'" + details['MenuIcon'] + "','" + details['RequestedOperation'] + "','" + details['LogDesc'] + "','" + details['LogPreviousState'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
        
#    SELECT * FROM groupmenuinsert(IN menustr character varying,
#                                  IN groupid integer, 
#                                  IN extrainfo character varying, 
#                                  IN permissionstr character varying, 
#                                  IN requestedoperation character varying, 
#                                  IN by_user integer, 
#                                  IN ip character varying, 
#                                  OUT result integer, 
#                                  OUT rescode integer)

def DBGroupMenuInsert(details):
  try:
	#SELECT * FROM  GroupMenuInsert(MenuStr,GroupID,PermissionStr,RequestedOperation,by_user,ip);
        query = "SELECT * FROM GroupMenuInsert('" + details['MenuStr'] + "'," + str(details['GroupID']) + ",'" + details['extrainfo'] + "','" + details['PermissionStr'] + "','" + details['RequestedOperation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
        
        
def DBGroupMenuDelete(details):
  try:
	#SELECT * FROM  GroupMenuDelete(MenuIDStr,RequestedOperation,by_user,ip);
        query = "SELECT * FROM GroupMenuDelete('" + details['MenuIDStr'] + "','" + details['RequestedOperation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[ %s ] [ %s ]" % (str(result[0]),query))
        return result[0]
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}



### ========================================================================================================  ### 
### ===========================    SELECT FUNCTIONS      ===================================================  ### 
### ========================================================================================================  ### 
def DBgetUserIDListByGroupID(groupid):
  try:
    query = 'SELECT id FROM "Users_user" WHERE "Group_id"=' + str(groupid)
    Result = DBhelper.CallSelectFunction(query)
    UserIDList = []
    for data in Result:
      UserIDList.append(data[0])
    return (1,UserIDList)
  except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      UserLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return {'result':-5,'rescode':str(ex)}
