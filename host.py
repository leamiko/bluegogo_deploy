#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import salt.client


class Host(object):
    def __init__(self,business):
        self.salt_obj = salt.client.LocalClient()
        self.business_all_host = self.fetch_business_host(business)
        print self.business_all_host

    def fetch_business_host(self,business):
        business_all_host = self.salt_obj("G@business:%s" % business,"grains.item",["business_ip"],expr_form='compound')
        return business_all_host

    def online(self,deploy_type,business):

        return "online"

    def gray(self,deploy_type,business):
        return "gray"