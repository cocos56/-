# -*- coding: UTF-8 -*-

import os
import shutil
import time

def copyRes(src, des):
    cmd = 'xcopy "' + src +'" \"' + des + '" /s /h /D /y'
    os.system(cmd)

cnt=0
def delRes(path, des, src):
    path2 = path.replace(des, src)
    if os.path.exists(path2):
        return
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
    global cnt
    cnt+=1
    print(cnt, path)

def updateRes(src, des):
    global cnt
    cnt=0
    print('正在从【',src,'】同步至【', des,'】',sep='')
    print('正在复制资源')
    copyRes(src, des)
    print('复制完毕')

    print('正在删除资源')
    for root, dirs, files in os.walk(des,topdown=True):
        for dir in dirs:
            delRes(os.path.join(root, dir), des, src)
        for file in files:
            delRes(os.path.join(root, file), des, src)
    print('删除完毕')

def run(li):
    while True:
        for i in li: updateRes(i[0], i[1])
        for i in range(60*60*24*7, 0, -1):
            print("距离下一轮更新还剩：", i, "秒。", end="", sep="")
            time.sleep(1)
            print("\r", end="", flush = True)

if __name__ == "__main__":
    li=[
        (r'E:\OneDrive - office 365 students and teachers\视频教程', r'Z:\视频教程')
    ]
    
    run(li)
    