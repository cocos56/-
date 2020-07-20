from .Config.api import query, commit, Timestamp
from pymysql import escape_string


def insertToT():
    s = r'D:\视频教程\大数据\【开课吧】廖雪峰 · 2019大数据分析\开课吧介绍'
    cmd = r"""insert into t(`t`)value('%s')""" % escape_string(s)
    print(cmd)
    query(cmd)
    commit()


def insertToChangVideoSpeed(path, speed, duration,
                            oldSize, newSize, oldFPS, newFPS,
                            oldWidth, oldHeigh, newWidth, newHeigh):
    cmd = r"""insert into chang_video_speed
    (`year`, `month`, `day`, `hour`, `minute`,
    `second`, `path`, `speed`, `duration`,
    `oldSize`, `newSize`, `oldFPS`, `newFPS`,
    `oldWidth`, `oldHeigh`, `newWidth`, `newHeigh`)
    value('%s', '%s', '%s', '%s', '%s',
    '%s', '%s', '%s', '%s',
    '%s', '%s', '%s', '%s',
    '%s', '%s', '%s', '%s')
    """ % (Timestamp.year, Timestamp.month, Timestamp.day, Timestamp.hour, Timestamp.minute,
           Timestamp.second, escape_string(path), speed, duration,
           oldSize, newSize, oldFPS, newFPS,
           oldWidth, oldHeigh, newWidth, newHeigh)
    print(cmd)
    query(cmd)
    # commit()


def insertToDelStr(fatherDir, oldName, newName):
    cmd = r"""insert into del_str
        (`year`, `month`, `day`, `hour`, `minute`,
        `second`, `fatherDir`, `oldName`, `newName`)
        value('%s', '%s', '%s', '%s', '%s',
        '%s', '%s', '%s', '%s')
        """ % (Timestamp.year, Timestamp.month, Timestamp.day, Timestamp.hour, Timestamp.minute,
               Timestamp.second, escape_string(fatherDir), oldName, newName)
    print(cmd)
    query(cmd)
    # commit()


