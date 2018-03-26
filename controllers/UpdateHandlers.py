#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from controllers.HomeHandlers import BaseHandler, initializeBaseRequestHandler
from common.Base import result, MyGuid, my_datetime, Config, my_log
from common.mySeacher.myWhoosh.updateIndex import *


"""
    更新索引数据
"""


class UpdateIndexHandler(initializeBaseRequestHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        # if self.verifyFlag == 1 and self.status == 0:
        status = 2000
        try:
            indexDirectory = Config().get_content("indexFilePath")["filepath"]
            dbname = self.get_argument('dbname', None)
            # rowData 是json的dict类型数据
            rowData = self.get_argument('rowData', None)
            if not dbname or not rowData:
                raise ValueError
            if isinstance(rowData, str):
                rowData = json.loads(rowData)
            update_index(indexdir=indexDirectory, indexname=dbname, rowData=rowData)
            # return json.dumps(result(status=2000), ensure_ascii=False)
        except Exception as e:
            my_log.error(e)
            status = 5003
        return result(status=status)

        # else:
        #     return self.noLogin()

    def noLogin(self):
        return result(status=4005)
