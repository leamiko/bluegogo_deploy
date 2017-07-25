#!/usr/bin/env python
#_*_ coding:utf-8 _*_


business_list = ["mqtt","webserver_http","weibao_http","alipay_http","baidu_http","webserver_coreapi","weibao_coreapi","alipay_coreapi","baidu_coreapi"]
deploy_type = ["online","gray"]
memcached_addr = "127.0.0.1"
gray_host_num = 2
online_interval_num = 4

nginx_config = {
    "webserver_http":["443vpc-api.bluegogo.com.conf"],
    "weibao_http":["443vpc-api-weibao.bluegogo.com.conf"],
    "alypay_http":["443vpc-alipay-api.bluegogo.com.conf"],
    "baidu_http":["443vpc-baidu-api.bluegogo.com.conf"],
}