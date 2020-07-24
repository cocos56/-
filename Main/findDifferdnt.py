from Path.api import getFiles
from os.path import exists, dirname
from os import system
from Storer.api import getMD5FromFiles


def findDiff(d1, d2):
	l1, l2, li = len(d1), len(d2), []
	for i in getFiles(d1):
		i2 = d2 + i[l1:]
		if not exists(i2):
			li.append([i, dirname(i2), dirname(i)])
		if getMD5FromFiles(i) != getMD5FromFiles(i2):
			li.append([i, dirname(i2), dirname(i)])
	for i in getFiles(d2):
		i2 = d1 + i[l2:]
		if not exists(d1 + i[l2:]):
			li.append([i, dirname(i2), dirname(i)])
	print(len(li))
	for i in li:
		print(i)
		print(i[0])
		input('Press enter key to continue.')
		system(r'start explorer "%s"' % i[1])
		system(r'start explorer "%s"' % i[2])


ds = [
	# (
	# 	r'E:\OneDrive - 微信公众号奇乐帮\大型软件',
	# 	r'\\1.coco56.top\大型软件'
	# ),
	# (
	# 	r'E:\OneDrive - 微信公众号奇乐帮\精品软件',
	# 	r'\\1.coco56.top\精品软件'
	# ),
	# (
	# 	r'E:\OneDrive - 微信公众号奇乐帮\开发相关',
	# 	r'\\1.coco56.top\开发相关'
	# ),
	# (
	# 	r'E:\OneDrive - 微信公众号奇乐帮\稀缺资源',
	# 	r'\\1.coco56.top\稀缺资源'
	# ),
	(
		r'E:\OneDrive - Office Everyday\学习视频',
		r'\\1.coco56.top\学习视频'
	),
]

for d in ds:
	print(d)
	findDiff(d[0], d[1])
