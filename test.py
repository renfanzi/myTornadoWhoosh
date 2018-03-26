#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys, time
#
# a = [{"VSerialNumber": "2018030710273529376223128138"}, {"VSerialNumber": "2018030710273529376223128139"}]
# from serialnumber import SerialNumber
# b = []
# for i in a:
#     c = [i for k in SerialNumber.SerialData if str(i["VSerialNumber"])==str(k["serialNumber"])]
#     if c:
#         b.append(c)
# print(b)


import requests

# ret = requests.post('http://192.168.1.137:8002/SelectSeacherComment', data={"clientContent": "用户"})
# ret = requests.post('http://192.168.1.137:8002/index', data={"clientContent": "用户"})
# print(ret.text)

ret  = requests.post("http://192.168.1.137:8002/CreateIndex")
print(ret.text)

