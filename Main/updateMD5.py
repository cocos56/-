from Storer.api import insertToFiles, getMD5FromFiles
from Path.api import getFiles
from GetHash.api import getMD5

dl = [
	r'E:\OneDrive - 美国乡村蹲不下学院\学习视频'
]


def update(d):
	cnt = 0
	for i in getFiles(d):
		cnt += 1
		print(cnt, i)
		if getMD5FromFiles(i):
			continue
		md5 = getMD5(i)
		print(md5)
		# print(len(md5))
		insertToFiles(i, md5)


for i in dl:
	update(i)
