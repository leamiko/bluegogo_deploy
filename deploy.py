#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import sys
from host import Host
from business import Business
class BusinessDeploy(object):

    def __init__(self,sys_argv):
        self.argvs = sys.argv
        self.deploy_type_list = self.fetch_deploy_type()
        self.argv_parser()
        self.host_list = Host.fetch_business_host()
        self.business_deploy()

    #参数验证
    def argv_parser(self):
        if len(sys.argv) != 3:
            sys.exit("\033[31;1mWrong number of parameters\033[0m")
        self.business_list = Business.fetch_business_list()
        if sys.argv[2] not in self.business_list:
            print ("\033[31;1mWrong of parameters,business does not exist\033[0m")
            sys.exit("\033[31;1mPlease choose business %s \033[0m" % self.business_list)
        if sys.argv[1] not in self.deploy_type_list:
            print("\033[31;1mWrong of parameters,deploy type does not exist\033[0m")
            sys.exit("\033[31;1mPlease choose deploy type %s \033[0m" % self.deploy_type_list)

    def fetch_host_list(self):
        pass

    def business_deploy(self):
        pass

    def fetch_deploy_type(self):
        from config import deploy_type
        return deploy_type