import urllib.request

with urllib.request.urlopen('https://www.python.org/') as stream:
	print(stream.read(300).decode('utf-8'))
	# print(stream.getUrl())
	print(stream.info())
	# print(stream.getCode())

