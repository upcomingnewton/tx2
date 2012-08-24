from tx2.UserReg.models import RegisterUser
from tx2.UserReg.DBFunctions.DBFunctions import DBRegUserUpdate,DBRegUserInsert
from tx2.UserReg.models import RegisterUser
from tx2.Users.models import User
from tx2.Misc.CacheManagement import setCache,getCache,getContentTypeIdFromModelandAppLabel
from tx2.CONFIG import LOGGER_UserReg
import logging
import datetime
from tx2.conf.LocalProjectConfig import *
from django.core.exceptions import ObjectDoesNotExist
import inspect

class UserRegFnx():
  def __init__(self):
                self.UserRegLogger = logging.getLogger(LOGGER_UserReg)
                self.UserSep = "$"
                self.GroupSep = "!"
                
        #Internal function
        # it takes input like ['1','2','3','4'] ... this is
        # what you usually get, when you put choice buttons on a 
        # web page ....
  def ConvertStringListtoIntegerList(self,StringList):
    try:
      res = [ int(i) for i in StringList]
      frame = inspect.currentframe()
      self.UserRegLogger.debug("[%s] IN = %s \n OUT = %s"%(inspect.getframeinfo(frame)[2],str(StringList),str(res)))
      return (1,res)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))



# this method will only return unique integers from a list of integers
  def getUniqueIntegerList(self,IntegerList):
    try:
      res = []
      num = len(IntegerList)
      for x in range(0,num):
        if IntegerList[x] not in IntegerList[x+1:]:
          res.append(IntegerList[x])
      frame = inspect.currentframe()
      self.UserRegLogger.debug("[%s] IN = %s \n OUT = %s"%(inspect.getframeinfo(frame)[2],str(IntegerList),str(res)))
      return (1,res)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))



#ConvertUsersListToString
#this method converts an integer list to a string 
# sepaarated by some separator
  def  ConvertIntegerListToDBString(self,IntegerList,sep):
    try:
      userstr = ''
      for _int in IntegerList:
        userstr += str(_int) + sep
      #userstr = userstr[:-1]
      frame = inspect.currentframe()
      self.UserRegLogger.debug("[%s] IN = %s, %s \n OUT = %s"%(inspect.getframeinfo(frame)[2],str(IntegerList),str(sep),userstr))
      return (1,userstr)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
        
        #Internal function
# it expects some string like (val1 sep val2 sep)
  def ConvertDBStringtoIntegerList(self,DBString,sep):
    try:
      _str = DBString.split(sep)
      _str = _str[:-1]
      res = [int(i) for i in _str]
      frame = inspect.currentframe()
      self.UserRegLogger.debug("[%s] IN = %s, %s \n OUT = %s"%(inspect.getframeinfo(frame)[2],str(DBString),str(sep),res))
      return (1,res)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))

  def Create(self,MetaInfo,Desc,Users,Groups,ReferenceToRegisterUser,Record,ContentType,Operation,by,ip):
    try:
        details = {
                'MetaInfo':MetaInfo,
                'Desc':Desc,
                'Users':Users,
                'Groups':Groups,
                'ReferenceToRegisterUser':ReferenceToRegisterUser,
                'Record':Record,#int
                'ContentType':ContentType,#int
                'Operation':Operation,
                'by':by,#int
                'ip':ip,
        }
        result = DBRegUserInsert(details)
        return (1,result)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
                        
  def Update(self,MetaInfo,Desc,Users,Groups,ReferenceToRegisterUser,Record,ContentType,Operation,by,ip,LogsDesc):
    try:
      details = {
                'MetaInfo':MetaInfo,
                'Desc':Desc,
                'Users':Users,
                'Groups':Groups,
                'ReferenceToRegisterUser':ReferenceToRegisterUser,
                'Record':Record,#int
                'ContentType':ContentType,#int
                'Operation':Operation,
                'LogsDesc':LogsDesc,
                'by':by,#int
                'ip':ip,
      }
      result = DBRegUserUpdate(details)
      return (1,result)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      
  def AdduserData(self,AppLabel,Model,rid,_Desc,by,ip,Users=-1,Groups=-1,op_insert=SYSTEM_PERMISSION_INSERT,op_update=SYSTEM_PERMISSION_UPDATE,ReferenceToRegisterUser=-1):
    try:
      # get the object, if present
      ctid = getContentTypeIdFromModelandAppLabel(AppLabel,Model)
      if( ctid[0] is not 1):
        return (-1,ctid[1])
      ctid = ctid[1]
      Desc = ''
      try:
        # get the object, if it is already there in database, also it creates DoesNotExist exception
        # in case no value is thgere in database
        UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
        UsersList = []
        GroupList = []
        DBUsersNullValue = self.UserSep * 3
        DBGroupsNullValue = self.GroupSep * 3
        # if there is some users list in input
                ###############  WE CHECK FOR Users ##############
        Desc += 'UPDATE.'
        if Users is not -1:
          #check if , earlier there was some entry for users in this record
          if UserRegObj.Users != DBUsersNullValue:
            # yes , there was some, get that value, and convert it to integer list
            DBStringList = self.ConvertDBStringtoIntegerList(UserRegObj.Users,self.UserSep)
            if DBStringList[0] is not 1:
              return (-1,DBStringList[1])
            DBStringList = DBStringList[1]
          else:
            # no there was not 
            DBStringList = []
        
          # this is a list of users , whom the user has requested to add to exisiting list
          UserReqList = self.ConvertStringListtoIntegerList(Users)
          if UserReqList[0] is not 1:
            return (-1,UserReqList[1])
          UserReqList = UserReqList[1]

          if len(DBStringList) > 0:
            UsersList = UsersList + DBStringList 
          if len(UserReqList) > 0:
            UsersList = UsersList + UserReqList
          UsersList = self.getUniqueIntegerList(UsersList)
          if( UsersList[0] is not 1):
            return (-1,UsersList[1])
          UsersList = self.ConvertIntegerListToDBString(UsersList[1],self.UserSep)
          if( UsersList[0] is not 1):
            return (-1,UsersList[1])
          UsersList = UsersList[1]
        else:
          UsersList = DBUsersNullValue
        Desc += 'Users : ' + UsersList + '.'
                ############### NOW WE CHECK FOR GROUPS ##############
        
        if Groups is not -1:
          #check if , earlier there was some entry for groups in this record
          if UserRegObj.Groups != DBGroupsNullValue:
            # yes , there was some, get that value, and convert it to integer list
            DBStringList = self.ConvertDBStringtoIntegerList(UserRegObj.Groups,self.GroupSep)
            if DBStringList[0] is not 1:
              return (-1,DBStringList[1])
            DBStringList = DBStringList[1]
          else:
            # no there was not 
            DBStringList = []
        
          # this is a list of groups , whom the user has requested to add to exisiting list
          UserReqList = self.ConvertStringListtoIntegerList(Groups)
          if UserReqList[0] is not 1:
            return (-1,UserReqList[1])
          UserReqList = UserReqList[1]

          if len(DBStringList) > 0:
            GroupList = GroupList + DBStringList 
          if len(UserReqList) > 0:
            GroupList = GroupList + UserReqList
          GroupList = self.getUniqueIntegerList(GroupList)
          if( GroupList[0] is not 1):
            return (-1,GroupList[1])
          GroupList = self.ConvertIntegerListToDBString(GroupList[1],self.GroupSep)
          if( GroupList[0] is not 1):
            return (-1,GroupList[1])
          GroupList = GroupList[1]
        else:
          GroupList = DBGroupsNullValue
        Desc += 'Groups : ' + GroupList + '.'
        return self.Update("-1",_Desc,UsersList,GroupList,"-1",rid,ctid,op_update,by,ip,Desc)
        #Update(self,MetaInfo,Desc,Users,Groups,ReferenceToRegisterUser,Record,ContentType,Operation,by,ip,LogsDesc):
      except  ObjectDoesNotExist , DoesNotExist:
        UsersList = []
        GroupList = []
        Desc += 'iNSERT.'
        DBUsersNullValue = self.UserSep * 3
        DBGroupsNullValue = self.GroupSep * 3
        if Users is not -1:
          # this is a list of users , whom the user has requested to add to exisiting list
          UserReqList = self.ConvertStringListtoIntegerList(Users)
          if UserReqList[0] is not 1:
            return (-1,UserReqList[1])
          UserReqList = UserReqList[1]
          UsersList = UserReqList
          UsersList = self.getUniqueIntegerList(UsersList)
          if( UsersList[0] is not 1):
            return (-1,UsersList[1])
          UsersList = self.ConvertIntegerListToDBString(UsersList[1],self.UserSep)
          if( UsersList[0] is not 1):
            return (-1,UsersList[1])
          UsersList = UsersList[1]
        else:
          UsersList = DBUsersNullValue
        Desc += 'Users : ' + UsersList + '.'

        if Groups is not -1:
          # this is a list of groups , whom the user has requested to add to exisiting list
          UserReqList = self.ConvertStringListtoIntegerList(Groups)
          if UserReqList[0] is not 1:
            return (-1,UserReqList[1])
          UserReqList = UserReqList[1]
          GroupsList = UserReqList
          GroupList = self.getUniqueIntegerList(GroupList)
          if( GroupList[0] is not 1):
            return (-1,GroupList[1])
          GroupList = self.ConvertIntegerListToDBString(GroupList[1],self.GroupSep)
          if( GroupList[0] is not 1):
            return (-1,GroupList[1])
          GroupList = GroupList[1]
        else:
          GroupList = DBGroupsNullValue
        Desc += 'Groups : ' + GroupList + '.'
        return self.Create(Desc,_Desc,UsersList,GroupList,"-1",rid,ctid,op_insert,by,ip)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))

  def DeleteUsersAndGroups(self,AppLabel,Model,rid,by,ip,Users = -1,Groups = -1,op_delete=SYSTEM_PERMISSION_DELETE):
    try:
      ctid = getContentTypeIdFromModelandAppLabel(AppLabel,Model)
      DBUsersNullValue = self.UserSep * 3
      DBGroupsNullValue = self.GroupSep * 3
      if( ctid[0] is not 1):
        return (-1,ctid[1])
      ctid = ctid[1]
      Desc = 'DELETE.'
      try:
        UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
        if Users is not -1:
          Desc += ' Users - '
          DBStringList = []
          if UserRegObj.Users != DBUsersNullValue:
            # yes , there was some, get that value, and convert it to integer list
            DBStringList = self.ConvertDBStringtoIntegerList(UserRegObj.Users,self.UserSep)
            if DBStringList[0] is not 1:
              return (-1,DBStringList[1])
            DBStringList = DBStringList[1]
          else:
            # no users present
            return (-1,'No user is registered for this content type id.')
          # this is a list of users , whom the user has requested to delete from exisiting list
          UserReqList = self.ConvertStringListtoIntegerList(Users)
          if UserReqList[0] is not 1:
            return (-1,UserReqList[1])
          UserReqList = UserReqList[1]
          UpdatedUsersList = []
          for x in DBStringList:
            if x not in UserReqList:
              UpdatedUsersList.append(x)
            else:
              Desc += str(x) + ','
          UpdatedUsersList = self.ConvertIntegerListToDBString(UpdatedUsersList,self.UserSep)
          if( UpdatedUsersList[0] is not 1):
            return (-1,UpdatedUsersList[1])
          UpdatedUsersList = UpdatedUsersList[1]
        else:
          UpdatedUsersList = UserRegObj.Users
          
        if Groups is not -1:
          Desc += 'Groups - '
          DBStringList = []
          if UserRegObj.Groups != DBGroupsNullValue:
            # yes , there was some, get that value, and convert it to integer list
            DBStringList = self.ConvertDBStringtoIntegerList(UserRegObj.Groups,self.GroupSep)
            if DBStringList[0] is not 1:
              return (-1,DBStringList[1])
            DBStringList = DBStringList[1]
          else:
            # no groups present
            return (-1,'No group is registered for this content type id.')
          # this is a list of groups , whom the user has requested to delete from exisiting list
          UserReqList = self.ConvertStringListtoIntegerList(Groups)
          if UserReqList[0] is not 1:
            return (-1,UserReqList[1])
          UserReqList = UserReqList[1]
          UpdatedGroupsList = []
          for x in DBStringList:
            if x not in UserReqList:
              UpdatedGroupsList.append(x)
            else:
              Desc += str(x) + ','
          UpdatedGroupsList = self.ConvertIntegerListToDBString(UpdatedGroupsList,self.GroupSep)
          if( UpdatedGroupsList[0] is not 1):
            return (-1,UpdatedGroupsList[1])
          UpdatedGroupsList = UpdatedGroupsList[1]
        else:
          UpdatedGroupsList = UserRegObj.Groups
        return self.Update("-2",UserRegObj.Desc,UpdatedUsersList,UpdatedGroupsList,"-1",rid,ctid,op_delete,by,ip,Desc)
      except  ObjectDoesNotExist , DoesNotExist:
        error_msg = 'No data for this content type'
        return (-1,error_msg)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
                        
                        
                        
  # SELECT FUNCTIONS

  def getUserIDListForARecord(self,AppLabel,Model,rid):
    DBUsersNullValue = self.UserSep * 3
    DBGroupsNullValue = self.GroupSep * 3
    try:
      ctid = getContentTypeIdFromModelandAppLabel(AppLabel,Model)
      if( ctid[0] is not 1):
        return (-1,ctid[1])
      ctid = ctid[1]
      try:
        UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
        DBStringList = []
        if UserRegObj.Users != DBUsersNullValue:
            # yes , there was some, get that value, and convert it to integer list
            DBStringList = self.ConvertDBStringtoIntegerList(UserRegObj.Users,self.UserSep)
            if DBStringList[0] is not 1:
              return (-1,DBStringList[1])
            DBStringList = DBStringList[1]
          else:
            # no users present
            return (-1,'No user is registered for this content type id.')
        return (1,DBStringList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))

  def getGroupIDListForARecord(self,AppLabel,Model,rid):
    DBUsersNullValue = self.UserSep * 3
    DBGroupsNullValue = self.GroupSep * 3
    try:
      ctid = getContentTypeIdFromModelandAppLabel(AppLabel,Model)
      if( ctid[0] is not 1):
        return (-1,ctid[1])
      ctid = ctid[1]
      try:
        UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
        DBStringList = []
        if UserRegObj.Groups != DBGroupsNullValue:
            # yes , there was some, get that value, and convert it to integer list
            DBStringList = self.ConvertDBStringtoIntegerList(UserRegObj.Groups,self.GroupSep)
            if DBStringList[0] is not 1:
              return (-1,DBStringList[1])
            DBStringList = DBStringList[1]
          else:
            # no users present
            return (-1,'No group is registered for this content type id.')
        return (1,DBStringList)
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))
      

  def getCompleteListOfUsersForAUser(self,AppLabel,Model,rid):
  # get users list
  # get groups list
  # get users of a group
  # megre both lists
  # get unique userids and return 
    try:
      UsersList = self.getUserIDListForARecord(AppLabel,Model,rid)
      if( UsersList[0] != 1):
        return (-1,UsersList[1])
      UsersList = UsersList[1]
      GroupsList = self.getGroupIDListForARecord(AppLabel,Model,rid)
      if( GroupsList[0] != 1):
        return (-1,GroupsList[1])
      GroupsList = GroupsList[1]
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      self.UserRegLogger.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      return (-2,str(ex))

#  def getUserObjectListForARecord(self,AppLabel,Model,rid):
#    try:
#                        ctid = -1
#                        ctlist = getContentTypes()
#                        for ctobj in ctlist:
#        if ctobj.app_label == AppLabel and ctobj.model == Model:
#                ctid = ctobj.id
#                        if ctid == -1:
#        #error here
#        error_msg = 'Invalid Applabel %s or Model %s' % (AppLabel, Model)
#        self.UserRegLogger.error('[%s] == Error == \n %s'%('getUserObjectListForARecord',error_msg))
#        return (-1,error_msg)
#                        try:
#        UserRegObj = RegisterUser.objects.get(ContentType__id=ctid , Record = rid)
#        user_id_list_str = str(self.getUserIDListForARecord(AppLabel,Model,rid)) # TODO check if it works
#        query = "id IN (" +  user_id_list_str[1:-1] + ")" 
#        UserObjList = User.objects.extra(where=[query])
#        return (1,UserObjList)
#                        except  ObjectDoesNotExist , DoesNotExist:
#        error_msg = 'Error Record Does not exist'
#        self.UserRegLogger.error('[%s] == Error == \n %s'%('getUserObjectListForARecord',error_msg))
#        return (-1,error_msg)
#    except:
#                        self.UserRegLogger.exception('[%s] == Exception =='%('getUserObjectListForARecord'))
#                        return (-1,'Error at business level getUserObjectListForARecord function in UserReg')

#  def getContentTypeAndRecordByUserID(self,userid):
#                try:
#                        query = self.UserSep + str(userid) + self.UserSep
#                        UserRegObjList = RegisterUser.objects.filter(Users__contains=query)
#                        return (1,UserRegObjList)
#                except:
#                        self.UserRegLogger.exception('[%s] == Exception =='%('getContentTypeAndRecordByUserID'))
#                        return (-1,'Error at business level getContentTypeAndRecordByUserID function in UserReg')
                        
#  def getContentTypeAndRecordByGroupID(self,gid):
#                try:
#                        query = self.GroupSep + str(gid) + self.GroupSep
#                        GroupRegObjList = RegisterUser.objects.filter(Groups__contains=query)
#                        return (1,GroupRegObjList)
#                except:
#                        self.UserRegLogger.exception('[%s] == Exception =='%('getContentTypeAndRecordByGroupID'))
#                        return (-1,'Error at business level getContentTypeAndRecordByGroupID function in UserReg')
                        
#  def geRecordIDListByUserIDAndContentType(self,Applabel,Model,userid):
#                try:
#                        ctid = -1
#                        ctlist = getContentTypes()
#                        for ctobj in ctlist:
#        if ctobj.app_label == Applabel and ctobj.model == Model:
#                ctid = ctobj.id
#                        if ctid == -1:
#        #error here
#        error_msg = 'Invalid Applabel %s or Model %s' % (AppLabel, Model)
#        self.UserRegLogger.error('[%s] == Error == \n %s'%('geRecordIDListByUserIDAndContentType',error_msg))
#        return (-1,error_msg)
#                        try:
#        query = "$" + str(userid) + "$"
#        UserRegObjList = RegisterUser.objects.filter(Users__contains=query,ContentType__id=ctid)
#        return (1,UserRegObjList)
#                        except  ObjectDoesNotExist , DoesNotExist:
#        error_msg = 'Error Record Does not exist'
#        self.UserRegLogger.error('[%s] == Error == \n %s'%('geRecordIDListByUserIDAndContentType',error_msg))
#        return (-1,error_msg)
#                except:
#                        self.UserRegLogger.exception('[%s] == Exception =='%('geRecordIDListByUserIDAndContentType'))
#                        return (-1,'Error at business level geRecordIDListByUserIDAndContentType function in UserReg')
                        
                        
#  def geRecordIDListByGroupIDAndContentType(self,Applabel,Model,groupid):
#    try:
#      ctid = -1
#      ctlist = getContentTypes()
#                        for ctobj in ctlist:
#        if ctobj.app_label == Applabel and ctobj.model == Model:
#                ctid = ctobj.id
#                        if ctid == -1:
#        #error here
#        error_msg = 'Invalid Applabel %s or Model %s' % (AppLabel, Model)
#        self.UserRegLogger.error('[%s] == Error == \n %s'%('geRecordIDListByUserIDAndContentType',error_msg))
#        return (-1,error_msg)
#                        try:
#        query2 = self.GroupSep + str(groupid) + self.GroupSep
#        GroupRegObjList = RegisterUser.objects.filter(Groups__contains=query2,ContentType__id=ctid)
#        return (1,GroupRegObjList)
#                        except  ObjectDoesNotExist , DoesNotExist:
#        error_msg = 'Error Record Does not exist'
#        self.UserRegLogger.error('[%s] == Error == \n %s'%('geRecordIDListByUserIDAndContentType',error_msg))
#        return (-1,error_msg)
#                except:
#                        self.UserRegLogger.exception('[%s] == Exception =='%('geRecordIDListByUserIDAndContentType'))
#                        return (-1,'Error at business level geRecordIDListByUserIDAndContentType function in UserReg')
