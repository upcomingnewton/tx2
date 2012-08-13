'''
Created on Mar 3, 2012

@author: nitin
'''
from tx2.DataBaseHelper import DBhelper
from datetime import datetime
from tx2.CONFIG import LoggerUser, LoggerQuery
import logging

UserLogger = logging.getLogger(LoggerUser)
QueryLogger = logging.getLogger(LoggerQuery)
# USER SYSTEM
### ========================================================================================================  ### 


def DBInsertUser(userdetails):
    try:
        query = "SELECT * FROM UserInsert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['bday'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "'," + str(userdetails['entity']) + ",'" + userdetails['gender'] + "'," + str(userdetails['group']) + ",'" + userdetails['op'] + "'," + str(userdetails['by']) + ",'" + userdetails['ip'] +"'); "
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[Query] %s [RESULT] %s"%(query,result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBInsertUser : %s ',str(userdetails))
        return {'result':-5,'rescode':str(ex)}
        
def DBUpdateUser(userdetails):
    try:
        query = "SELECT * FROM UserUpdate('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['bday'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "'," + str(userdetails['entity']) + ",'" + userdetails['gender'] + "','" + userdetails['LogsDesc'] + "','" + userdetails['PreviousState']  + "'," + str(userdetails['group']) + ",'" + userdetails['op'] + "'," + str(userdetails['by']) + ",'" + userdetails['ip'] +"'); "
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[Query] %s [RESULT] %s"%(query,result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBUpdateUser : %s ',str(userdetails))
        return {'result':-5,'rescode':str(ex)}
        
def DBLoginUser(logindetails):
    try:
        query = "SELECT * FROM UserLogin('" + logindetails['email'] + "','" + logindetails['pass'] + "'," + str(logindetails['login_type']) + ",'" + logindetails['ip'] + "','" + str(datetime.now()) + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[Query] %s [RESULT] %s"%(query,result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBLoginUser : %s ',str(userdetails))
        return {'result':-5,'rescode':str(ex)}
    
def DBLogoutUser(details):
    try:
        query = "SELECT * FROM userlogout(" + str(details['loginid']) + "," +  str(details['logout_from']) + ",'" + str(datetime.now()) + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[Query] %s [RESULT] %s"%(query,result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBLoginUser : %s ',str(userdetails))
        return {'result':-5,'rescode':str(ex)}
    
### ========================================================================================================  ###  

def DBGroupTypeInsert(details):
    try:
        query = "SELECT * FROM GroupTypeInsert('"+ details['name'] +"','"+ details['desc'] +"','"+ details['req_op'] +"',"+ str(details['by']) +",'"+ details['ip'] +"');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[Query] %s [RESULT] %s"%(query,result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBGroupTypeInsert')
        return {'result':-5,'rescode':str(ex)}
        
    
def DBGroupInsert(details):
    try:
        query = "SELECT * FROM GroupInsert('" + details['GroupName'] + "','" + details['GroupDescription'] + "'," + str(details['GroupType']) + "," + str(details['GroupEntity']) + ",'" + details['RequestedOperation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        result =  DBhelper.CallFunction(query)
        UserLogger.debug("[Query] %s [RESULT] %s"%(query,result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBGroupInsert')
        return {'result':-5,'rescode':str(ex)}
      
# MENU SYSTEM
### ========================================================================================================  ### 

def DBMenuInsert(details):
    try:
	#SELECT * FROM  MenuInsert('MenuName','MenuDesc','MenuUrl','MenuPid','MenuIcon','RequestedOperation','by_user','_ip');
        query = "SELECT * FROM MenuInsert('" + details['MenuName'] + "','" + details['MenuDesc'] + "','" + details['MenuUrl'] + "'," + str(details['MenuPid']) + ",'" + details['MenuIcon'] + "','" + details['RequestedOperation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBMenuInsert',query))
        QueryLogger.debug('[%s] %s'%('DBMenuInsert',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBMenuInsert',result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBMenuInsert')
        return {'result':-5,'rescode':str(ex)}
        
def DBMenuUpdate(details):
    try:
	#SELECT * FROM  MenuUpdate(MenuId,MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,RequestedOperation,LogDesc,LogPreviousState,'by_user','_ip');
        query = "SELECT * FROM MenuUpdate(" + str(details['MenuId']) + ",'" + details['MenuName'] + "','" + details['MenuDesc'] + "','" + details['MenuUrl'] + "'," + str(details['MenuPid']) + ",'" + details['MenuIcon'] + "','" + details['RequestedOperation'] + "','" + details['LogDesc'] + "','" + details['LogPreviousState'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBMenuUpdate',query))
        QueryLogger.debug('[%s] %s'%('DBMenuUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBMenuUpdate',result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBMenuUpdate')
        return {'result':-5,'rescode':str(ex)}
        
        
def DBGroupMenuInsert(details):
    try:
	#SELECT * FROM  GroupMenuInsert(MenuStr,GroupID,PermissionStr,RequestedOperation,by_user,ip);
        query = "SELECT * FROM GroupMenuInsert('" + details['MenuStr'] + "'," + str(details['GroupID']) + ",'" + details['PermissionStr'] + "','" + details['RequestedOperation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBGroupMenuInsert',query))
        QueryLogger.debug('[%s] %s'%('DBGroupMenuInsert',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBGroupMenuInsert',result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBGroupMenuInsert')
        return {'result':-5,'rescode':str(ex)}
        
        
def DBGroupMenuDelete(details):
    try:
	#SELECT * FROM  GroupMenuDelete(MenuIDStr,RequestedOperation,by_user,ip);
        query = "SELECT * FROM GroupMenuDelete('" + details['MenuIDStr'] + "','" + details['RequestedOperation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBGroupMenuDelete',query))
        QueryLogger.debug('[%s] %s'%('DBGroupMenuDelete',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBGroupMenuDelete',result))
        return result[0]
    except Exception, ex:
        UserLogger.exception('DBGroupMenuDelete')
        return {'result':-5,'rescode':str(ex)}

