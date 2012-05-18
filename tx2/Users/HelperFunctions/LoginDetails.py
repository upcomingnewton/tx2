from tx2.CONFIG import LoggerUser
from tx2.Misc.Encryption import Encrypt
import logging

LOGGERUSER = logging.getLogger(LoggerUser)

def GetLoginDetails(request):
    encdec  = Encrypt()
    try:
        if "details" in request.session.keys():
            token = request.session["details"]
            return {"userid":token['userid'],"groupid":token['groupid'],"loginid": encdec.decrypt(token['loginid']),}
        else:
            return {"userid":-1}
    except:
        LOGGERUSER.exception('EXCEPTION IN GetLoginDetails')
        return {"userid":-1}