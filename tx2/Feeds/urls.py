from django.conf.urls.defaults import patterns,  url
from tx2.Feeds.Views import NewsFeeds 


feeds = {
         'rss': NewsFeeds().NewsIntemFeeds,
         
         }



urlpatterns = patterns('',

url(
        r'^news/(?P<url>.*)$', 
        'django.contrib.syndication.views.feed',
        {'feed_dict': feeds},
        name='feeds'
    ),       

)