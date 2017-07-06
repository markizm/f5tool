#!/usr/bin/python

import bigsuds
import getpass
import json

class Ltmstuff(object):

    def __init__(self, ltm_ip, user, passwd, f5):
        self.ltm_ip = ltm_ip
        self.user = user
        self.passwd = passwd
        self.f5 = f5 

    ## get current stats for all virtual servers
    def vs_stats (self):
        vs_stats=self.f5.LocalLB.VirtualServer.get_all_statistics()
        for stats in vs_stats['statistics']:
            print stats['virtual_server'].values()[2]
            print stats['statistics'][8]['value']['low']

    ## get list of all virtual servers
    def vs_all (self):
        vs_list=self.f5.LocalLB.VirtualServer.get_list()
        for virtual in vs_list:
            print virtual

    ## get status of all virtual servers
    def vs_status (self):
        vs_list=self.f5.LocalLB.VirtualServer.get_list()
        for vl in vs_list:
            print vl
            print self.f5.LocalLB.VirtualServer.get_object_status([vl])[0]['enabled_status']

    ## get list of all pools
    def pool_all (self):
        pool_list=self.f5.LocalLB.Pool.get_list()
        for pl in pool_list:
            print pl

    ## get status of pool members
    def pm_status (self):
        pool_list=self.f5.LocalLB.Pool.get_list()
        for pl in pool_list:
            print self.f5.LocalLB.PoolMember.get_object_status([pl])[0][0]['member']
            print self.f5.LocalLB.PoolMember.get_object_status([pl])[0][0]['object_status']['enabled_status']

    ## get stats for all pools
    def pool_stats (self):
        pool_list=self.f5.LocalLB.Pool.get_all_statistics()
        for pl in pool_list['statistics']:
            print pl['pool_name']
            print pl['statistics'][4]['value']['low'] 

    ## get pool member stats
    def pm_stats (self):
        pool_list=self.f5.LocalLB.Pool.get_list()
        for pm in pool_list:
            print pm
            print self.f5.LocalLB.Pool.get_all_member_statistics([pm])[0]['statistics'][0]['member']
            print self.f5.LocalLB.Pool.get_all_member_statistics([pm])[0]['statistics'][0]['statistics'][4]['value']['low']

    # get list of irules and their definitions
    def irule_list (self, key, cert):
        rule_list=self.f5.LocalLB.Rule.query_all_rules()
        for irule in rule_list:
            json_text=json.dumps(irule)
            json_output=json.loads(json_text)
            print json_output['rule_name']
            print json_output['rule_definition']

    # create a new ssl profile on the load balancer
    def create_ssl (self):
        ssl_new=self.f5.LocalLB.ProfileClientSSL.create(key, cert)

    def get_ssl_profiles (self):
        ssl_prof = self.f5.LocalLB.ProfileClientSSL.get_list() 
        for ssllist in ssl_prof:
            return ssllist    
            
    def get_ssl_cert (self):
        obj = get_ssl_profiles()
        for ssls in obj:
            print self.f5.LocalLB.ProfileClientSSL.get_certificate_file(ssls) 
