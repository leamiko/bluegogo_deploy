#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import salt.client


class Host(object):
    def __init__(self):
        # self.salt_obj = salt.client.LocalClient()
        pass

    def fetch_business_host(self):
        self.host_list = self.salt_obj()

    def online(self,deploy_type,business):
        return "online"

    def gray(self,deploy_type,business):
        return "gray"