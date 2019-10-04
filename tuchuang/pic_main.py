#!/usr/bin/env python
# coding=utf-8

import pic2
import oss2
import uuid
import pyperclip
import sys
import time
import os
from PIL import Image
import sys


def is_img(ext) :
    if ext in ['.jpg', '.png', '.jepg']:
        return 1
    else :
        return 0

def is_exist(file):
    return os.path.exists(file)

def gen_remote_name(srcname):
    name = uuid.uuid4().__str__().replace('-', '').upper()
    srcname = str(srcname).rsplit('.')
    data = time.strftime("%Y-%m-%d-%H")
    return "%s/%s/%s" % (data, name, srcname[-1])

if __name__ == "__main__":
    up = pic2.Picbed("xxx", "xxx", "xxx", "xxx")
    if len(sys.argv) == 1:
        im = pyperclip.paste()
        srcname = im
    else :
        srcname = sys.argv[1]

    if is_exist(srcname):
        if is_img(os.path.splitext(srcname)[1]):
            ret = up.upfile(gen_remote_name(srcname), srcname)
            pyperclip.copy(ret)
        else :
            print("格式错误")
    else :
        print("无效路径")
