# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
""" 这个文件用来使celery启动的时候能够加载外面模块的文件 """

import os
import sys
import inspect

# 当前路径 megagame/celery_md
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# 父路径 megagame
parentdir = os.path.dirname(currentdir)

# 解析器路径加上父路径 fate
sys.path.insert(0, parentdir)
