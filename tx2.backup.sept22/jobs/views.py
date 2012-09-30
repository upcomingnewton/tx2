# Create your views here.
import inspect
from django.contrib import messages
from django.http import HttpResponseRedirect
from tx2.jobs.BussinessFunctions.CompanyInfoFunctions import CompanyInfoFunctions
def test(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        obj=CompanyInfoFunctions()
        result=obj.Add(CompanyName='test1', CompanyAdress='test2', CompanyWebsite='test3', CompanyAbout='test4', CompanyOtherDetails1='test5', CompanyOtherDetails2='test6', 1, ip)
        messages.error(HttpRequest,'result: %s'%result)
        return HttpResponseRedirect('/message/')
    
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
