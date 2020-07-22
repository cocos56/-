import hashlib


def getMD5(filePath):
	hashRule = hashlib.md5()
	f = open(filePath, 'rb')
	while True:
		b = f.read(1024 * 1024 * 8)
		if not b:
			break
		hashRule.update(b)
	f.close()
	return hashRule.hexdigest()
