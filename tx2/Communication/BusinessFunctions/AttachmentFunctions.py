from tx2.Communication.DBFunctions.DBFunctions import DBInsertAttachment, DBUpdateAttachment
from tx2.CONFIG import LOGGER_COMMUNICATION
import logging


class AttachmentFnx():
    def __init__(self):
        self.CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
        
        
    def InsertAttachment(self,Content,Record, AttachmentType, AttachmentDesc, AttachmentName, AttachmentRef,by,ip,RequestedOperation):
        try:
            details= {
                        'Content': Content,
                        'Record': Record,
                        'AttachmentType':AttachmentType,
                        'AttachmentName':AttachmentName,
                        'AttachmentDesc':AttachmentDesc,
                        'AttachmentRef':AttachmentRef,
                        'op':RequestedOperation,
                        'by':by,
                        'ip':ip

                    }
            res= DBInsertAttachment(details)
            return res
        except:
            error_msg = 'Error @ InsertAttachment in Business Functions'
            self.CommunicationLogger.exception('[%s] == Exception =='%('InsertAttachment'))
            return (-5,error_msg)

    def UpdateAttachment(self,Content,Record, AttachmentType, AttachmentDesc, AttachmentName, AttachmentRef,by,ip,RequestedOperation,LogsDesc):
        try:
            details= {
                        'Content': Content,
                        'Record': Record,
                        'AttachmentType':AttachmentType,
                        'AttachmentName':AttachmentName,
                        'AttachmentDesc':AttachmentDesc,
                        'AttachmentRef':AttachmentRef,
                        'op':RequestedOperation,
                        'by':by,
                        'ip':ip,
                        'LogsDesc':LogsDesc

                    }
            res= DBUpdateAttachment(details)
            return res
        except:
            error_msg = 'Error @ UpdateAttachment in Business Functions'
            self.CommunicationLogger.exception('[%s] == Exception =='%('UpdateAttachment'))
            return (-5,error_msg)

        

        
