from pymysql import connect
from .host import host, port, database, user, password

# 创建Connection连接并获得Cursor对象
conn = connect(
	host=host, port=port, database=database,
	user=user, password=password, charset='utf8')

cs = conn.cursor()


def query(cmd):
	cs.execute(cmd)
	results = cs.fetchall()
	return results


def commit():
	"""
	# 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
	"""
	conn.commit()
