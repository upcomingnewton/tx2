'''
Created on 26-Jul-2012

@author: jivjot
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
                       
                       # Board
                       url(r'^Marks/Board/new$','UserProfile.Views.Marks.BoardInsert'),
                       url(r'^Marks/Board/View$','UserProfile.Views.Marks.BoardSelect'),
                       url(r'^Marks/Board/delete$','UserProfile.Views.Marks.BoardDelete'),
                       url(r'^Marks/Board/update$','UserProfile.Views.Marks.BoardUpdate'),
                       url(r'^Marks/Board/$','UserProfile.Views.Marks.BoardIndex'),
                       #DegreeType
                       url(r'^Marks/DegreeType/new$','UserProfile.Views.Marks.DegreeTypeInsert'),
                       url(r'^Marks/DegreeType/View$','UserProfile.Views.Marks.DegreeTypeSelect'),
                       url(r'^Marks/DegreeType/delete$','UserProfile.Views.Marks.DegreeTypeDelete'),
                       url(r'^Marks/DegreeType/update$','UserProfile.Views.Marks.DegreeTypeUpdate'),
                       url(r'^Marks/DegreeType/$','UserProfile.Views.Marks.DegreeTypeIndex'),
                      )