from Path.api import getFiles
from os.path import exists, dirname
from os import system

d1 = r'E:\OneDrive - 微信公众号奇乐帮\大型软件'
l1 = len(d1)
d2 = r'\\1.coco56.top\大型软件'
l2 = len(d2)

li = []

for i in getFiles(d1):
	i2 = d2+i[l1:]
	if not exists(i2):
		li.append([i, dirname(i2), dirname(i)])


for i in getFiles(d2):
	i2 = d1+i[l2:]
	if not exists(d1+i[l2:]):
		li.append([i, dirname(i2), dirname(i)])

for i in li:
	# print(i)
	print(i[0])
	input('Press enter key to continue.')
	system(r'start explorer "%s"' % i[1])
	system(r'start explorer "%s"' % i[2])
