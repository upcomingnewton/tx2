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
                       
                       url(r'^jobtype/$','jobs.Views.JobTypeViews.JobTypeIndex'),
                       url(r'^jobtype/add/post/$','jobs.Views.JobTypeViews.JobTypeAdd'),
                       
                       url(r'^company/(?P<CompanyID>\d+)/jobs/add/$','jobs.Views.JobViews.EditJobIndex',{'JobID':-1}),
                       )
