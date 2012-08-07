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
    
    	#SELECT * FROM UserInsert('testfromdb1','testfromdb1',current_date,'testfromdb1','testfromdb1','testfromdb1',1,'S',3,'SYS_PER_INSERT',2,'RequestedOperation');
    query = "SELECT * FROM UserInsert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['bday'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "'," + str(userdetails['entity']) + ",'" + userdetails['gender'] + "'," + str(userdetails['group']) + ",'" + userdetails['op'] + "'," + str(userdetails['by']) + ",'" + userdetails['ip'] +"'); "
    try:
        UserLogger.debug('[%s] %s'%('DBInsertUser',query))
        QueryLogger.debug('[%s] %s'%('DBLogoutUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBInsertUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
def DBUpdateUser(userdetails):
    query = "SELECT * FROM UserUpdate('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['bday'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "'," + str(userdetails['entity']) + ",'" + userdetails['gender'] + "','" + userdetails['LogsDesc'] + "','" + userdetails['PreviousState']  + "'," + str(userdetails['group']) + ",'" + userdetails['op'] + "'," + str(userdetails['by']) + ",'" + userdetails['ip'] +"'); "
    try:
        UserLogger.debug('[%s] %s'%('DBUpdateUser',query))
        QueryLogger.debug('[%s] %s'%('DBLogoutUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBUpdateUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBUpdateUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
def DBLoginUser(logindetails):
	#SELECT * FROM UserLogin('SystemInit1@init.com','41MCGF_P4L5U6S98h0viy4QQ2mOBhZdsWPSHVqCQ6Il6mwkyNY1k=',1,'testfromdb',now());
    try:
        query = "SELECT * FROM UserLogin('" + logindetails['email'] + "','" + logindetails['pass'] + "'," + str(logindetails['login_type']) + ",'" + logindetails['ip'] + "','" + str(datetime.now()) + "');"
        UserLogger.debug('[%s] %s'%('DBLoginUser',query))
        QueryLogger.debug('[%s] %s'%('DBLoginUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBLoginUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBLoginUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
    
def DBLogoutUser(details):
	#SELECT * FROM UserLogout(1,1,now());
    try:
        query = "SELECT * FROM userlogout(" + str(details['loginid']) + "," +  str(details['logout_from']) + ",'" + str(datetime.now()) + "');"
        UserLogger.debug('[%s] %s'%('DBLogoutUser',query))
        QueryLogger.debug('[%s] %s'%('DBLogoutUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBLogoutUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBLogoutUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
    
### ========================================================================================================  ###  

def DBGroupTypeInsert(details):
    try:
    	#SELECT * FROM GroupTypeInsert('testfromdb','testfromdb','SystemInit_Insert',1,'test');
        query = "SELECT * FROM GroupTypeInsert('"+ details['name'] +"','"+ details['desc'] +"','"+ details['req_op'] +"',"+ str(details['by']) +",'"+ details['ip'] +"');"
        UserLogger.debug('[%s] %s'%('DBGroupTypeInsert',query))
        QueryLogger.debug('[%s] %s'%('DBGroupTypeInsert',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBGroupTypeInsert',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBGroupTypeInsert',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
    
def DBGroupInsert(details):
    try:
    	#SELECT * FROM GroupTypeInsert('testfromdb','testfromdb','SystemInit_Insert',1,'test');
        query = "SELECT * FROM GroupInsert('" + details['GroupName'] + "','" + details['GroupDescription'] + "'," + str(details['GroupType']) + "," + str(details['GroupEntity']) + ",'" + details['RequestedOperation'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBGroupInsert',query))
        QueryLogger.debug('[%s] %s'%('DBGroupInsert',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBGroupInsert',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBGroupInsert',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
      
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
        UserLogger.exception("[%s] %s"%('DBMenuInsert'))
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
        UserLogger.exception("[%s] %s"%('DBMenuUpdate'))
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
        UserLogger.exception("[%s] %s"%('DBGroupMenuInsert'))
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
        UserLogger.exception("[%s] %s"%('DBGroupMenuDelete'))
        return {'result':-5,'rescode':str(ex)}

