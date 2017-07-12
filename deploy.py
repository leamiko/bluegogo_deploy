#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import sys
from host import Host
from business import Business
class BusinessDeploy(object):

    def __init__(self):
        self.deploy_type,self.business = sys.argv[1],sys.argv[2]
        self.deploy_type_list = self.fetch_deploy_type()
        self.host_obj = Host()
        self.business_obj = Business()
        self.business_list = self.business_obj.fetch_business_list()
        self.argv_parser()
        self.host_list = self.fetch_deploy_host(self.deploy_type,self.business)
        print self.host_list
        self.business_deploy()

    #参数验证
    def argv_parser(self):
        if len(sys.argv) != 3:
            sys.exit("\033[31;1mWrong number of parameters\033[0m")
        if self.deploy_type not in self.deploy_type_list:
            print("\033[31;1mWrong of parameters,deploy type does not exist\033[0m")
            sys.exit("\033[31;1mPlease choose deploy type %s \033[0m" % self.deploy_type_list)
        if self.business not in self.business_list:
            print ("\033[31;1mWrong of parameters,business does not exist\033[0m")
            sys.exit("\033[31;1mPlease choose business %s \033[0m" % self.business_list)

    #获取要发布的主机
    def fetch_deploy_host(self,deploy_type,business):
        fetch_host_method = getattr(self.host_obj,self.deploy_type)
        return fetch_host_method(deploy_type,business)

    #获取所有发布方法的列表
    def fetch_deploy_type(self):
        from config import deploy_type
        return deploy_type

    def business_deploy(self):
        pass