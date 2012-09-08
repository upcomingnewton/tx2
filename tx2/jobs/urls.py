'''
Created on 08-Sep-2012

@author: jivjot
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
                       url(r'^test$','jobs.Views.temp.test'),
                       )