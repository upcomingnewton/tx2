# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect
from tx2.jobs.BussinessFunctions.CompanyInfoFunctions import CompanyInfoFunctions
import inspect

def test(HttpRequest):
    ipadd = HttpRequest.META['REMOTE_ADDR']
    try:
      obj=CompanyInfoFunctions()
      result=obj.Add(CompanyName='test1', CompanyAdress='test2', CompanyWebsite='test3', CompanyAbout='test4', CompanyOtherDetails1='test5', CompanyOtherDetails2='test6', User=1,by=1,ip=ipadd)
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
