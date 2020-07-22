from os import walk
from os.path import join

files = []
dirs = []


def init(workDir):
    files.clear()
    dirs.clear()
    for root, ds, fs in walk(workDir):
        for i in fs:
            temp = join(root, i)
            files.append(temp)
        for i in ds:
            temp = join(root, i)
            dirs.append(temp)


def getFiles(workDir):
    init(workDir)
    return files


def getDirs(initFlag=True):
    if initFlag:
        init()
    return dirs
