from django.conf.urls.defaults import patterns,  url


urlpatterns = patterns('',
        #INDEX PAGES
        url(r'^register/$','alumni.Views.AlumniViews.RegisterIndex'),
        url(r'^register/post/$','alumni.Views.AlumniViews.Register'),
)
