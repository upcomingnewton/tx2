from django.db import models
from tx2.Users.models import Menu
from tx2.Users.DBFunctions.DatabaseFunctions import DBMenuInsert , DBMenuUpdate
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_UPDATE
from tx2.Misc.CacheManagement import setCache,getCache
import logging

class MenuFnx():
    
        def __init__(self):
            #self.encrypt = Encrypt()
            self.UserLogger = logging.getLogger(LoggerUser)
            
        #CRUD FUNCTIONS
        
        def Insert(self,MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,by,ip,RequestedOperation=SYSTEM_PERMISSION_INSERT):
            try:
		details = {
		 		#'MenuId':3,
		 		'MenuName':MenuName,
		 		'MenuDesc':MenuDesc,
		 		'MenuUrl':MenuUrl,
		 		'MenuPid':MenuPid,
		 		'MenuIcon':MenuIcon,
		 		'RequestedOperation':RequestedOperation,
		 		#'LogDesc':'LogDesc',
		 		#'LogPreviousState':'LogPreviousState',
		 		'by':by,
		 		'ip':ip,
		 	}
                result = DBMenuInsert(details)
                return (result)
            except:
                exception_log = ('[%s] == EXCEPTION ==')%('Insert')
                self.UserLogger.exception(exception_log)
                return (-1,'Exception Occoured at Business Functions while creating menu')
                
        def Update(self,MenuId,MenuName,MenuDesc,MenuUrl,MenuPid,MenuIcon,by,ip,LogDesc,RequestedOperation=SYSTEM_PERMISSION_UPDATE):
            MenuObj = self.getMenuObjByMenuId(MenuId)
            if  MenuObj is None:
            	error_msg = '[%s] Menu does not exist for menuid %d' % ('Update',MenuId)
            	self.UserLogger.error(error_msg)
            	return (-1,error_msg)
            PreviousState = str(MenuObj)
            try:
		details = {
		 		'MenuId':MenuId,
		 		'MenuName':MenuName,
		 		'MenuDesc':MenuDesc,
		 		'MenuUrl':MenuUrl,
		 		'MenuPid':MenuPid,
		 		'MenuIcon':MenuIcon,
		 		'RequestedOperation':RequestedOperation,
		 		'LogDesc':LogDesc,
		 		'LogPreviousState':PreviousState,
		 		'by':by,
		 		'ip':ip,
		 	}
                result = DBMenuUpdate(details)
                return (result)
            except:
                exception_log = ('[%s] == EXCEPTION ==')%('Update')
                self.UserLogger.exception(exception_log)
                return (-1,'Exception Occoured at Business Functions while updating menu')


        # SELECTION AND QUERY FUNCTIONS
                    
        
    
        def getMenuObjByMenuId(self,menuid):
        	try:
        		return Menu.objects.get(id=menuid)
        	except:
        		return None
        		
        		
        def getMenuParentMenuObj(self):
        	try:
        		return Menu.objects.get(MenuPid=-1)
        	except:
        		return []
        		
        def getAllMenuObj(self):
        	try:
        		return Menu.objects.all()
        	except:
        		return []
