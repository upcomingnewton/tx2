from ThoughtXplore.txUser.DBFunctions.DatabaseFunctions import DBAddUserToGroup,DBAddUsertoSecGroupForCommunications
from django.db import models
from cPickle import dumps, loads
from ThoughtXplore.txUser.DBFunctions.DBMessages import db_messages,decode
from ThoughtXplore.txUser.models import User,Group,SecGroup_Comm

class UserGroupFnx(models.Model):
    
    def __init__(self):
        pass
    
    #CRUD FUNCTIONS
    
    def AddUserToGroup(self,groupid,userid,by_user,ip):
                    str_userid = ''
                    logsdesc = ""
                    print userid
                    for x in userid:
                        str_userid = str_userid + x + ','
                    str_userid = str_userid[:-1]
                    print str_userid
                    details = {
                                'groupid':groupid,
                                'userid':str_userid,
                                'logsdesc':logsdesc,
                                'by_user':by_user,
                                'ip':ip,
                               }
                    result = DBAddUserToGroup(details)
                    print result
                    return result
    def AddUserToSecGroupForComm(self,groupid,userlist,by,ip):
        d = SecGroup_Comm.objects.all()
        #print d[0]
        t = []
        prev = ''
        params = ''
        for x in d:
            #print x.id
            if ( x.Group.id == groupid):
                params = x.UserParams
                prev = dumps(x.User).encode("zip").encode("base64").strip()
                t = x.User + ',' + userlist + '-1'
        details = {
                   'groupid':groupid,
                    'userid':str(t),
                    'permission':'UPDATE',
                    'params':params,
                    'logdesc':'AddUserToSecGroupForComm',
                    'prevstate':prev,
                    'by':by,
                    'ip':ip
                   }
        result = DBAddUsertoSecGroupForCommunications(details)
        return (result[0],decode(int(result[0]), result[1],'AddUserToSecGroupForComm'))