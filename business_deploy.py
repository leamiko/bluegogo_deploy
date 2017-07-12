#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import sys,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print BASE_DIR
sys.path.append(BASE_DIR)
from deploy import BusinessDeploy

if __name__ == '__main__':
    business_deploy = BusinessDeploy()

