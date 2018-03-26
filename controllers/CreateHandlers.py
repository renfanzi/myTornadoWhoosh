#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json, os
from controllers.HomeHandlers import BaseHandler, initializeBaseRequestHandler
from common.Base import result, MyGuid, my_datetime, Config, my_log, WhooshParameter
from common.mySeacher.myWhoosh.createIndex import app


class MyTestHandler(BaseHandler):
    # executor = ThreadPoolExecutor(2)

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.asynchronous_get()

    def _get(self):
        user = self.get_argument('user', None)
        print("get", user)
        # ret = json.dumps(result(status=2000, value="<p>hello world !!! </p>"))
        ret = json.dumps('<a href=http://www.w3school.com.cn>W3School</a>')
        return ret

    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        user = self.get_argument('user', None)
        print("post", user)
        ret = result(status=2000, value="hello world!")
        return ret


class CreateProjectHandler(initializeBaseRequestHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        if self.verifyFlag == 1 and self.status == 0:
            return result(status=2000, value="hello world!")
        else:
            return self.noLogin()

    def noLogin(self):
        return result(status=4005)


"""
    创建索引 结构 + 数据
"""

class CreateIndexHandler(initializeBaseRequestHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        try:
            tableNameList = WhooshParameter.tableNameList
            dataBaseList = WhooshParameter.dataBaseList
            uniqueValueList = WhooshParameter.uniqueValueList
            indexDirectory = Config().get_content("indexFilePath")["filepath"]
            '''
            try:
                indexDirectory = Config().get_content("indexFilePath")["filepath"]
            except Exception as e:
                my_log.error(e)
                indexDirectory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'indexdir')
            '''
            app(tableNameList, dataBaseList, uniqueValueList, indexDirectory)
            return result(status=2000)
        except Exception as e:
            my_log.error(e)
            return result(status=5003)

    def noLogin(self):
        return result(status=4005)
