#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import sys
from host import Host
class BusinessDeploy(object):

    def __init__(self,sys_argv):
        self.argvs = sys.argv
        self.argv_parser()
        self.host_list = Host.fetch_business_host()
        self.business_deploy()

    def argv_parser(self):
        pass

    def fetch_host_list(self):
        pass

    def business_deploy(self):
        pass