#!/usr/bin/env python
#_*_ coding:utf-8 _*_


business_list = ["mqtt","webserver_http","weibao_http","alipay_http","baidu_http","webserver_coreapi","weibao_coreapi","alipay_coreapi","baidu_coreapi"]
deploy_type = ["online","gray"]
memcached_addr = "127.0.0.1"
gray_host_num = 2
online_interval_num = 4

nginx_config = {
    "root_dir":"/apps/srv/salt/base/files/prod/bluegogo_nginx_prod/conf/conf.d/",
    "webserver_http":"api.bluegogo.com.conf",
    "webserver_coreapi":"coreapi.bluegogo.com.conf",
    "weibao_http":"api-weibao.bluegogo.com.conf",
    "weibao_coreapi":"coreapi-weibao.bluegogo.com.conf",
    "alypay_http":"alipay-api.bluegogo.com.conf",
    "alypay_coreapi":"alipay-coreapi.bluegogo.com.conf",
    "baidu_http":"baidu-api.bluegogo.com.conf",
    "baidu_coreapi":"baidu-coreapi.bluegogo.com.conf"
}

business_pkg_attr = {
    "webserver_http":{
        "pkg_dir": "/apps/srv/salt/base/files/prod/bluegogo_web_http_prod",
        "pkg_name": "bluegogo_backend_http-1.0.war"
    },
}