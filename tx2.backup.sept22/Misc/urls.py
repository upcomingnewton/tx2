from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
                       # states
                       url(r'^notice/iframe/(?P<noticeid>\d+)/$','Misc.CommViews.NoticeIndex'),
                       url(r'^test/','Misc.CommViews.TestIndex')
                    )
