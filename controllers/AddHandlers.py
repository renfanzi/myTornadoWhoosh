#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from controllers.HomeHandlers import BaseHandler, initializeBaseRequestHandler
from common.Base import result, MyGuid, my_datetime, Config, my_log
from common.mySeacher.myWhoosh.addIndex import *


"""
    添加索引数据
"""


class AddIndexHandler(initializeBaseRequestHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        # if self.verifyFlag == 1 and self.status == 0:
        try:
        # print("add")
            indexDirectory = Config().get_content("indexFilePath")["filepath"]
            dbname = self.get_argument('dbname', None)
            # print(dbname)
            # rowData 是json的dict类型数据
            rowData = self.get_argument('rowData', None)
            # print(rowData)
            if not dbname or not rowData:
                raise ValueError
            if isinstance(rowData, str):
                rowData = json.loads(rowData)
                if isinstance(rowData, list):
                    for i in rowData:
                        incremental_index(indexdir=indexDirectory, indexname=dbname, rowData=i)
                elif isinstance(rowData, dict):
                    incremental_index(indexdir=indexDirectory, indexname=dbname, rowData=rowData)
            return result(status=2000)
        except Exception as e:
            my_log.error(e)
            return result(status=5003)

        # else:
        #     return self.noLogin()

    def noLogin(self):
        return result(status=4005)
