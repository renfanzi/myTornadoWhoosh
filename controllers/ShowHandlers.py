#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from controllers.HomeHandlers import BaseHandler, initializeBaseRequestHandler
from common.Base import result, MyGuid, my_datetime, Config, my_log, WhooshParameter, MyPymysql
from common.mySeacher.myWhoosh.selectSeacherData import *
from serialnumber import SerialNumber
from core.SelectDetail import *


class SelectSeacherCommentHandler(initializeBaseRequestHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        # if self.verifyFlag == 1 and self.status == 0:
        try:
            status = 2000
            indexdir = Config().get_content("indexFilePath")["filepath"]
            indList = WhooshParameter.tableNameList
            # 客户端传递过来查询的内容
            clientContent = self.get_argument("clientContent", None)
            if clientContent:
                data = SearchData(indexdir, indList, clientContent)
            else:
                raise ValueError
        except Exception as e:
            my_log.error(e)
            status = 5003
            data = [[], [], []]
        return result(status=status, value=data)

            # else:
            #     return self.noLogin()

    def noLogin(self):
        return result(status=4005)
