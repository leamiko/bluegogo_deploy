#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import sys

class Business(object):

    def __init__(self,business,deploy_type):
        self.business = business
        self.deploy_type = deploy_type

    def fetch_business_list(self):
        from config import business_list
        return business_list

    def webserver_http_gray_before_set(self):
        print self.business,self.deploy_type

    def weibao_http_gray_before_set(self):
        print self.business,self.deploy_type

    def alipay_http_gray_before_set(self):
        print self.business,self.deploy_type,"LLL"

    def baidu_http_gray_before_set(self):
        print self.business,self.deploy_type

    def webserver_http_gray_after_set(self):
        print self.business,self.deploy_type

    def weibao_http_gray_after_set(self):
        print self.business,self.deploy_type

    def alipay_http_gray_after_set(self):
        print self.business,self.deploy_type

    def baidu_http_gray_after_set(self):
        print self.business,self.deploy_type

    def mqtt_gray_before_set(self):
        print self.business,self.deploy_type

    def mqtt_gray_after_set(self):
        print self.business,self.deploy_type

