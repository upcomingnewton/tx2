from tx2.UserReg.models import RegisterUser
from tx2.Communication.models import *
from tx2.Communication.DBFunctions.DBFunctions import DBInsertCommunicationType, DBInsertCommunicationTemplate
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypes,getContentTypesByAppNameAndModel,getStateIDbyStateName, deleteCacheKey
from tx2.CONFIG import LOGGER_COMMUNICATION
from tx2.conf.LocalProjectConfig import *
import logging
import datetime
from cPickle import dumps, loads
from tx2.Communication.BusinessFunctions.CommunicationTypeFunctions import CommunicationTypeFnx



class CommunicationTemplateFnx():
    
    def __init__(self):
        self.CommunicationLogger = logging.getLogger(LOGGER_COMMUNICATION)
    
    def insertCommunicationTemplate(self, CommTypeName, CommTempName, CommTempDesc, CommTempFormat, paramList, by, ip, RequestedOperation=SYSTEM_PERMISSION_INSERT):
        CACHE_COMMUNICATION_TYPES = 'CACHE_COMMUNICATION_TEMPLATE'
        try:
            CommunicationTypeObj = CommunicationTypeFnx()
            CommunicationTypeID = CommunicationTypeObj.getCommunicationTypeIDbyName(CommTypeName)

            CommTempFormat= dumps(CommTempFormat).encode("zip").encode("base64").strip()
            paramList= dumps(paramList).encode("zip").encode("base64").strip()
            
            details = {
                    'CommunicationType':CommunicationTypeID,    
                    'TemplateName': CommTempName,
                    'TemplateDisc':CommTempDesc,
                    'TemplateFormat':CommTempFormat,
                    'paramList':paramList,
                    'op':RequestedOperation,
                    'by':by,
                    'ip':ip,
                }
            res = DBInsertCommunicationTemplate(details)
            deleteCacheKey(CACHE_COMMUNICATION_TYPES)
            return res
        except:
            error_msg = 'Error @ InsertCommunicationTemplate in Business Functions'
            self.CommunicationLogger.exception('[%s] == Exception =='%('InsertCommunicationTemplate'))
            return (-5,error_msg)
    def getCommunicationTemplate(self):
        CACHE_COMMUNICATION_TEMPLATE = 'CACHE_COMMUNICATION_TEMPLATE'
        CommTemplateList = getCache(CACHE_COMMUNICATION_TEMPLATE)
        if CommTemplateList is None:
            CommTemplateList = CommunicationTemplates.objects.all()
            setCache(CACHE_COMMUNICATION_TEMPLATE,CommTemplateList)
        return CommTemplateList
            
    def getCommunicationTemplateIDbyName(self,_CommunicationTemplateName):
        CommunicationTemplateID = -1
        CommTemplateList = self.getCommunicationTemplate()
        if  CommTemplateList is None:
            return  CommunicationTemplateID
        for CommTemplateObj in CommTemplateList:
            print CommTemplateObj.CommName
            if CommTemplateObj.CommName == _CommunicationTemplateName:
                CommunicationTemplateID = CommTemplateObj.id
        print CommunicationTemplateID
        return CommunicationTemplateID


