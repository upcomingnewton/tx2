from django.conf.urls.defaults import patterns, url



urlpatterns = patterns('',
                       
                       # states
                       url(r'^state/$','Security.Views.StateViews.StatesIndex'),
                       url(r'^state/create/$','Security.Views.StateViews.CreateNewStateIndex',{'init':0}),
                       url(r'^state/create/new/$','Security.Views.StateViews.CreateNewState',{'init':0}), 
                       url(r'^state/list/$','Security.Views.StateViews.ListAllStates'),
                       
                       url(r'^contenttypes/list/$','Security.Views.ContentTypeViews.ListAllContentTypes'),
                       url(r'^contenttypes/(?P<ctid>\d+)/group/$','Security.Views.ContentTypeViews.GroupSecurity'),
                       url(r'^contenttypes/create/$','Security.Views.ContentTypeViews.GroupSecurityCreateIndex'),
                       url(r'^contenttypes/create/new/$','Security.Views.ContentTypeViews.GroupSecurityCreate'),
                       #state_init
                       url(r'^init/state/create/$','Security.Views.StateViews.CreateNewStateIndex',{'init':1}),
                       url(r'^init/state/create/new/$','Security.Views.StateViews.CreateNewState',{'init':1}),
                    )
