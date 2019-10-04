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
    BUCKET_NAME = ""
    ENDPOINT = ""
    __ACCESS_KEY_ID = ""
    __ACCESS_KEY_SECRET = ""

    def __init__(self, name, point, id, secret):
        self.BUCKET_NAME = name
        self.ENDPOINT = point 
        self.__ACCESS_KEY_ID = id
        self.__ACCESS_KEY_SECRET = secret
        self.auth = oss2.Auth(self.__ACCESS_KEY_ID, self.__ACCESS_KEY_SECRET)
        self.bucket = oss2.Bucket(self.auth, self.ENDPOINT, self.BUCKET_NAME)
    
    def upfile(self, remotename, srcname):
        self.bucket.put_object_from_file(remotename, srcname)
        return "![](https://%s.%s/%s)" % (self.BUCKET_NAME, self.ENDPOINT, srcname)



