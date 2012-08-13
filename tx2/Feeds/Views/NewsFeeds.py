from django.contrib.syndication.views import Feed
from tx2.Communication.models import Messages
from tx2.Communication.BusinessFunctions.CommunicationTypeFunctions import CommunicationTypeFnx
from cPickle import dumps, loads

class NewsIntemFeeds(Feed):
    
    title="Happenings @ UIET RSS Feeds"
    link="http://uiet.thoughtxplore.com"
    descriptions="All the latest News and events of UIET PU"

    def items(self):
        commtypeID=CommunicationTypeFnx().getCommunicationTypeIDbyName("NOTICES")
        return Messages.objects.filter(CommunicationType=commtypeID).order_by('Timestamp')
    def item_title(self, item):
        return loads(item.Title.decode("base64").decode("zip"))
    def item_content(self,item):
        return loads(item.Content.decode("base64").decode("zip"))
   
    