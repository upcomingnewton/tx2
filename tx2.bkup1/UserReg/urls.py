from django.conf.urls.defaults import patterns,  url


urlpatterns = patterns('',
	#/userreg/
        url(r'^users/selected/$','UserReg.Views.UserRegViews.AddUserForReg'),
        url(r'^users/$','UserReg.Views.UserRegViews.AddUserForRegIndex'),
)               
