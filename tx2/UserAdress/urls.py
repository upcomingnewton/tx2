from django.conf.urls.defaults import patterns,  url


urlpatterns = patterns('',
        url(r'^city/$','UserAdress.Views.CityViews.CityIndex'),
        url(r'^city/add/$','UserAdress.Views.CityViews.CityIndex'),
        url(r'^city/add/post/$','UserAdress.Views.CityViews.CityAdd'),

        url(r'^state/$','UserAdress.Views.StateViews.StateIndex'),
        url(r'^state/add/$','UserAdress.Views.StateViews.StateIndex'),
        url(r'^state/add/post/$','UserAdress.Views.StateViews.StateAdd'),

        url(r'^country/$','UserAdress.Views.CountryViews.CountryIndex'),
        url(r'^country/add/$','UserAdress.Views.CountryViews.CountryIndex'),
        url(r'^country/add/post/$','UserAdress.Views.CountryViews.CountryAdd'),
        
        url(r'^adress/$','UserAdress.Views.AdressViews.AdressIndex'),
        url(r'^adress/add/post/$','UserAdress.Views.AdressViews.AddAdress'),
        url(r'^adress/edit/post/$','UserAdress.Views.AdressViews.EditAdress'),

        url(r'^contactinfo/$','UserAdress.Views.ContactInfoViews.ContactInfoIndex',{'UserID':-1}),
        url(r'^contactinfo/edit/post/$','UserAdress.Views.ContactInfoViews.ContactInfoEdit'),
        url(r'^contactinfo/(?P<UserID>\d+)/$','UserAdress.Views.ContactInfoViews.ContactInfoIndex'),
)
