from Storer.api import insertToFiles, getMD5FromFiles
from Path.api import getFiles
from GetHash.api import getMD5

dl = [
	r'E:\OneDrive - 微信公众号奇乐帮',
	r'\\1.coco56.top\大型软件',
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
