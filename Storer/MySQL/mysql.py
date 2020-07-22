from .Config.api import query, commit
from pymysql import escape_string


def insertToT():
    s = r'D:\视频教程\大数据\【开课吧】廖雪峰 · 2019大数据分析\开课吧介绍'
    cmd = r"""insert into t(`t`)value('%s')""" % escape_string(s)
    print(cmd)
    query(cmd)
    commit()


def insertToFiles(filePath, md5):
    cmd = r"""insert into files
    (`path`, `md5`)
    value('%s', '%s')
    """%(escape_string(filePath), md5)
    print(cmd)
    query(cmd)
    commit()

def getMD5FromFiles(filePath):
    cmd = r"""select `md5` from files where `path` = '%s'"""\
          % escape_string(filePath)
    print(cmd)
    return query(cmd)
