# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect
from tx2.jobs.BussinessFunctions.CompanyInfoFunctions import CompanyInfoFunctions
import inspect
from tx2.jobs.BussinessFunctions.JobFunctions import JobFunctions
from datetime import date
from tx2.jobs.BussinessFunctions.JobTypeFunctions import JobTypeFunctions
from tx2.jobs.BussinessFunctions.BranchJobFunctions import BranchJobFunctions
from tx2.jobs.BussinessFunctions.StudentCreditFunctions import StudentCreditFunctions
from tx2.Users.models import User
from tx2.Misc.ExcelResponse import ExcelResponse
from tx2.DataBaseHelper import DBhelper
def test(HttpRequest):
    ipadd = HttpRequest.META['REMOTE_ADDR']
    try:
      obj='Select * from "Users_user";'
      obj=DBhelper.CallSelectFunction(obj)
      obj=[(1,'jivjot'),(2,'jj')]
      
      return ExcelResponse(obj)
      result=obj.getObjectsbyUser(Userid=1)
      #result=obj.Update(_Id=1, Userid=1, JobType=1, Credit=3, by=1, ip=ipadd)
      #result=obj.Add(Userid=1, JobType=1, Credit=2, by=1, ip=ipadd)
      #result=obj.Add(Name='Name', by=1, ip=ipadd)
      #result=obj.Update(_Id=1, Name='fdfsd', by=1, ip=ipadd)
      #result=obj.Add(Branch=13, Job=2, JobType=1, Comments1='value1', Comments2='valuue2', by=1, ip=ipadd)
      #result=obj.Update(_Id=4, Branch=14, Job=2, JobType=1, Comments1='value2', Comments2='value3', by=1, ip=ipadd)
      #result=obj.getObjectsbyState(1)
      #result=obj.Update(3,CompanyName='test3', CompanyAdress='test3', CompanyWebsite='test4', CompanyAbout='test5', CompanyOtherDetails1='test6', CompanyOtherDetails2='test7', Userid=1,by=1,ip=ipadd)
      #result=obj.Add(CompanyId=2, Profile='valuue1', Designation='valuue2', Package='valuue3', DateOfVisit='1 Jan 2012', JobDetails1='valuue4', JobDetails2='valuue5', RecruitmentRounds='valuue6', ContactPersonName='valuue7', ContactPersonMobile='valuue8', ContactPersonEmail='valuue9', ContactPersonDetails='valuue10', RegistrationsUpto='1 jan 2013', by=1, ip=ipadd)
      #result=obj.Update(2,CompanyId=2, Profile='valuue2', Designation='valuue3', Package='valuue4', DateOfVisit='1 Jan 2013', JobDetails1='valuue5', JobDetails2='valuue6', RecruitmentRounds='valuue7', ContactPersonName='valuue8', ContactPersonMobile='valuue9', ContactPersonEmail='valuue10', ContactPersonDetails='valuue11', RegistrationsUpto='1 jan 2014', by=1, ip=ipadd)
      #result=obj.getObjectByRegistraionUpto(date(2014,1,1))
      #result=(obj.getObjectByUserId(1))
      messages.error(HttpRequest,'result: %s %s'%(result[0],result[1]))
#      messages.error(HttpRequest,'result: %s'%(result))
      
      return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
