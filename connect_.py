import sys
import getpass
from ltmstuff import * 

ltm_ = input("enter ltm ip in quotes: ")

pwd=getpass.getpass(prompt='enter your ltm password:  ')

obj=bigsuds.BIGIP(hostname=ltm_,username='<your_uid>',password=pwd,debug=True)

ltm = Ltmstuff('ltm', '<your_uid>', pwd, obj)

#
# def sys_info (self):
#    infos = self.f5.System.SystemInfo.get_memory_usage_information()
#    print infos['used_memory']
#    print infos['total_memory']
#
#
# sys_info(ltm)
#
# def sys_info (self):
#    infos = self.f5.System.SystemInfo.get_memory_usage_information()
#    return infos
#
# sys_info(ltm)['used_memory']
#
