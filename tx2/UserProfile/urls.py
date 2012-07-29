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
                       #Branch
                       url(r'^UserProfile/Branch/new$','UserProfile.Views.UserProfile.BranchInsert'),
                       url(r'^UserProfile/Branch/View$','UserProfile.Views.UserProfile.BranchSelect'),
                       url(r'^UserProfile/Branch/delete$','UserProfile.Views.UserProfile.BranchDelete'),
                       url(r'^UserProfile/Branch/update$','UserProfile.Views.UserProfile.BranchUpdate'),
                       url(r'^UserProfile/Branch/$','UserProfile.Views.UserProfile.BranchIndex'),
                       #Category
                       url(r'^UserProfile/Category/new$','UserProfile.Views.UserProfile.CategoryInsert'),
                       url(r'^UserProfile/Category/View$','UserProfile.Views.UserProfile.CategorySelect'),
                       url(r'^UserProfile/Category/delete$','UserProfile.Views.UserProfile.CategoryDelete'),
                       url(r'^UserProfile/Category/update$','UserProfile.Views.UserProfile.CategoryUpdate'),
                       url(r'^UserProfile/Category/$','UserProfile.Views.UserProfile.CategoryIndex'),
                      
                      )