from tx2.DataBaseHelper import DBhelper
from datetime import datetime
from tx2.CONFIG import LoggerUser, LoggerQuery
import logging

UserLogger = logging.getLogger(LoggerUser)
QueryLogger = logging.getLogger(LoggerQuery)

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
