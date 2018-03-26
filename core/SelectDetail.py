#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json, requests
from controllers.HomeHandlers import BaseHandler, initializeBaseRequestHandler
from common.Base import result, MyGuid, my_datetime, Config, my_log, WhooshParameter, MyPymysql, ComplexEncoder
from common.mySeacher.myWhoosh.selectSeacherData import *
from serialnumber import SerialNumber

"""
    查看索引搜索数据
"""


def retsearch(results):
    projectList = []
    questList = []
    variableList = []

    variableIDList = []
    groupProjectList = []  # grouping project list
    groupQuesList = []  # grouping ques list
    '''
        过滤得到有效数据
    '''
    for i in results:
        if "PSerialNumber" in i:
            if int(i["ProjectStatus"]) == 1:
                if int(i["ProjectPublic"]) == 2:
                    projectList.append(i)
        if "QSerialNumber" in i:
            if int(i["QuesStatus"]) == 1:
                if int(i["QuesPublic"]) == 2:
                    questList.append(i)
        if "VSerialNumber" in i:
            if int(i["VarStatus"]) == 1:
                variableList.append(i)
    '''
        根据不同serial number 得到不同的variableid list
        分别请求
    '''
    for k in SerialNumber.SerialData:

        subVairableList = []
        subProjectList = [i for i in projectList if str(i["PSerialNumber"]) == str(k["serialNumber"])]
        subQuesList = [i for i in questList if str(i["QSerialNumber"]) == str(k["serialNumber"])]
        for i in variableList:

            if str(i["VSerialNumber"]) == str(k["serialNumber"]):
                if i["VariableID"] not in subVairableList:
                    subVairableList.append(i["VariableID"])

        if subVairableList:
            variableIDList.append({"serialNumber": k["serialNumber"], "variableList": subVairableList, "url": k["url"],
                                   "name": k["name"]})
        if subProjectList:
            groupProjectList.append({"serialNumber": k["serialNumber"], "projectList": subProjectList, "url": k["url"],
                                     "name": k["name"]})
        if subQuesList:
            groupQuesList.append({"serialNumber": k["serialNumber"], "quesList": subQuesList, "url": k["url"],
                                  "name": k["name"]})
    return groupProjectList, groupQuesList, variableIDList


def SearchData(indexdir, indList, clientContent):
    ret = app(indexdir=indexdir, indList=indList, clientContent=clientContent)
    daprojectList, questList, variableIDList = retsearch(ret)

    newVariableList = []

    def yieldRequest():
        for subVariable in variableIDList:
            '''
                1. 得到URL
                2. 发送请求， 然后获得数据， 在放到列表里返回
            '''
            subURL = \
            [i["url"] for i in SerialNumber.SerialData if str(i["serialNumber"]) == str(subVariable["serialNumber"])][
                0]
            URL = subURL + "/AnonymousSearchReturnData"

            try:
                # 加入生成器
                subVariable["variableList"] = requests.post(URL,
                                    data={"variableList": json.dumps(subVariable["variableList"], cls=ComplexEncoder)})
                yield subVariable
                """
                同步方式写法， 后更改为异步
                # if ret.status_code == 200:
                #     subWhooshReturnData = json.loads(ret.text)
                #     if subWhooshReturnData["statuscode"] == 2000:
                #         if subWhooshReturnData["value"]:
                #             newVariableList.append(subWhooshReturnData["value"])
                """
            except Exception as e:
                my_log.error(e)

    for subReq in yieldRequest():
        if subReq["variableList"].status_code == 200:
            subWhooshReturnData = json.loads(subReq["variableList"].text)
            if subWhooshReturnData["statuscode"] == 2000:
                if subWhooshReturnData["value"]:
                    subReq["variableList"] = subWhooshReturnData["value"]
                    newVariableList.append(subReq)

    return daprojectList, questList, newVariableList
