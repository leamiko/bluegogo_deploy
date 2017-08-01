#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import sys
import salt.client
import memcache
from config import memcached_addr

class Host(object):
    def __init__(self,business,deploy_type):
        self.business = business
        self.deploy_type = deploy_type
        self.salt_obj = salt.client.LocalClient()
        self.business_all_host = self.fetch_business_host()
        # print self.business_all_host
        self.deploy_host_dict = self.salt_obj.cmd("G@business:%s and G@deploy_type:%s" % (self.business, self.deploy_type),"grains.item", ["business_ip"], expr_form='compound')
        # print self.deploy_host_dict

    def fetch_business_host(self):
        business_all_host = self.salt_obj.cmd("G@business:%s" % self.business,"grains.item",["business_ip"],expr_form='compound')
        return business_all_host

    def host_grains_set(self):
        host_name_li = self.business_all_host.keys()
        host_name_li.sort()
        print "%s所有服务器列表：%s" %(self.business,host_name_li)
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
        print "其中灰度发布服务器为%s\n,线上发布服务器为：%s\n" %(gray_host_list,host_name_li)
        print "开始设置服务器deploy_type信息......."
        self.deploy_type_grains_set("gray",gray_host_list)
        # self.set_grains_memcache("gray",gray_host_list)
        self.deploy_type_grains_set("online",host_name_li)
        # self.set_grains_memcache("online",host_name_li)
        print "开始设置服务器gray_ip信息......"
        self.gray_ip_grains_set(gray_host_list,host_name_li)
        return gray_host_list,host_name_li

    def host_grains_check(self):
        get_host_list = self.deploy_host_dict.keys()
        get_host_list.sort()
        mem_host_list = self.get_grains_memcache()
        # print "!!!!%s!!!!%s" %(get_host_list,mem_host_list)
        if get_host_list != mem_host_list:
            self.host_grains_set()
            self.deploy_host_dict = self.salt_obj.cmd("G@business:%s and G@deploy_type:%s" % (self.business, self.deploy_type),"grains.item", ["business_ip"], expr_form='compound')
            # if self.deploy_type == "online":
            #     sys.exit("\033[31;1mBusiness host is changed,Please rerun grayscale release \033[0m")


    def set_grains_memcache(self,deploy_type,host_list):
        mc = memcache.Client([memcached_addr],debug=True)
        mc.set("%s_%s" %(self.business,deploy_type),host_list)
        print mc.get("%s_%s" %(self.business,deploy_type)),".........."

    def get_grains_memcache(self):
        mc = memcache.Client([memcached_addr],debug=True)
        ret = mc.get("%s_%s" %(self.business,self.deploy_type))
        # print ret,"........."
        return ret

    def host_expr_generate(self,host_list):
        target_expr = ""
        for i in host_list:
            if not target_expr:
                target_expr = "L@%s" % (i)
            else:
                target_expr = "%s,%s" % (target_expr, i)
        return target_expr

    def deploy_type_grains_set(self,deploy_type,host_list):
        target_expr = self.host_expr_generate(host_list)
        set_ret = self.salt_obj.cmd(target_expr, 'grains.setval', ["deploy_type", deploy_type], expr_form='compound')
        print set_ret

    def gray_ip_grains_set(self,gray_host_list,online_host_li):
        gray_host_target_expr = self.host_expr_generate(gray_host_list)
        gray_ip_list = self.salt_obj.cmd(gray_host_target_expr,"grains.get",["business_ip"],expr_form='compound').values()
        ip_dict = {}
        for i in range(len(gray_ip_list)):
            ip_dict[gray_ip_list[i]] = online_host_li[i::len(gray_ip_list)]
        print ip_dict,"gray_ip_grains_set......."
        for gray_ip,host_list in ip_dict.items():
            target_expr = self.host_expr_generate(host_list)
            set_ret = self.salt_obj.cmd(target_expr, 'grains.setval', ["gray_ip", gray_ip], expr_form='compound')
            print set_ret

    def fetch_host_ip(self,target_expr):
        host_ip_list = self.salt_obj.cmd(target_expr,"grains.get", ["business_ip"], expr_form='compound').values()
        return host_ip_list

    def fetch_nginx_host(self):
        nginx_host_list = self.salt_obj.cmd("G@busienss:nginx","grains.item", ["business_ip"], expr_form='compound').keys()
        return nginx_host_list