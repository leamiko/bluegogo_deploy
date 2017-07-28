#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import sys,os
import salt.client
import subprocess
from config import nginx_config

class Business(object):

    def __init__(self,business,deploy_type):
        self.business = business
        self.deploy_type = deploy_type

    def fetch_business_list(self):
        from config import business_list
        return business_list

    def gray_nginx_templete(self,host_ip_list,tag=True):
        nginx_file = "%s%s" % (nginx_config["root_dir"], nginx_config[self.business])
        for i in host_ip_list:
            if tag:
                ret = subprocess.Popen("sed -i '/%s/s/^/#/' %s" % (i,nginx_file),shell=True, cwd='/tmp/',stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print ret.stdout.read(),ret.stderr.read()
            else:
                ret = subprocess.Popen("sed -i '/%s/s/^#*//' %s" % (i, nginx_file), shell=True, cwd='/tmp/',stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print ret.stdout.read(), ret.stderr.read()
            conf_ret = subprocess.Popen("grep %s %s" %(i,nginx_file),shell=True, cwd='/tmp/',stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print conf_ret.stdout.read(),conf_ret.stderr.read()
        return not ret.poll()

    def webserver_http_gray_before_set(self,host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list)
        return ret

    def weibao_http_gray_before_set(self,host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list)
        return ret

    def alipay_http_gray_before_set(self,host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list)
        return ret

    def baidu_http_gray_before_set(self,host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list)
        return ret

    def webserver_coreapi_gray_before_set(self, host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list)
        return ret

    def weibao_coreapi_gray_before_set(self, host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list)
        return ret

    def alipay_coreapi_gray_before_set(self, host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list)
        return ret

    def baidu_coreapi_gray_before_set(self, host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list)
        return ret

    def webserver_http_gray_after_set(self,host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list,False)
        return ret

    def weibao_http_gray_after_set(self,host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list,False)
        return ret

    def alipay_http_gray_after_set(self,host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list,False)
        return ret

    def baidu_http_gray_after_set(self,host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list,False)
        return ret


    def webserver_coreapi_gray_after_set(self, host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list, False)
        return ret


    def weibao_coreapi_gray_after_set(self, host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list, False)
        return ret


    def alipay_coreapi_gray_after_set(self, host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list, False)
        return ret


    def baidu_coreapi_gray_after_set(self, host_ip_list):
        ret = self.gray_nginx_templete(host_ip_list, False)
        return ret

