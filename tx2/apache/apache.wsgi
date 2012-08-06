import os, sys

sys.path.append('/var/www/vhosts/thoughtxplore.com/uiet/tx2/tx2')
sys.path.append('/var/www/vhosts/thoughtxplore.com/uiet/tx2/')
#sys.path.append('/opt/python2.7/lib/python2.7/site-packages/django')
#sys.path.append('/opt/python2.7/lib/python2.7/site-packages/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tx2.settings'
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
