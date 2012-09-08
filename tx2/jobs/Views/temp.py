# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect
from tx2.jobs.BussinessFunctions.CompanyInfoFunctions import CompanyInfoFunctions
import inspect

def test(HttpRequest):
    ipadd = HttpRequest.META['REMOTE_ADDR']
    try:
      obj=CompanyInfoFunctions()
      result=obj.Update(_Id=2,CompanyName='test2', CompanyAdress='test3', CompanyWebsite='test4', CompanyAbout='test5', CompanyOtherDetails1='test6', CompanyOtherDetails2='test7', User=1,by=1,ip=ipadd)
      messages.error(HttpRequest,'result: %s %s'%(result[0],result[1]))
      return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
