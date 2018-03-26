#!/usr/bin/env python
# -*- coding:utf-8 -*-


from controllers.CreateHandlers import *
from controllers.AddHandlers import *
from controllers.UpdateHandlers  import *
from controllers.ShowHandlers  import *

urls = list()

testUrls = [(r'/index', MyTestHandler), ]

createUrls = [
    #(r'/CreateProject', CreateProjectHandler),

    # ----- 创建索引 ----- #
    (r'/CreateIndex', CreateIndexHandler),
]

addUrls = [
    # ----- 添加索引 ----- #
    (r'/AddIndex', AddIndexHandler),
]

updateUrls = [
    # ----- 修改索引 ----- #
    (r'/UpdateIndex', UpdateIndexHandler),
]

showUrls = [
    # ----- 搜索数据 ----- #
    (r'/SelectSeacherComment', SelectSeacherCommentHandler)
]

urls += testUrls + createUrls + addUrls + showUrls + updateUrls
