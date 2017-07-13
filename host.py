#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import salt.client


class Host(object):
    def __init__(self,business):
        self.salt_obj = salt.client.LocalClient()
        self.business_all_host = self.fetch_business_host(business)
        print self.business_all_host

    def fetch_business_host(self,business):
        business_all_host = self.salt_obj.cmd("G@business:%s" % business,"grains.item",["business_ip"],expr_form='compound')
        return business_all_host

    def online(self,deploy_type,business):

        return "online"

    def gray(self,deploy_type,business):
        self.gray_host_set()
        return "gray"

    def gray_host_set(self):
        host_name_li = self.business_all_host.keys()
        host_name_li.sort()
        print host_name_li
        if len(self.business_all_host) < 4:
            gray_host_list = [host_name_li[0]]
        else:
            gray_host_list = [host_name_li[0],host_name_li[1]]
        target_expr = ""
        for i in gray_host_list:
            if not target_expr:
                target_expr = "L@%s" %(i)
            else:
                target_expr = "%s,%i" %(target_expr,i)
        print target_expr
        set_ret = self.salt_obj.cmd(target_expr,'grains.setval',["deploy_type","gray"],expr_form='compound')
        print set_ret

    def gray_host_check(self):
        pass