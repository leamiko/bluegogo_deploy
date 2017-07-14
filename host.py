#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import salt.client
import memcache
from config import memcached_addr

class Host(object):
    def __init__(self,business,deploy_type):
        self.business = business
        self.deploy_type = deploy_type
        self.salt_obj = salt.client.LocalClient()
        self.business_all_host = self.fetch_business_host()
        self.host_grains_check()
        # print self.business_all_host

    def fetch_business_host(self):
        business_all_host = self.salt_obj.cmd("G@business:%s" % self.business,"grains.item",["business_ip"],expr_form='compound')
        return business_all_host

    def online(self):

        return "online"

    def gray(self):
        return "gray"

    def host_grains_set(self):
        host_name_li = self.business_all_host.keys()
        host_name_li.sort()
        print "....%s" % host_name_li
        gray_host_list = []
        if len(self.business_all_host) < 4:
            gray_host = host_name_li.pop(0)
            gray_host_list.append(gray_host)
            print "....%s" % gray_host_list
        else:
            from config import gray_host_num
            for i in xrange(gray_host_num):
                gray_host = host_name_li.pop(0)
                gray_host_list.append(gray_host)
        print host_name_li,"...."
        print gray_host_list,"...."
        self.grains_set("gray",gray_host_list)
        self.set_grains_memcache("gray",gray_host_list)
        self.grains_set("online",host_name_li)
        self.set_grains_memcache("online",host_name_li)

    def host_grains_check(self):
        get_host_list = self.salt_obj.cmd("G@business:%s and G@deploy_type:%s" %(self.business,self.deploy_type),"grains.item",["business_ip"],expr_form='compound').keys()
        get_host_list.sort()
        mem_host_list = self.get_grains_memcache()
        print "!!!!%s!!!!%s" %(get_host_list,mem_host_list)
        if get_host_list != mem_host_list:
            self.host_grains_set()


    def set_grains_memcache(self,deploy_type,host_list):
        mc = memcache.Client([memcached_addr],debug=True)
        mc.set("%s_%s" %(self.business,deploy_type),host_list)
        print mc.get("%s_%s" %(self.business,deploy_type)),".........."

    def get_grains_memcache(self):
        mc = memcache.Client([memcached_addr],debug=True)
        ret = mc.get("%s_%s" %(self.business,self.deploy_type))
        print ret,"........."
        return ret

    def host_expr_generate(self,host_list):
        target_expr = ""
        for i in host_list:
            if not target_expr:
                target_expr = "L@%s" % (i)
            else:
                target_expr = "%s,%i" % (target_expr, i)
        return target_expr

    def grains_set(self,deploy_type,host_list):
        target_expr = self.host_expr_generate(host_list)
        set_ret = self.salt_obj.cmd(target_expr, 'grains.setval', ["deploy_type", deploy_type], expr_form='compound')
