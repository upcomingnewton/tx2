
import urls

def show_urls(append,urllist, depth=0):
    for entry in urllist:
	    append =  append +  entry.regex.pattern[1:]
	    print append
            if hasattr(entry, 'url_patterns'):
            	show_urls(append,entry.url_patterns, depth + 1)
            	
def MakeAllUrls(append,urllist,_list, depth=0):
    for entry in urllist:
	    t =  append +  entry.regex.pattern[1:]
	    _list.append(t[:-1])
            if hasattr(entry, 'url_patterns'):
            	MakeAllUrls(t,entry.url_patterns,_list, depth + 1)


if __name__=="__main__":
	#show_urls('/',urls.urlpatterns)
	_list = []
	MakeAllUrls('/',urls.urlpatterns,_list, depth=0)
	for x in _list:
	  print x


