from tx2.Users.DBFunctions.DatabaseFunctions import DBLoginUser ,DBLogoutUser, DBGroupTypeInsert
from tx2.Users.DBFunctions.DBMessages import decode
from tx2.Users.models import GroupType
from tx2.CONFIG import LoggerUser
from tx2.conf.LocalProjectConfig import SYSTEM_PERMISSION_INSERT, SYSTEM_USERDEFINED_GROUPTYPE
import logging

class GroupTypeFnx():
    
        def __init__(self):
            self.UserLogger = logging.getLogger(LoggerUser)
            
        #CRUD FUNCTIONS
        
        def CreateGroupType(self,gname,gdesc,by,ip,req_op=SYSTEM_PERMISSION_INSERT):
            try:
                self.UserLogger.debug('inside CreateGroupType')
                details = {
                           'ip':ip,
                           'by':by,
                           'name':gname,
                           'desc':gdesc,
                           'req_op':req_op,
                           }
                result = DBGroupTypeInsert(details)
                self.UserLogger.debug('[%s] %s,%s'%('CreateGroupType',str(details),str(result)))
                #return (result,decode(int(result['result']), result['rescode']))
            	return (1,result)
            except:
                exception_log = ('[%s] %s,%s,%s,%s')%('CreateGroupType',gname,gdesc,str(by),ip)
                self.UserLogger.exception(exception_log)
                return (-1,'Exception Occoured at Business Functions while  CreateGroupType')


        # SELECTION AND QUERY FUNCTIONS
            
        def ListAllGroupTypes(self):
            try:
                grouptypelist =  GroupType.objects.all()
                self.UserLogger.debug('[%s] %s'%('ListAllGroupTypes',str(len(grouptypelist))))
                return (1,grouptypelist)
            except:
                exception_log = ('[%s]')%('ListAllGroupTypes')
                self.UserLogger.exception(exception_log)
                return (-1,[])
                
        
        def getGroupTypeByName(self,gtypename):
        	#SYSTEM_USERDEFINED_GROUPTYPE      
            try:
                grouptype =  GroupType.objects.get(GroupTypeName=gtypename)
		return (1,grouptype)
            except:
                exception_log = ('[%s]')%('getGroupTypeByName')
                self.UserLogger.exception(exception_log)
                return (-1,'')      
        
    
      
