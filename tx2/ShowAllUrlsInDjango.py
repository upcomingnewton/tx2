
import urls

def show_urls(append,urllist, depth=0):
    for entry in urllist:
	    append =  append +  entry.regex.pattern[1:]
	    print append
            if hasattr(entry, 'url_patterns'):
            	show_urls(append,entry.url_patterns, depth + 1)


if __name__=="__main__":
	show_urls('/',urls.urlpatterns)


