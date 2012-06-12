
import os
hostname = os.environ['HOSTNAME']
print hostname

if( hostname == 'linux-4bv4.site' ):
	from conf.nitin_settings import *
