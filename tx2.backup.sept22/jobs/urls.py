'''
Created on 08-Sep-2012

@author: jivjot
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
                       url(r'^test$','jobs.Views.temp.test'),
                       url(r'^company/add/$','jobs.Views.CompanyInfoViews.ObjectIndex',{'CompanyID':-1}),
                       url(r'^company/(?P<CompanyID>\d+)/edit/$','jobs.Views.CompanyInfoViews.ObjectIndex'),
                       url(r'^company/list/$','jobs.Views.CompanyInfoViews.ListIndex'),
                       url(r'^company/add/post/$','jobs.Views.CompanyInfoViews.EditCompany',{'CompanyID':-1}),
                       url(r'^company/(?P<CompanyID>\d+)/edit/post/$','jobs.Views.CompanyInfoViews.EditCompany'),
                       url(r'^details/(?P<JobID>\d+)/$','jobs.Views.JobViews.ListJobDetailsForStudents'),
                       url(r'^details/list/$','jobs.Views.JobViews.ListJobsForStudents'),
                       
                       url(r'^jobtype/$','jobs.Views.JobTypeViews.JobTypeIndex'),
                       url(r'^jobtype/add/post/$','jobs.Views.JobTypeViews.JobTypeAdd'),
                       
                       url(r'^company/(?P<CompanyID>\d+)/jobs/add/$','jobs.Views.JobViews.EditJobIndex',{'JobID':-1}),
                       url(r'^company/(?P<CompanyID>\d+)/jobs/list/$','jobs.Views.JobViews.ListJobsByCompany'),
                       url(r'^company/(?P<CompanyID>\d+)/jobs/add/post/$','jobs.Views.JobViews.AddJob'),
                       url(r'^company/(?P<CompanyID>\d+)/jobs/(?P<JobID>\d+)/edit/$','jobs.Views.JobViews.EditJobIndex'),
                       url(r'^company/(?P<CompanyID>\d+)/jobs/(?P<JobID>\d+)/edit/post/$','jobs.Views.JobViews.EditJob'),
                       url(r'^excel/job/(?P<JobId>\d+)/applied$','jobs.Views.StudentListView.ExcelJobApplied'),
                       url(r'^view/job/(?P<JobId>\d+)/applied$','jobs.Views.StudentListView.ViewJobApplied'),
                       
                       url(r'^branchjob/(?P<CompanyID>\d+)/jobs/(?P<JobID>\d+)/edit/post/$','jobs.Views.JobViews.BranchJobEdit'),
                       
                       url(r'^studentjobs/(?P<JobBranchID>\d+)/(?P<Status>\d+)/edit/post/$','jobs.Views.StudentJobViews.EditStudentJob'),
                       )
