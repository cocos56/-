from os.path import exists
from shutil import rmtree
from time import sleep
from datetime import datetime

path = r'E:\OneDrive - office 365 students and teachers\视频教程\Python\87、Python接口测试框架实战与自动化进阶'
cnt = 0

while True:
    if exists(path):
        rmtree(path)
        cnt += 1
        print(cnt, datetime, path)
    sleep(3)