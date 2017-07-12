#!/usr/bin/env python
#_*_ coding:utf-8 _*_

class Business(object):

    def __init__(self):
        pass

    @staticmethod
    def fetch_business_list():
        from config import business_list
        return business_list
