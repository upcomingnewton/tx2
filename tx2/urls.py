from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tx2.views.home', name='home'),
    url(r'^recruiters/$', 'tx2.views.recruitersIndex', name='home'),
    
    # url(r'^tx2/', include('tx2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^user/',include('Users.urls')),
    url(r'^security/',include('Security.urls')),
    url(r'^userreg/',include('UserReg.urls')),
    url(r'^userprofile/',include('UserProfile.urls')),
    url(r'^message/','Users.Views.UserViewIndex.ShowMessages'),
    url(r'^comm/',include('Misc.urls')),
    url(r'^communication/',include('Communication.urls')),
    url(r'^rss/',include('Feeds.urls'))
    
)
