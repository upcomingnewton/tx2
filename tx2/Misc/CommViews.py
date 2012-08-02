from django.http import HttpResponseRedirect
from tx2.CONFIG import LoggerUser
import logging
LoggerUser = logging.getLogger(LoggerUser)


def NoticeIndex(noticeid):
    s = 'http://www.tnpuiet.thoughtxplore.com/comm/notice/iframe/' + str(noticeid)
    LoggerUser.debug('redirecting to : %s'%(s) )
    return HttpResponseRedirect(s)
