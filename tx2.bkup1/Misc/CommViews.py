from django.http import HttpResponseRedirect,HttpResponse
from tx2.CONFIG import LoggerUser
import logging
LoggerUser = logging.getLogger(LoggerUser)


def NoticeIndex(HttpRequest,noticeid):
    s = 'http://tnpuiet.thoughtxplore.com/comm/notice/iframe/' + str(noticeid)
    return HttpResponseRedirect(s)
