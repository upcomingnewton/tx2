from django.conf.urls.defaults import patterns,  url

urlpatterns = patterns('',
    #/userreg/
        url(r'^Admin/Notice/$','Communication.Views.AdminCommViews.adminNoticeIndex'),
        url(r'^Admin/Notice/Post$','Communication.Views.AdminCommViews.adminNoticePost'),
        url(r'^Admin/News/$','Communication.Views.AdminCommViews.adminNewsIndex'),
        url(r'^Admin/News/Post$','Communication.Views.AdminCommViews.adminNewsPost'),
        
)               