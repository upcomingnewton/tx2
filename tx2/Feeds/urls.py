from django.conf.urls.defaults import patterns,  url
from tx2.Feeds.Views import NewsFeeds

urlpatterns = patterns('',

        url(r'^happenings/$','NewsFeeds()'),
)