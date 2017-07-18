#!/usr/bin/env python
#_*_ coding:utf-8 _*_

class Business(object):

    def __init__(self,business,deploy_type):
        self.business = business
        self.deploy_type = deploy_type

    def fetch_business_list(self):
        from config import business_list
        return business_list


