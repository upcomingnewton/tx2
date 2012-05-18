
from tx2.Users.models import GroupType
from tx2.CONFIG import LoggerUser
import logging

class GroupFnx():
    
        def __init__(self):
            self.UserLogger = logging.getLogger(LoggerUser)
            
        #CRUD FUNCTIONS
        
#        def CreateGroup(self,gname,gdesc,gtype,entity,by,ip):
#            try:
#                self.UserLogger.debug('inside CreateGroup')
#                details = {
#                           'ip':ip,
#                           'by':by,
#                           'request':'INSERT',
#                           'entity':entity,
#                           'group_type_id':gtype,
#                           'groupname':gname,
#                           'groupdesc':gdesc,
#                           }
#                result = DBCreateGroup(details)
#                self.UserLogger.debug('[%s] %s,%s'%('CreateGroup',str(details),str(result)))
#                return (result,decode(int(result['result']), result['rescode']))
#            except:
#                exception_log = ('[%s] %s,%s,%s,%s,%s,%s')%('CreateGroup',gname,gdesc,gtype,entity,by,ip)
#                self.UserLogger.exception(exception_log)
#                return (-1,'Exception Occoured at Business Functions while creating group')


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
                    
        
    
      