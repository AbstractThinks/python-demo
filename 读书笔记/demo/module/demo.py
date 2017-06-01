"""
from os import makedirs, unlink, sep   #从os包中引入 makedirs.unlink,sep类
from os.path import dirname, exists, isdir, splitext  从 os包中的path类中引入 dirmame exists 等方法
import urllib.request   //引入 urllib resquest包
from urllib.parse import urlparse
from sys import argv
import html.parser as h   #给包html.parser 定义一个h别名
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import support
support.print_func("jesse")

# import support as demo
# demo.print_func("jesse")


from support_part import print_part_func
print_part_func("alvin")


from mod1 import mod_1
mod_1.print_mod_1_func("leslie")

# import mod1.mod_1
# mod1.mod_1.print_mod_1_func("leslie")
#
# # import mod1.mod_1 as demo
# # demo.print_mod_1_func("leslie")
#
# # from mod1.mod_1 import print_mod_1_func
# # print_mod_1_func("leslie")
#
# from mod1.mod2.mod_2 import print_mod_2_func
# print_mod_2_func("fen")


# “__name__ == '__main__'”是True,
# 但是我们如果从另外一个.py文件通过import导入该文件的时候，
# 这时__name__的值就是我们这个py文件的名字而不是__main__。
if __name__ == '__main__':
    print("hello")
