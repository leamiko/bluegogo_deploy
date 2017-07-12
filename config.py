#!/usr/bin/env python
#_*_ coding:utf-8 _*_


deploy_dic = {
    "interval_num":4,
    "online_pick_method":"iptables",
    "gray_pick_method":"nginx",
    "online":False,
    "deploy_type_li":["tomcat","jar","static"]
}

business_list = ["mqtt","coreapi","webserver"]
deploy_type = ["online","gray"]