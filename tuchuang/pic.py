#!/usr/bin/env python
# coding=utf-8

import oss2
import uuid
import pyperclip
import sys
import time
import os
from PIL import Image
import sys

class Picbed :
    def __init__(self, name, point, id, secret) :
        self.BUCKET_NAME = name
        self.ENDPOINT = point
        self.ACCESS_KEY_ID = id
        self.ACCESS_KEY_SECRET = secret
        self.Url = ['']
    def is_img(self, str) :
        if str in ['.jpg', '.git', '.png', '.jpeg']:
            return 1
        else :
            return 0
    def upfile(self, File):
        auth = oss2.Auth(self.ACCESS_KEY_ID, self.ACCESS_KEY_SECRET)
        bucket = oss2.Bucket(auth, self.ENDPOINT, self.BUCKET_NAME)

        Time = time.strftime("%Y.%m.%d-%H")
        Uuid = uuid.uuid4()
        path = Time + '/' + str(Uuid) + '.png'
        with open(File, "rb") as fileobj:
            fileobj.seek(0, os.SEEK_SET)
            #current = fileobj.tell()
            bucket.put_object(path, fileobj)
        re_str = "![](https://%s.%s/%s)" % (self.BUCKET_NAME, self.ENDPOINT, path)
        self.Url[0] = re_str + " "
        print(re_str)
        pyperclip.copy(self.Url[0])
            
obj = Picbed("deng-feng", "oss-cn-beijing.aliyuncs.com", "LTAI4Fbiqo58HHBK4BtTKQCP", "xoD9VI60gNQFzIIrOIhbJmHrx9Zhom")
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        objfile = sys.argv[i]
        if os.path.exits(objfile):
            if obj.is_img(os.path.splitext(objfile)[1]):
                print(objfile)
                obj.upfile(objfile)
            else :
                print("格式不符")
                exit
        else :
            print("无效路径")
            exit
else :
    temp = pyperclip.paste()
    print(temp)
    if obj.is_img(temp[-4 : len(temp)]):
        obj.upfile(temp)
    else :
        print("格式不符")

