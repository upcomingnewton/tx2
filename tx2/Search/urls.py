'''
Created on 08-Sep-2012

@author: jivjot
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
                       url(r'^$','Search.View.Search.SearchIndex'),
                       url(r'^PostBack$','Search.View.Search.SearchPostBack'),
                      )
