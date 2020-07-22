from Storer.api import getMD5FromFiles
from Path.api import getFiles


d1 = r'E:\OneDrive - 微信公众号奇乐帮\大型软件'
for i in getFiles(d1):
	md5 = getMD5FromFiles(i)
	print(md5)
