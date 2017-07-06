import sys
import getpass
from ltmstuff import * 

qry = input("query?")

ltm_ = input("enter ltm ip in quotes: ")

pwd=getpass.getpass(prompt='enter your ltm password:  ')

obj=bigsuds.BIGIP(hostname=ltm_,username='<your_uid>',password=pwd,debug=True)

ltm = Ltmstuff('ltm', '<your_uid>', pwd, obj)

if qry == 'vip_stats':
    ltm.vs_stats()

elif qry == 'all_vips':
    ltm.vs_all()

elif qry == 'vip_status':
    ltm.vs_status()

elif qry == 'all_pools':
    ltm.pool_all()

elif qry == 'all_pools':
    ltm.pool_all()

elif qry == 'ssl_list':
    ltm.get_ssl_profiles()

elif qry == 'pool_status':
    ltm.pool_stats()

elif qry == 'pm_status':
    ltm.pm_status()

elif qry == 'mem_stats':
    ltm.pm_stats()

elif qry == 'irules':
    ltm.irule_list()

elif qry == 'ssl_cert':
    ltm.get_ssl_cert()

else:
    print "closing app"


