from tx2.UserReg.models import Priority
from tx2.UserReg.DBFunctions.DBFunctions import DBUpdatePriority, DBInsertPriority
from tx2.Users.models import Group, User
class PriorityFnx():
    def updatePriority(self, ContentType, Record,UserGroup, PriorityVal, Desc,by,ip ):
        try:
            if(PriorityVal=='Default'):
                PriorityVal=1
            
            details={
                     'ContentType':ContentType, 
                     'Record': Record,
                     'Group': UserGroup,
                     'Priority':PriorityVal,
                     'Desc':Desc,
                     'RequestedOperation':'SYSTEM_PERMISSION_UPDATE',
                     'ByUser':by,
                     'ip':ip,
                     'LogsDesc':"Update"
                     }
            res= DBUpdatePriority(details)
            return res
        except:
            error_message= "Error @ updatePriority in Business Function"
            self.CommunicationLogger.exception('[%s] == Exception =='%('updatePriority'))
            return (-5, error_message)
    def setPriority(self, ContentType, Record,UserGroup, PriorityVal, Desc,by,ip ):
        try:
            if(PriorityVal=='Default'):
                PriorityVal=1
            
            details={
                     'ContentType':ContentType, 
                     'Record': Record,
                     'Group': UserGroup,
                     'Priority':PriorityVal,
                     'Desc':Desc,
                     'RequestedOperation':'SYSTEM_PERMISSION_INSERT',
                     'ByUser':by,
                     'ip':ip
                     }
            res= DBInsertPriority(details)
            return res
        except:
            error_message= "Error @ setPriority in Business Function"
            self.CommunicationLogger.exception('[%s] == Exception =='%('setPriority'))
            return (-5, error_message)
        
    def getPriorityByUserID(self, user_id, _ContentType,_Record):
        try:
            group=User.objects.get(id=user_id)
            if(group is None):
                return (-1, 'User doesnot Exist')
            else:
                GroupId=group.Group_id
            priority= Priority.objects.filter(ContentType=_ContentType, Record= _Record, UserGroup=GroupId)
            if(priority is None):
                return (-1,'Priority Record does not exists for this User-Group and record')
            else:
                return priority.PriorityVal 
        except:
            error_message= "Error @ getPriorityByUserID in Business Function"
            self.CommunicationLogger.exception('[%s] == Exception =='%('getPriorityByUserID'))
            return (-5, error_message)
        