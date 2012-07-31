from django.http import HttpResponseRedirect



def NoticeIndex(noticeid):
    return HttpResponseRedirect('http://www.tnpuiet.thoughtxplore.com/comm/notice/iframe/' + str(noticeid))
